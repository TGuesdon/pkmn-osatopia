#!/usr/bin/env python3
"""Small local editor for the "taille" of each monster (see overrides.json), with the sprites shown
at the size they would get. Stdlib only, no venv needed.

Usage: ./dev_scripts/sprite_import/sizes.py [port]   then pick sizes in the browser; every click is
saved to overrides.json right away. Regenerate the previews afterwards with ./run.sh --src ...
"""
import json
import re
import socket
import sys
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
OVERRIDES = HERE / "overrides.json"
GFX_DIR = REPO / "graphics" / "pokemon"


def read_overrides():
    return json.loads(OVERRIDES.read_text())


def write_overrides(data):
    OVERRIDES.write_text(json.dumps(data, ensure_ascii=False, indent=1))


def species():
    """Monsters with a sprite folder, in national dex order, grouped by evolution family."""
    info = (REPO / "src/data/pokemon/species_info.h").read_text()
    gfx = (REPO / "src/data/graphics/pokemon.h").read_text()
    dex = (REPO / "include/constants/pokedex.h").read_text()
    pic_dir = dict(re.findall(r'gMonFrontPic_(\w+)\[\]\s*=\s*INCBIN_U32\("graphics/pokemon/(.+?)/(?:anim_)?front', gfx))
    dex_order = {n: i for i, n in enumerate(re.findall(r"^\s*(NATIONAL_DEX_\w+)", dex, re.M))}

    mons = {}
    for const, body in re.findall(r"^\s*\[(SPECIES_\w+)\]\s*=(.*?)(?=^\s*\[SPECIES_|\Z)", info, re.M | re.S):
        pic = re.search(r"\.frontPic\s*=\s*gMonFrontPic_(\w+)", body)
        name = re.search(r'\.speciesName\s*=\s*_\("(.*?)"\)', body)
        num = re.search(r"\.natDexNum\s*=\s*(NATIONAL_DEX_\w+)", body)
        folder = pic and pic_dir.get(pic.group(1))
        if not folder or folder.startswith("question_mark") or not (GFX_DIR / folder / "back.png").exists():
            continue
        evo = re.search(r"\.evolutions\s*=\s*EVOLUTION\((.*?)\)\s*,\s*$", body, re.M | re.S)
        mons[const] = {
            "folder": folder,
            "name": name.group(1) if name else folder,
            "dex": dex_order.get(num.group(1), 9999) if num else 9999,
            "evolves": [s for s in re.findall(r"SPECIES_\w+", evo.group(1)) if s != "SPECIES_NONE"] if evo else [],
        }

    # union-find over evolutions so a whole family is shown on one line
    parent = {c: c for c in mons}

    def root(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c

    for c, m in mons.items():
        for t in m["evolves"]:
            if t in mons:
                parent[root(t)] = root(c)
    families = {}
    for c in sorted(mons, key=lambda c: (mons[c]["dex"], c)):
        families.setdefault(root(c), []).append({k: v for k, v in mons[c].items() if k != "evolves"})
    return sorted(families.values(), key=lambda f: f[0]["dex"])


def state():
    data = read_overrides()
    d = data["defaults"]
    return {
        "tailles": d["tailles"],
        "place": {"front": d["front_place"], "back": d["back_place"]},
        "sizes": {n: m["taille"] for n, m in data["monsters"].items() if "taille" in m},
        "families": species(),
    }


def set_taille(folder, taille):
    data = read_overrides()  # re-read so hand edits made meanwhile are kept
    if taille is not None and taille not in data["defaults"]["tailles"]:
        raise ValueError(f"taille inconnue : {taille}")
    monsters = data["monsters"]
    if taille is None:
        if folder in monsters:
            monsters[folder].pop("taille", None)
            if not monsters[folder]:
                del monsters[folder]
    else:
        monsters.setdefault(folder, {})["taille"] = taille
    write_overrides(data)


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(REPO), **kwargs)

    def log_message(self, *args):
        pass

    def send_json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.path = "/dev_scripts/sprite_import/sizes.html"
        if self.path == "/api/state":
            try:
                return self.send_json(state())
            except Exception as e:  # shown in the page instead of a silent 500
                return self.send_json({"error": repr(e)}, 500)
        if not self.path.startswith(("/graphics/pokemon/", "/dev_scripts/sprite_import/sizes.html")):
            return self.send_error(404)
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/taille":
            return self.send_error(404)
        try:
            req = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            set_taille(req["folder"], req.get("taille"))
            self.send_json({"ok": True})
        except Exception as e:
            self.send_json({"error": str(e)}, 400)


def free_port(port):
    while True:
        with socket.socket() as s:
            if s.connect_ex(("127.0.0.1", port)):
                return port
        port += 1


def main():
    port = free_port(int(sys.argv[1]) if len(sys.argv) > 1 else 8650)
    url = f"http://localhost:{port}/"
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Éditeur de tailles : {url}  (Ctrl+C pour arrêter)")
    threading.Timer(1, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
