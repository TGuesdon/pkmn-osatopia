#!/usr/bin/env python3
"""Converts Dofus artwork into GBA battle sprites (front + back, 64x64, one shared 16-colour palette).

Source layout (e.g. ~/Dev/perso/imgToGBASprite/source):
  <name>.png       front, transparent background (already mirrored)
  <name>_back.png  back, plain white background (shadows are removed by segmentation)

Workflow:
  1. ./run.sh --src <dir> [names...]   generate previews into preview/ (+ audit in preview/index.json)
  2. ./dev_scripts/dex_viewer/serve.sh  tick « Comparer avec l'aperçu » to review them
  3. ./run.sh --apply [names...]        copy previews into graphics/pokemon/<name>/
  4. touch up graphics/pokemon/<name>/*.png by hand (indexed 16 colours, e.g. Aseprite); later
     --apply runs skip those files automatically (applied.json remembers what the script wrote)

Per-monster tuning and explicitly protected sprites live in overrides.json. Every artwork is fitted
to the same box, so each monster gets a "taille" (minuscule, petit, moyen, grand, enorme; see
defaults.tailles) to keep their relative sizes readable; without one it fills the whole box.
./sizes.py opens a page to pick them with the sprites shown side by side, family by family.
"""
import argparse
import hashlib
import json
import shutil
import sys
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
GFX_DIR = REPO / "graphics" / "pokemon"
PREVIEW_DIR = HERE / "preview"
CACHE_DIR = HERE / ".cache"
TRANSPARENT = (98, 156, 131)  # palette index 0, replaced by transparency in game
SIZE = 64


# ---------- Config ----------

def load_overrides():
    data = json.loads((HERE / "overrides.json").read_text())
    return data["defaults"], data.get("monsters", {})


def config_for(name, defaults, monsters):
    cfg = json.loads(json.dumps(defaults))
    for key, value in monsters.get(name, {}).items():
        if isinstance(value, dict) and isinstance(cfg.get(key), dict):
            cfg[key].update(value)
        else:
            cfg[key] = value
    if "taille" in cfg:
        # relative size between monsters; "scale" stays available to fine-tune within a tier
        if cfg["taille"] not in cfg["tailles"]:
            sys.exit(f"{name} : taille « {cfg['taille']} » inconnue ({', '.join(cfg['tailles'])})")
        cfg["scale"] = cfg["tailles"][cfg["taille"]] * cfg.get("scale", 1.0)
    return cfg


# ---------- Masks ----------

def drop_shadows(rgba, cfg):
    """Dofus exports draw the ground shadow as faint, dark (sometimes tinted) pixels under the monster.
    Only the lower part is considered, so dark translucent parts of the body (robes, grass) survive."""
    a = np.asarray(rgba).astype(int)
    rgb, al = a[..., :3], a[..., 3]
    lum = rgb.mean(2)
    sat = rgb.max(2) - rgb.min(2)
    shadow = (al < cfg["shadow_alpha"]) & (lum < cfg["shadow_lum"]) & (sat < cfg["shadow_sat"])
    ys = np.nonzero((al > 128).any(1))[0]
    if len(ys):
        shadow[: ys[0] + int((ys[-1] - ys[0]) * cfg["shadow_from"])] = False
    if cfg.get("ground_color"):
        # opaque ground ellipse painted into some AI backs: drop that colour in the lower third
        near = np.abs(rgb - cfg["ground_color"]).max(2) < 32
        near[: a.shape[0] * 2 // 3] = False
        shadow |= near
    a[..., 3] = np.where(shadow, 0, al)
    return Image.fromarray(a.astype(np.uint8), "RGBA")


def flood_segment(path, cfg):
    """Fallback for monsters rembg crops badly (e.g. white parts touching the white background):
    flood from the border with a small step tolerance, stopped by any saturated or dark pixel."""
    img = Image.open(path).convert("RGB")
    a = np.asarray(img.resize((512, 512), Image.BOX)).astype(int)
    h, w, _ = a.shape
    bgish = ((a.max(2) - a.min(2)) < 14) & (a.mean(2) > 120)
    seen = np.zeros((h, w), bool)
    q = deque((y, x) for y in range(h) for x in (0, w - 1)) + deque((y, x) for x in range(w) for y in (0, h - 1))
    for p in q:
        seen[p] = True
    while q:
        y, x = q.popleft()
        for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if 0 <= ny < h and 0 <= nx < w and not seen[ny, nx] and bgish[ny, nx] \
                    and np.abs(a[ny, nx] - a[y, x]).max() <= cfg["flood_step"]:
                seen[ny, nx] = True
                q.append((ny, nx))
    out = img.convert("RGBA")
    out.putalpha(Image.fromarray(np.where(seen, 0, 255).astype(np.uint8)).resize(img.size, Image.BILINEAR))
    return out


_rembg_session = None


def segment(path, cfg):
    """Background removal for the opaque back artworks, cached by source mtime."""
    global _rembg_session
    if cfg["segmentation"] == "flood":
        return flood_segment(path, cfg)
    CACHE_DIR.mkdir(exist_ok=True)
    cache = CACHE_DIR / f"{path.stem}.{cfg['rembg_model']}.{int(path.stat().st_mtime)}.png"
    if not cache.exists():
        from rembg import new_session, remove
        if _rembg_session is None or _rembg_session[0] != cfg["rembg_model"]:
            _rembg_session = (cfg["rembg_model"], new_session(cfg["rembg_model"]))
        mask = remove(Image.open(path).convert("RGB"), session=_rembg_session[1], only_mask=True)
        mask.save(cache)
    out = Image.open(path).convert("RGB").convert("RGBA")
    out.putalpha(Image.open(cache).convert("L"))
    return out


def load_art(path, cfg):
    img = Image.open(path).convert("RGBA")
    has_alpha = (np.asarray(img)[..., 3] < 10).mean() > 0.05
    if not has_alpha or cfg.get("force_segmentation"):
        img = segment(path, cfg)
    return drop_shadows(img, cfg)


# ---------- Downscale ----------

def components(mask):
    """4-connected components of a boolean 2D mask, as lists of (y, x)."""
    seen = np.zeros_like(mask)
    h, w = mask.shape
    for y0, x0 in zip(*np.nonzero(mask)):
        if seen[y0, x0]:
            continue
        seen[y0, x0] = True
        comp, q = [], deque([(y0, x0)])
        while q:
            y, x = q.popleft()
            comp.append((y, x))
            for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not seen[ny, nx]:
                    seen[ny, nx] = True
                    q.append((ny, nx))
        yield comp


def grow_thin(strong, weak):
    """Adds partially covered pixels that continue a thin structure (stem, leg, whisker, stick).
    A candidate must touch the shape and have at most 2 strong 8-neighbours: along the edge of a
    body it would have more, so silhouettes don't get fatter."""
    h, w = strong.shape

    def neigh(m):
        p = np.pad(m, 1).astype(int)
        return sum(p[1 + dy:1 + dy + h, 1 + dx:1 + dx + w]
                   for dy in (-1, 0, 1) for dx in (-1, 0, 1) if dy or dx)

    strong_n = neigh(strong)
    cand = weak & ~strong & (strong_n <= 2)
    shape = strong.copy()
    for _ in range(SIZE):
        add = cand & ~shape & (neigh(shape) > 0)
        if not add.any():
            break
        shape |= add
    return shape


def to_sprite(img, cfg):
    """Crops to content, fits it bottom-centred and downsamples by area while keeping line art.

    Returns (rgb float array 64x64x3, opaque bool mask 64x64, line bool mask 64x64)."""
    place = cfg["place"]
    alpha = np.asarray(img)[..., 3]
    ys, xs = np.nonzero(alpha > 128)
    img = img.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    w, h = img.size
    s = place["size"] * cfg.get("scale", 1.0) / max(w, h)
    tw, th = min(SIZE, max(1, round(w * s))), min(SIZE, max(1, round(h * s)))
    k = 8  # each target pixel averages k*k resampled source pixels
    big = np.asarray(img.resize((tw * k, th * k), Image.LANCZOS)).astype(float) / 255
    rgb, al = big[..., :3], big[..., 3:]
    if cfg.get("translucent_over"):
        # translucent parts (insect wings) read as pale tints instead of saturated opaque plates
        bg = np.array(cfg["translucent_over"]) / 255
        seen = al > cfg["visible_alpha"]
        rgb = np.where(seen, rgb * al + bg * (1 - al), rgb)
        al = np.where(seen, 1.0, al)
    cells = lambda m: m.reshape(th, k, tw, k, -1)

    lum = (rgb @ [0.299, 0.587, 0.114])[..., None] * 255
    dark = ((lum < cfg["line_lum"]) & (al > 0.5)).astype(float)
    a_sum = cells(al).sum((1, 3))
    col = cells(rgb * al).sum((1, 3)) / np.maximum(a_sum, 1e-6)
    d_sum = cells(dark).sum((1, 3))
    d_col = cells(rgb * dark).sum((1, 3)) / np.maximum(d_sum, 1e-6)
    line = (d_sum / (k * k))[..., 0] > cfg["line_fraction"]
    col[line] = d_col[line]
    # coverage of *visible* pixels, so translucent bodies (jelly, ghosts) stay solid
    visible = (al > cfg["visible_alpha"]).astype(float)
    cover = cells(visible).mean((1, 3))[..., 0]
    opaque = (cover > cfg["alpha_cut"]) | (line & (cover > cfg["thin_cut"]))
    opaque = grow_thin(opaque, cover > cfg["thin_cut"])

    for comp in components(opaque):
        if len(comp) < cfg["min_island"]:
            for p in comp:
                opaque[p] = False

    pad = np.pad(opaque, 1)
    edge = opaque & ~(pad[:-2, 1:-1] & pad[2:, 1:-1] & pad[1:-1, :-2] & pad[1:-1, 2:])
    col[edge & ~line] *= 1 - cfg["outline"]
    line |= edge & (cfg["outline"] > 0)

    out_rgb = np.zeros((SIZE, SIZE, 3))
    out_a = np.zeros((SIZE, SIZE), bool)
    out_l = np.zeros((SIZE, SIZE), bool)
    ox = (SIZE - tw) // 2
    oy = min(SIZE - th, max(0, place["bottom"] + 1 - th))
    out_rgb[oy:oy + th, ox:ox + tw] = col
    out_a[oy:oy + th, ox:ox + tw] = opaque
    out_l[oy:oy + th, ox:ox + tw] = line & opaque
    return out_rgb * 255, out_a, out_l


# ---------- Palette ----------

def to_oklab(rgb):
    c = rgb / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    lms = c @ np.array([[0.4122214708, 0.2119034982, 0.0883024619],
                        [0.5363325363, 0.6806995451, 0.2817188376],
                        [0.0514459929, 0.1073969566, 0.6299787005]])
    lms = np.cbrt(lms)
    return lms @ np.array([[0.2104542553, 1.9779984951, 0.0259040371],
                           [0.7936177850, -2.4285922050, 0.7827717662],
                           [-0.0040720468, 0.4505937099, -0.8086757660]])


def build_palette(sprites, cfg):
    """Weighted k-means in OKLab over the opaque pixels of every sprite, seeded by median cut.
    Line-art pixels weigh more so outlines and eyes keep a colour of their own."""
    px, wt = [], []
    for rgb, opaque, line in sprites:
        px.append(rgb[opaque])
        wt.append(np.where(line[opaque], cfg["line_weight"], 1.0))
    px = np.concatenate(px).round().clip(0, 255)
    wt = np.concatenate(wt)
    # one sample per colour bin weighted by sqrt(area): small but distinct details (a tongue,
    # an iris) are not swallowed by the large flat areas
    keys, inv = np.unique((px // 8).astype(int), axis=0, return_inverse=True)
    inv = inv.ravel()
    bin_w = np.bincount(inv, wt)
    px = np.stack([np.bincount(inv, px[:, c] * wt) / bin_w for c in range(3)], 1)
    wt = np.sqrt(bin_w)
    n = 15
    seed = Image.fromarray(px.astype(np.uint8)[None], "RGB").quantize(n, Image.Quantize.MEDIANCUT)
    centers = np.array(seed.getpalette()[:3 * n], float).reshape(-1, 3)
    lab = to_oklab(px)
    for _ in range(15):
        assign = ((lab[:, None] - to_oklab(centers)[None]) ** 2).sum(-1).argmin(1)
        for i in range(n):
            sel = assign == i
            if sel.any():
                centers[i] = (px[sel] * wt[sel, None]).sum(0) / wt[sel].sum()
            else:  # revive an empty cluster on the worst-represented pixel
                err = ((lab - to_oklab(centers)[assign]) ** 2).sum(1) * wt
                centers[i] = px[err.argmax()]
    centers = centers.round().clip(0, 255).astype(int)
    order = np.argsort(to_oklab(centers.astype(float))[:, 0])  # dark to light, easier to edit by hand
    return centers[order]


def index_sprite(rgb, opaque, pal):
    lab_pal = to_oklab(pal.astype(float))
    idx = ((to_oklab(rgb)[..., None, :] - lab_pal[None, None]) ** 2).sum(-1).argmin(-1) + 1
    idx[~opaque] = 0
    return idx.astype(np.uint8)


def read_pal(path):
    lines = path.read_text().split()
    return np.array(lines[3:3 + 48], int).reshape(16, 3)


def write_pal(path, colors):
    rows = ["JASC-PAL", "0100", "16"] + [f"{r} {g} {b}" for r, g, b in colors]
    path.write_bytes(("\r\n".join(rows) + "\r\n").encode())


def carry_shiny(new_pal, old_normal, old_shiny):
    """Keeps a hand-made shiny: each new colour gets the shift of its closest old normal colour."""
    out = []
    for c in new_pal:
        i = 1 + ((old_normal[1:] - c) ** 2).sum(1).argmin()
        out.append(np.clip(c + old_shiny[i] - old_normal[i], 0, 255))
    return np.array(out, int)


def save_indexed(path, idx, palette):
    im = Image.fromarray(idx, "P")
    flat = [int(v) for c in palette for v in c]
    im.putpalette(flat + [0] * (768 - len(flat)))
    im.save(path, optimize=True)


# ---------- Audit ----------

def audit(name, sprites, palette, scale):
    flags = []
    for view, (rgb, opaque, _line), idx in sprites:
        cover = opaque.mean()
        if cover < 0.08 * scale ** 2:  # small monsters are meant to cover less
            flags.append(f"{view} : très peu de pixels opaques ({cover:.0%})")
        islands = sum(1 for c in components(opaque)) - 1
        if islands > 3:
            flags.append(f"{view} : {islands} morceaux détachés")
        if len(set(idx[opaque].tolist())) < 6:
            flags.append(f"{view} : seulement {len(set(idx[opaque].tolist()))} couleurs")
    _, (_, fo, _), _ = sprites[0]
    _, (_, bo, _), _ = sprites[1]
    ratio = bo.sum() / max(fo.sum(), 1)
    if not 0.4 < ratio < 2.5:
        flags.append(f"dos/face : surfaces très différentes (x{ratio:.1f})")
    return flags


# ---------- Commands ----------

APPLIED = HERE / "applied.json"  # fingerprints of what --apply wrote, to detect later hand edits
SPRITE_FILES = ["front.png", "back.png", "anim_front.png", "normal.pal", "shiny.pal"]


def fingerprint(path):
    """Content hash that ignores how the file was saved (PNG encoder, line endings)."""
    if path.suffix == ".pal":
        data = read_pal(path).tobytes()
    else:
        data = np.asarray(Image.open(path).convert("RGB")).tobytes()
    return hashlib.sha1(data).hexdigest()[:16]


def load_applied():
    return json.loads(APPLIED.read_text()) if APPLIED.exists() else {}


def hand_edited(name, applied):
    """Files of graphics/pokemon/<name> changed since the pipeline last wrote them."""
    return [f for f, h in applied.get(name, {}).items()
            if (GFX_DIR / name / f).exists() and fingerprint(GFX_DIR / name / f) != h]


def protection(name, cfg, applied=None):
    """Why the current sprites must not be overwritten, or None."""
    if cfg.get("protected"):
        return cfg["protected"]
    edited = hand_edited(name, load_applied() if applied is None else applied)
    if edited:
        return "retouché à la main : " + ", ".join(edited)
    anim = GFX_DIR / name / "anim_front.png"
    if anim.exists():
        a = np.asarray(Image.open(anim))
        h = a.shape[0] // 2
        if a.shape[0] == 2 * SIZE and (a[:h] != a[h:]).any():
            return "anim_front.png contient une vraie animation"
    return None


def generate(name, src, art, cfg):
    # "front" / "back" sub-objects in overrides.json only apply to that view
    f_cfg = {**cfg, **cfg.get("front", {}), "place": cfg["front_place"]}
    b_cfg = {**cfg, **cfg.get("back", {}), "place": cfg["back_place"]}
    front = to_sprite(load_art(src / f"{art}.png", f_cfg), f_cfg)
    back = to_sprite(load_art(src / f"{art}_back.png", b_cfg), b_cfg)
    pal = build_palette([front, back], cfg)
    palette = [TRANSPARENT] + [tuple(c) for c in pal]

    out = PREVIEW_DIR / name
    out.mkdir(parents=True, exist_ok=True)
    f_idx, b_idx = index_sprite(front[0], front[1], pal), index_sprite(back[0], back[1], pal)
    save_indexed(out / "front.png", f_idx, palette)
    save_indexed(out / "back.png", b_idx, palette)
    save_indexed(out / "anim_front.png", np.vstack([f_idx, f_idx]), palette)
    write_pal(out / "normal.pal", palette)

    shiny = palette
    old = GFX_DIR / name
    if (old / "normal.pal").exists() and (old / "shiny.pal").exists():
        old_n, old_s = read_pal(old / "normal.pal"), read_pal(old / "shiny.pal")
        if (old_n != old_s).any():
            shiny = [TRANSPARENT] + [tuple(c) for c in carry_shiny(pal, old_n, old_s)]
    write_pal(out / "shiny.pal", shiny)
    return audit(name, [("face", front, f_idx), ("dos", back, b_idx)], palette, cfg["scale"])


def cmd_generate(args, defaults, monsters):
    src = args.src.expanduser()
    # names are graphics/pokemon folders; overrides map renamed ones to their artwork ("source")
    renamed = {m["source"]: name for name, m in monsters.items() if "source" in m}
    names = args.names or sorted({renamed.get(p.stem, p.stem) for p in src.glob("*.png") if not p.stem.endswith("_back")})
    index_path = PREVIEW_DIR / "index.json"
    index = json.loads(index_path.read_text()) if index_path.exists() else {}
    for i, name in enumerate(names, 1):
        cfg = config_for(name, defaults, monsters)
        art = cfg.get("source", name)
        if not (src / f"{art}.png").exists() or not (src / f"{art}_back.png").exists():
            print(f"[{i}/{len(names)}] {name} : source {art}.png ou {art}_back.png manquante, ignoré")
            continue
        flags = generate(name, src, art, cfg)
        index[name] = {
            "flags": flags,
            "protected": protection(name, cfg),
            "inGame": (GFX_DIR / name).is_dir(),
        }
        print(f"[{i}/{len(names)}] {name}" + "".join(f"\n    ⚠ {f}" for f in flags))
        PREVIEW_DIR.mkdir(exist_ok=True)
        index_path.write_text(json.dumps(index, ensure_ascii=False, indent=1, sort_keys=True))
    flagged = [n for n in names if index.get(n, {}).get("flags")]
    print(f"\n{len(names)} aperçus, {len(flagged)} à vérifier : {', '.join(flagged) or '—'}")


def cmd_apply(args, defaults, monsters):
    names = args.names or sorted(p.name for p in PREVIEW_DIR.iterdir() if (p / "front.png").exists())
    applied = load_applied()
    for name in names:
        src, dst = PREVIEW_DIR / name, GFX_DIR / name
        if not (src / "front.png").exists():
            print(f"{name} : pas d'aperçu, lance d'abord la génération")
            continue
        if not dst.is_dir():
            print(f"{name} : absent de graphics/pokemon, ignoré")
            continue
        why = protection(name, config_for(name, defaults, monsters), applied)
        if why and not args.force:
            print(f"{name} : protégé ({why}), ignoré — --force pour écraser")
            continue
        files = [f for f in SPRITE_FILES if f != "front.png" or (dst / f).exists()]
        for f in files:
            shutil.copy2(src / f, dst / f)
        applied[name] = {f: fingerprint(dst / f) for f in files}
        APPLIED.write_text(json.dumps(applied, indent=1, sort_keys=True) + "\n")
        print(f"{name} : appliqué")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("names", nargs="*", help="monstres à traiter (défaut : tous)")
    p.add_argument("--src", type=Path, help="dossier des artworks sources")
    p.add_argument("--apply", action="store_true", help="copie les aperçus dans graphics/pokemon")
    p.add_argument("--force", action="store_true", help="avec --apply, écrase aussi les sprites protégés")
    args = p.parse_args()
    defaults, monsters = load_overrides()
    if args.apply:
        cmd_apply(args, defaults, monsters)
    elif args.src:
        cmd_generate(args, defaults, monsters)
    else:
        p.error("--src (génération) ou --apply requis")


if __name__ == "__main__":
    sys.exit(main())
