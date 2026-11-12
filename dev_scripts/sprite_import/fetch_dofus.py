#!/usr/bin/env python3
"""Fetches a monster's front and back artworks straight from Dofus, then generates its previews.

Dofus draws every monster in 4 directions (1, 3 = facing the camera, 5, 7 = seen from behind), so
there is a real 3/4 back view: no need to have one imagined. DofusDB gives the monster's « look »
and Ankama's renderer draws that look in any direction, on a transparent background.

Defaults: front = direction 3 (looking down-left, the mirror of DofusDB's picture, as the existing
sources), back = direction 7 (head on the right, towards the opponent). A few monsters are drawn the
other way round (Bouftou): --face 1 or --dos 5. preview/<name>/directions.png shows the 4 directions.

  ./run.sh fetch <name> [dofus] [--taille petit] [--face 1|3] [--dos 5|7]
      <name>   graphics/pokemon folder (e.g. tofu)
      dofus    Dofus name or DofusDB id (default: <name> with spaces); an id settles homonyms
  then review in the dex viewer and ./run.sh --apply <name>, as for any other source.

The DofusDB id and directions are saved in overrides.json (« dofus »), so later runs need only the
name. Existing source files are never overwritten without --force (hand-made poses, Gemini backs).
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / ".claude" / "skills" / "concevoir-monstre" / "scripts"))
import dofusdb  # noqa: E402
import import_sprites  # noqa: E402

RENDERER = "https://static.ankama.com/dofus/renderer/look/{look}/full/{dir}/600_600-10.png"
DEFAULT_SRC = Path("~/Dev/perso/imgToGBASprite/source")
DEFAULT_DIRS = {"face": 3, "dos": 7}
OVERRIDES = HERE / "overrides.json"


def render(look, direction):
    url = RENDERER.format(look=look.encode().hex(), dir=direction)
    out = subprocess.run(["curl", "-sS", "-f", "-m", "30", "-A", "osatopia-sprite-import", url],
                         capture_output=True)
    if out.returncode:
        sys.exit(f"Le renderer Ankama a refusé la direction {direction} ({url}) : {out.stderr.decode().strip()}")
    from io import BytesIO
    return Image.open(BytesIO(out.stdout)).convert("RGBA")


def contact_sheet(views, front, back, path):
    """The 4 directions side by side, the chosen pair framed in red."""
    s = 200
    sheet = Image.new("RGBA", (s * 4, s + 20), (255, 255, 255, 255))
    d = ImageDraw.Draw(sheet)
    for i, direction in enumerate((1, 3, 5, 7)):
        im = views[direction].copy()
        im.thumbnail((s, s))
        sheet.alpha_composite(im, (s * i, 20))
        role = {front: " (face)", back: " (dos)"}.get(direction, "")
        d.text((s * i + 6, 4), f"direction {direction}{role}", fill="black")
        if role:
            d.rectangle((s * i, 0, s * i + s - 1, s + 19), outline="red", width=2)
    path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(path)


def save_overrides(name, entry):
    data = json.loads(OVERRIDES.read_text())
    data["monsters"].setdefault(name, {}).update(entry)
    OVERRIDES.write_text(json.dumps(data, indent=1, ensure_ascii=False))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("name", help="dossier graphics/pokemon (ex. tofu)")
    p.add_argument("dofus", nargs="?", help="nom Dofus ou id DofusDB (défaut : celui enregistré, sinon le nom)")
    p.add_argument("--src", type=Path, default=DEFAULT_SRC, help=f"dossier des artworks (défaut : {DEFAULT_SRC})")
    p.add_argument("--taille", help="minuscule, petit, moyen, grand ou enorme (enregistrée dans overrides.json)")
    p.add_argument("--face", type=int, choices=(1, 3), help="direction de face (défaut : enregistrée, sinon 3)")
    p.add_argument("--dos", type=int, choices=(5, 7), help="direction de dos (défaut : enregistrée, sinon 7)")
    p.add_argument("--force", action="store_true", help="écrase les artworks sources existants")
    p.add_argument("--no-generate", action="store_true", help="télécharge seulement, sans générer les aperçus")
    args = p.parse_args()

    defaults, monsters = import_sprites.load_overrides()
    known = monsters.get(args.name, {}).get("dofus", {})
    if args.taille and args.taille not in defaults["tailles"]:
        p.error(f"taille inconnue ({', '.join(defaults['tailles'])})")

    query = args.dofus or known.get("id") or args.name.replace("_", " ")
    monster, homonyms = dofusdb.resolve(str(query))
    mname = dofusdb.fr(monster.get("name"))
    print(f"{mname} (DofusDB #{monster['id']}), look {monster['look']}")
    if homonyms:
        print("  homonymes : " + ", ".join(f"#{m['id']}" for m in homonyms) + " (passe l'id pour en choisir un)")

    front = args.face or known.get("face", DEFAULT_DIRS["face"])
    back = args.dos or known.get("dos", DEFAULT_DIRS["dos"])
    views = {d: render(monster["look"], d) for d in (1, 3, 5, 7)}
    sheet = import_sprites.PREVIEW_DIR / args.name / "directions.png"
    contact_sheet(views, front, back, sheet)
    if not ImageChops.difference(views[front], views[back]).getbbox():
        print("  ⚠ le renderer renvoie la même image de face et de dos : pas de vraie vue de dos pour ce monstre")

    src = args.src.expanduser()
    art = monsters.get(args.name, {}).get("source", args.name)
    targets = {front: src / f"{art}.png", back: src / f"{art}_back.png"}
    existing = [t.name for t in targets.values() if t.exists()]
    if existing and not args.force:
        print(f"  {', '.join(existing)} existe déjà dans {src} : rien n'est écrasé (--force pour remplacer).")
        print(f"  Les 4 directions sont dans {sheet}")
        return 1
    src.mkdir(parents=True, exist_ok=True)
    for direction, path in targets.items():
        views[direction].save(path)
    print(f"  face (direction {front}) → {targets[front]}\n  dos (direction {back}) → {targets[back]}")

    entry = {"dofus": {"id": monster["id"], "face": front, "dos": back}}
    if args.taille:
        entry["taille"] = args.taille
    save_overrides(args.name, entry)
    if "taille" not in {**monsters.get(args.name, {}), **entry}:
        print("  ⚠ pas de taille : le sprite remplira tout le cadre (--taille, ou ./sizes.py)")

    if args.no_generate:
        return 0
    print()
    import_sprites.cmd_generate(argparse.Namespace(src=src, names=[args.name]), *import_sprites.load_overrides())
    if (import_sprites.GFX_DIR / args.name).is_dir():
        sys.stdout.flush()
        subprocess.run([sys.executable, str(HERE / "icon_palettes.py"), "--src", str(src), args.name], check=True)
    else:
        print(f"  graphics/pokemon/{args.name} n'existe pas encore : icône et --apply après l'ajout de l'espèce")
    print(f"\nDirections : {sheet}  (mauvais sens ? relance avec --face 1 / --dos 5 et --force)")
    print(f"Vérifie dans ./dev_scripts/dex_viewer/serve.sh, puis : ./dev_scripts/sprite_import/run.sh --apply {args.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
