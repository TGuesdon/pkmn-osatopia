#!/usr/bin/env python3
"""Party icons (32x32, 2 frames) for the Dofus monsters, read through one of the 6 shared icon palettes
(graphics/pokemon/icon_palettes/pal0-5) chosen by .iconPalIndex in src/data/pokemon/species_info.h.

Palette choice: for each candidate palette, the icon's colours are compared to the front sprite's in
OKLab, both ways (are the icon's colours found in the sprite? are the sprite's colours found in the
icon?), and the closest palette wins. An icon whose PNG palette is one of pal0-5 (as the regenerated
ones are) keeps that palette.

Regeneration (--src): the front artwork is downscaled with the battle sprite pipeline, then indexed on
the palette that reproduces it best. The palettes have few dark or brown tones, so colours are matched
with a lifted lightness and more weight on hue, and a dark outline keeps the silhouette readable.

  python3 dev_scripts/sprite_import/icon_palettes.py                  list palette changes
  python3 dev_scripts/sprite_import/icon_palettes.py --src <dir> [names...]
                                                regenerate icons into preview/<name>/icon.png
  python3 dev_scripts/sprite_import/icon_palettes.py --apply [names...]
                                                copy regenerated icons into graphics/pokemon/<name>/
                                                (all previews by default), then write the palettes
  --preview saves preview/icon_palettes.png: current | proposed (or regenerated) | front sprite
"""
import argparse
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image

from import_sprites import GFX_DIR, PREVIEW_DIR, REPO, config_for, load_art, load_overrides, to_oklab, to_sprite

SPECIES_INFO = REPO / "src" / "data" / "pokemon" / "species_info.h"
GRAPHICS = REPO / "src" / "data" / "graphics" / "pokemon.h"
ICON_PALETTES = REPO / "graphics" / "pokemon" / "icon_palettes"

ICON_FIELD = re.compile(r"(\.iconSprite = gMonIcon_(\w+),\s*\.iconPalIndex = )(\d)")
ICON = 32
OUTLINE = 15  # darkest grey, the same index in every icon palette
HUE_WEIGHT = 1.6  # OKLab a/b weight against lightness when indexing a regenerated icon
CHROMA_BOOST = 1.3
MIN_LIGHTNESS = 0.55  # median OKLab lightness a regenerated icon is lifted to
GREY_PENALTY = 0.05  # keeps coloured pixels (dark browns, dark greens) off the grey ramp


def load_icon_palettes():
    pals = []
    for i in range(6):
        lines = (ICON_PALETTES / f"pal{i}.pal").read_text().split("\n")[3:19]
        pals.append([tuple(map(int, line.split())) for line in lines])
    return np.array(pals, float)


def graphic_path(symbol, graphics):
    m = re.search(rf"\b{symbol}\[\] = INCBIN_\w+\(\"(.*?)\.4bpp(?:\.lz)?\"", graphics)
    return REPO / f"{m.group(1)}.png" if m else None


def sprite_colours(path):
    """OKLab colour of every opaque pixel of the first frame."""
    im = Image.open(path)
    pal = np.array(im.getpalette()[:48], float).reshape(16, 3)
    idx = np.array(im)[:64]
    return to_oklab(pal[idx[idx > 0]])


def own_palette(path, pals):
    """Index of the icon palette stored in the PNG itself, if it is one of them."""
    pal = Image.open(path).getpalette()
    if pal and len(pal) >= 48:
        pal = np.array(pal[:48], float).reshape(16, 3)
        for i, p in enumerate(pals):
            if (p == pal).all():
                return i
    return None


def best_palette(icon_idx, sprite_lab, lab_pals):
    counts = Counter(icon_idx[icon_idx > 0].tolist())
    used, weights = np.array(list(counts)), np.array(list(counts.values()), float)
    costs = []
    for lab in lab_pals:
        dist = np.sqrt(((lab[used][:, None] - sprite_lab[None]) ** 2).sum(-1))
        icon_in_sprite = (dist.min(1) * weights).sum() / weights.sum()
        sprite_in_icon = dist.min(0).mean()
        costs.append(icon_in_sprite + sprite_in_icon)
    return int(np.argmin(costs))


def generate_icon(art_path, cfg, lab_pals):
    """Returns (icon indices 64x32 with both frames, palette index)."""
    cfg = {**cfg, **cfg.get("front", {}), "scale": 1.0, "place": {"size": ICON - 4, "bottom": ICON - 4}}
    rgb, opaque, _ = to_sprite(load_art(art_path, cfg), cfg)
    # to_sprite centres a 64x64 canvas; the icon is its top-middle 32x32
    rgb, opaque = rgb[:ICON, 16:16 + ICON], opaque[:ICON, 16:16 + ICON]

    pix = to_oklab(rgb[opaque])
    pix[:, 0] += max(0.05, MIN_LIGHTNESS - np.median(pix[:, 0]))
    pix[:, 1:] *= CHROMA_BOOST
    weight = np.array([1, HUE_WEIGHT, HUE_WEIGHT])
    coloured = np.hypot(*pix[:, 1:].T) > 0.03
    best = None
    for k, lab in enumerate(lab_pals):
        cand = lab[1:]
        grey = np.hypot(*cand[:, 1:].T) < 0.02
        dist = (((pix[:, None] - cand[None]) * weight) ** 2).sum(-1) + GREY_PENALTY * (coloured[:, None] & grey[None])
        err = np.sqrt(dist.min(1)).mean()
        if best is None or err < best[0]:
            best = (err, k, dist.argmin(1) + 1)

    idx = np.zeros((ICON, ICON), np.uint8)
    idx[opaque] = best[2]
    pad = np.pad(opaque, 1)
    idx[~opaque & (pad[:-2, 1:-1] | pad[2:, 1:-1] | pad[1:-1, :-2] | pad[1:-1, 2:])] = OUTLINE
    # second frame bobs one pixel down, like the original icons
    return np.vstack([idx, np.roll(idx, 1, axis=0)]), best[1]


def save_icon(path, idx, pal):
    im = Image.fromarray(idx, "P")
    im.putpalette([int(v) for c in pal for v in c])
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path)


def colourise(icon_idx, pal, bg=(40, 40, 40)):
    rgb = pal[icon_idx].astype(np.uint8)
    rgb[icon_idx == 0] = bg
    return Image.fromarray(rgb)


def save_preview(rows, pals):
    cell, cols = 64, 4
    width = cell * 3 + 16
    sheet = Image.new("RGB", (cols * width, -(-len(rows) // cols) * cell), (40, 40, 40))
    for i, row in enumerate(rows):
        x, y = (i % cols) * width, (i // cols) * cell
        for j, (idx, pal) in enumerate(((row["icon"], row["current"]), (row["new_icon"], row["best"]))):
            sheet.paste(colourise(idx, pals[pal]).resize((cell, cell), Image.NEAREST), (x + j * cell, y))
        front = Image.open(row["front"]).convert("RGBA").crop((0, 0, 64, 64))
        sheet.paste(front, (x + 2 * cell, y), front)
    PREVIEW_DIR.mkdir(exist_ok=True)
    out = PREVIEW_DIR / "icon_palettes.png"
    sheet.save(out)
    print(f"aperçu : {out}")


def monsters_in_game(graphics, source):
    """(icon name, graphics folder, current palette, icon png, front png) for every species with sprites."""
    for block in re.split(r"\n(?=    \[SPECIES_)", source):
        front = re.search(r"\.frontPic = (gMonFrontPic_\w+),", block)
        icon = ICON_FIELD.search(block)
        if not front or not icon:
            continue
        front_png, icon_png = graphic_path(front.group(1), graphics), graphic_path(f"gMonIcon_{icon.group(2)}", graphics)
        if front_png and front_png.exists() and icon_png and icon_png.exists():
            yield icon.group(2), icon_png.parent.name, int(icon.group(3)), icon_png, front_png


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("names", nargs="*", help="dossiers graphics/pokemon à régénérer ou appliquer (défaut : tous)")
    p.add_argument("--src", type=Path, help="régénère les icônes depuis ce dossier d'artworks")
    p.add_argument("--apply", action="store_true", help="copie les icônes régénérées et écrit les palettes")
    p.add_argument("--preview", action="store_true", help="planche actuelle | proposée | sprite de face")
    args = p.parse_args()

    graphics = GRAPHICS.read_text()
    source = SPECIES_INFO.read_text()
    pals = load_icon_palettes()
    lab_pals = to_oklab(pals)
    defaults, overrides = load_overrides()
    wanted = set(args.names)

    rows = []
    for name, folder, current, icon_png, front_png in monsters_in_game(graphics, source):
        icon_idx = np.array(Image.open(icon_png))
        row = {"name": name, "folder": folder, "icon": icon_idx[:ICON], "front": front_png, "current": current}
        preview = PREVIEW_DIR / folder / "icon.png"
        if args.src and (not wanted or folder in wanted):
            cfg = config_for(folder, defaults, overrides)
            art = args.src.expanduser() / f"{cfg.get('source', folder)}.png"
            if not art.exists():
                print(f"{folder} : artwork {art.name} manquant, ignoré")
            else:
                new_idx, pal = generate_icon(art, cfg, lab_pals)
                save_icon(preview, new_idx, pals[pal])
        if args.apply and preview.exists() and (not wanted or folder in wanted):
            shutil.copy2(preview, icon_png)
            print(f"{folder} : icône régénérée appliquée")
        if (args.src or args.apply) and preview.exists() and (not wanted or folder in wanted):
            row["new_icon"] = np.array(Image.open(preview))[:ICON]
            row["best"] = own_palette(preview, pals)
        else:
            row["new_icon"] = row["icon"]
            own = own_palette(icon_png, pals)
            row["best"] = own if own is not None else best_palette(row["icon"], sprite_colours(front_png), lab_pals)
        rows.append(row)

    changed = {r["name"]: r["best"] for r in rows if r["best"] != r["current"]}
    for r in rows:
        if r["name"] in changed:
            print(f"{r['name']:<24} palette {r['current']} → {r['best']}")
    print(f"\n{len(changed)} / {len(rows)} icônes changent de palette")

    if args.preview:
        save_preview([r for r in rows if not wanted or r["folder"] in wanted], pals)
    if args.apply and changed:
        def replace(m):
            return m.group(1) + str(changed.get(m.group(2), m.group(3)))
        SPECIES_INFO.write_text(ICON_FIELD.sub(replace, source))
        print(f"{SPECIES_INFO.relative_to(REPO)} mis à jour")


if __name__ == "__main__":
    sys.exit(main())
