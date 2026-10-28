"""Lecture des données du jeu (pokeemerald-expansion) + traductions FR.

Les données de jeu (stats, attaques, learnsets) sont lues en direct dans le
repo, pour refléter l'état actuel. Les traductions viennent des glossaires
CSV générés par generer_glossaires.py.
"""
import csv
import os
import re

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(SKILL_DIR, "data")


def find_repo_root():
    d = os.getcwd()
    while d != "/":
        if os.path.exists(os.path.join(d, "src/data/moves_info.h")):
            return d
        d = os.path.dirname(d)
    d = SKILL_DIR
    while d != "/":
        if os.path.exists(os.path.join(d, "src/data/moves_info.h")):
            return d
        d = os.path.dirname(d)
    raise SystemExit("Racine du repo introuvable (src/data/moves_info.h)")


TYPES_FR = {
    "NORMAL": "Normal", "FIGHTING": "Combat", "FLYING": "Vol", "POISON": "Poison",
    "GROUND": "Sol", "ROCK": "Roche", "BUG": "Insecte", "GHOST": "Spectre",
    "STEEL": "Acier", "FIRE": "Feu", "WATER": "Eau", "GRASS": "Plante",
    "ELECTRIC": "Électrik", "PSYCHIC": "Psy", "ICE": "Glace", "DRAGON": "Dragon",
    "DARK": "Ténèbres", "FAIRY": "Fée", "STELLAR": "Stellaire", "MYSTERY": "???",
    "NONE": "-",
}
TYPES_FR_INV = {}
for _k, _v in TYPES_FR.items():
    TYPES_FR_INV[_v.lower()] = _k
    TYPES_FR_INV[_k.lower()] = _k
TYPES_FR_INV["electrik"] = "ELECTRIC"
TYPES_FR_INV["tenebres"] = "DARK"
TYPES_FR_INV["fee"] = "FAIRY"

CATEGORIES_FR = {"PHYSICAL": "Physique", "SPECIAL": "Spéciale", "STATUS": "Statut"}


def type_fr(t):
    return TYPES_FR.get(t.replace("TYPE_", ""), t)


def type_const(s):
    """'feu' / 'Fire' / 'TYPE_FIRE' -> 'FIRE'."""
    s = s.strip().replace("TYPE_", "")
    return TYPES_FR_INV.get(s.lower(), s.upper())


# ---------------------------------------------------------------- parsing C

def _first_branch(lines):
    """Garde la première branche des #if/#else (en général la config récente)."""
    out, stack = [], []  # stack de booléens "on garde"
    for line in lines:
        s = line.strip()
        if s.startswith("#if"):
            stack.append(True)
        elif s.startswith("#elif") or s.startswith("#else"):
            if stack:
                stack[-1] = False
        elif s.startswith("#endif"):
            if stack:
                stack.pop()
        elif all(stack):
            out.append(line)
    return out


def _resolve(val):
    """'(X >= GEN_5) ? 175 : 200' -> '175' ; garde la branche récente."""
    val = val.strip().rstrip(",").strip()
    if "?" in val and ":" in val:
        val = val.split("?", 1)[1].split(":", 1)[0].strip()
    return val.strip("() ")


def parse_entries(path, prefix):
    """Parse les tableaux `[PREFIX_X] = { .champ = valeur, ... }`."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    entries = {}
    for m in re.finditer(r"\[(%s\w+)\]\s*=\s*\{" % prefix, text):
        start = m.end()
        depth, i = 1, start
        while depth and i < len(text):
            c = text[i]
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            i += 1
        body = _first_branch(text[start:i - 1].split("\n"))
        fields = {}
        for line in body:
            fm = re.match(r"\s*\.(\w+)\s*=\s*(.+?)\s*$", line)
            if fm and fm.group(1) not in fields:
                fields[fm.group(1)] = fm.group(2)
        entries[m.group(1)] = fields
    return entries


def _in_paren(val):
    m = re.search(r"\((.*)\)", val)
    return m.group(1) if m else val


def _str(val):
    m = re.search(r'"([^"]*)"', val or "")
    return m.group(1) if m else ""


def load_moves(root):
    raw = parse_entries(os.path.join(root, "src/data/moves_info.h"), "MOVE_")
    moves = {}
    for const, f in raw.items():
        def num(k, default=0):
            v = _resolve(f.get(k, str(default)))
            try:
                return int(v)
            except ValueError:
                return default
        moves[const] = {
            "const": const,
            "name_en": _str(f.get("name")),
            "type": _resolve(f.get("type", "TYPE_NONE")).replace("TYPE_", ""),
            "category": _resolve(f.get("category", "")).replace("DAMAGE_CATEGORY_", ""),
            "power": num("power"),
            "accuracy": num("accuracy"),
            "pp": num("pp"),
            "priority": num("priority"),
            "effect": _resolve(f.get("effect", "")).replace("EFFECT_", ""),
        }
    return moves


def learnable_move_consts(root):
    """Attaques normales : exclut les capacités Z et Dynamax (après MOVES_COUNT)."""
    with open(os.path.join(root, "include/constants/moves.h"), encoding="utf-8") as f:
        text = f.read()
    count = int(re.search(r"#define MOVES_COUNT_GEN9\s+(\d+)", text).group(1))
    return {c for c, n in re.findall(r"#define (MOVE_\w+)\s+(\d+)\s*$", text, re.M) if int(n) < count}


def load_abilities(root):
    raw = parse_entries(os.path.join(root, "src/data/abilities.h"), "ABILITY_")
    return {k: {"const": k, "name_en": _str(v.get("name"))} for k, v in raw.items()}


STAT_KEYS = [("baseHP", "PV"), ("baseAttack", "Att"), ("baseDefense", "Déf"),
             ("baseSpAttack", "AtqSpé"), ("baseSpDefense", "DéfSpé"), ("baseSpeed", "Vit")]


def load_species(root):
    base = os.path.join(root, "src/data/pokemon")
    files = [("species_info.h", True)] + [
        (os.path.join("species_info", n), False)
        for n in sorted(os.listdir(os.path.join(base, "species_info")))
        if n.endswith("_families.h")]
    species = {}
    for fname, is_custom_file in files:
        for const, f in parse_entries(os.path.join(base, fname), "SPECIES_").items():
            if "baseHP" not in f:
                continue
            stats = []
            for k, _ in STAT_KEYS:
                try:
                    stats.append(int(_resolve(f.get(k, "0"))))
                except ValueError:
                    stats.append(0)
            abilities = [a.strip() for a in _in_paren("(" + f.get("abilities", "").strip("{} ,") + ")").split(",")]
            species[const] = {
                "const": const,
                "name_game": _str(f.get("speciesName")),
                "types": [t.strip().replace("TYPE_", "") for t in _in_paren(f.get("types", "")).split(",") if t.strip()],
                "stats": stats,
                "abilities": [a for a in abilities if a and a != "ABILITY_NONE"],
                "levelUp": f.get("levelUpLearnset", "").rstrip(","),
                "teachable": f.get("teachableLearnset", "").rstrip(","),
                "eggMoves": f.get("eggMoveLearnset", "").rstrip(","),
                "evolutions": f.get("evolutions", "").rstrip(","),
                "custom": is_custom_file,
            }
    return species


def load_level_up_learnsets(root):
    path = os.path.join(root, "src/data/pokemon/level_up_learnsets/gen_9.h")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    out = {}
    for m in re.finditer(r"struct LevelUpMove (\w+)\[\]\s*=\s*\{(.*?)\};", text, re.S):
        out[m.group(1)] = [(int(l), mv) for l, mv in
                           re.findall(r"LEVEL_UP_MOVE\(\s*(\d+)\s*,\s*(MOVE_\w+)\s*\)", m.group(2))]
    return out


def load_move_lists(root, filename):
    with open(os.path.join(root, "src/data/pokemon", filename), encoding="utf-8") as f:
        text = f.read()
    return {m.group(1): re.findall(r"MOVE_\w+", m.group(2).replace("MOVE_UNAVAILABLE", ""))
            for m in re.finditer(r"u16 (\w+)\[\]\s*=\s*\{(.*?)\};", text, re.S)}


# ---------------------------------------------------------------- glossaires

def load_glossary(name):
    path = os.path.join(DATA_DIR, name)
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return {row["constante"]: row for row in csv.DictReader(f)}


def norm(s):
    s = s.lower().strip()
    for a, b in [("é", "e"), ("è", "e"), ("ê", "e"), ("ë", "e"), ("à", "a"), ("â", "a"),
                 ("î", "i"), ("ï", "i"), ("ô", "o"), ("û", "u"), ("ù", "u"), ("ç", "c"),
                 ("♀", "f"), ("♂", "m")]:
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]", "", s)
