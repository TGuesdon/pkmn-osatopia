"""Consultation de DofusDB (api.dofusdb.fr) pour nourrir la conception des monstres.

    python3 dofusdb.py cherche <texte>             # monstres dont le nom contient le texte
    python3 dofusdb.py fiche <nom|id> [--grade N]  # stats, résistances, sorts détaillés, zones
    python3 dofusdb.py famille <nom|id>            # monstres de la même race Dofus

Lecture seule. Les réponses de l'API sont mises en cache dans
data/dofusdb_cache/ (non versionné) pendant 30 jours ; --rafraichir l'ignore.
L'API n'est pas officielle : les données reflètent la version actuelle de Dofus.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.parse

API = "https://api.dofusdb.fr"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(HERE, "..", "data", "dofusdb_cache")
CACHE_TTL = 30 * 24 * 3600
REFRESH = False

ELEMENTS = {0: "Neutre", 1: "Terre", 2: "Feu", 3: "Eau", 4: "Air"}
# Caractéristique Dofus -> élément de ses sorts
CARACS = [("strength", "Force", "Terre"), ("intelligence", "Intelligence", "Feu"),
          ("chance", "Chance", "Eau"), ("agility", "Agilité", "Air")]
RESISTS = [("reductionNeutral", "Neutre"), ("reductionEarth", "Terre"), ("reductionFire", "Feu"),
           ("reductionWater", "Eau"), ("reductionAir", "Air")]
ZONES = {"P": None, "C": "cercle", "X": "croix", "L": "ligne", "T": "ligne perpendiculaire",
         "D": "damier", "O": "anneau", "Q": "croix vide", "G": "carré", "+": "étoile",
         "#": "croix diagonale", "/": "ligne diagonale", "-": "ligne perpendiculaire",
         "a": "tout le terrain", "A": "tout le terrain", "V": "cône", "W": "carré"}


# --------------------------------------------------------------------------- API

def get(path, params=None):
    """GET JSON via curl (le Python de python.org n'a pas toujours les certificats)."""
    url = API + "/" + path
    if params:
        url += "?" + urllib.parse.urlencode(params, safe="[]$")
    os.makedirs(CACHE_DIR, exist_ok=True)
    key = os.path.join(CACHE_DIR, hashlib.sha1(url.encode()).hexdigest() + ".json")
    if not REFRESH and os.path.exists(key) and time.time() - os.path.getmtime(key) < CACHE_TTL:
        with open(key, encoding="utf-8") as f:
            return json.load(f)
    try:
        out = subprocess.run(["curl", "-sS", "-g", "-m", "20", "-A", "osatopia-concevoir-monstre", url],
                             capture_output=True, check=True, text=True).stdout
        data = json.loads(out)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        sys.exit("Erreur DofusDB sur %s : %s" % (url, e))
    if isinstance(data, dict) and data.get("className") in ("not-found", "bad-request"):
        return None
    with open(key, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    return data


def fr(obj):
    return (obj or {}).get("fr") or ""


def slugify(text):
    s = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s).strip()  # format des slugs DofusDB : « bouftou royal »


_names = {}


def name_of(kind, ident):
    """Nom FR d'un monstre, sort, état… (mis en cache mémoire)."""
    if (kind, ident) not in _names:
        d = get("%s/%s" % (kind, ident))
        _names[(kind, ident)] = fr(d.get("name")) if d else "#%s" % ident
    return _names[(kind, ident)]


# ----------------------------------------------------------------- monstres

def search_monsters(text, limit=50):
    slug = slugify(text)
    sel = ["id", "name", "race", "slug", "isBoss", "isMiniBoss", "hideInBestiary", "subareas",
           "isQuestMonster"]
    q = [("slug.fr[$regex]", re.escape(slug)), ("$limit", limit)] + [("$select[]", s) for s in sel]
    url = "monsters?" + urllib.parse.urlencode(q, safe="[]$")
    r = get(url)
    return (r or {}).get("data", []), slug


def score(m, slug):
    """Plus petit = meilleur candidat (nom exact, visible au bestiaire, présent en jeu)."""
    return (m["slug"]["fr"] != slug, bool(m.get("hideInBestiary")), not m.get("subareas"),
            bool(m.get("isQuestMonster")), m["id"])


def resolve(query):
    if str(query).isdigit():
        m = get("monsters/%s" % query)
        if not m:
            sys.exit("Aucun monstre d'id %s." % query)
        return m, []
    found, slug = search_monsters(query)
    if not found:
        sys.exit("Aucun monstre trouvé pour « %s ». Essaie `cherche`." % query)
    found.sort(key=lambda m: score(m, slug))
    others = [m for m in found[1:] if m["slug"]["fr"] == slug]
    return get("monsters/%s" % found[0]["id"]), others


def flags(m):
    out = []
    if m.get("isBoss"):
        out.append("boss")
    if m.get("isMiniBoss"):
        out.append("archi/mini-boss")
    if m.get("isQuestMonster"):
        out.append("quête")
    if m.get("hideInBestiary"):
        out.append("caché du bestiaire")
    return out


# --------------------------------------------------------------------- sorts

def render_effect(e):
    d = get("effects/%s" % e["effectId"]) or {}
    tpl = fr(d.get("description"))
    if not tpl:
        return None
    n1, n2, n3 = e.get("diceNum", 0), e.get("diceSide", 0), e.get("value", 0)
    eid = e["effectId"]
    # Paramètres qui sont des identifiants : on les remplace par un nom
    if "Invoque" in tpl or eid in (181, 405, 1008, 1011):
        n1 = name_of("monsters", n1) if n1 else n1
    elif "#1 :" in tpl or eid in (293, 294):
        n1 = name_of("spells", n1) if n1 else n1
    if "État" in tpl and n3:
        n3 = name_of("spell-states", n3)
    plural = (isinstance(n1, int) and n1 > 1) or (isinstance(n2, int) and n2 > 1)
    txt = re.sub(r"\{\{~1~2([^}]*)\}\}", lambda mo: mo.group(1) if n2 else "", tpl)
    txt = re.sub(r"\{\{~[pz]s\}\}", "s" if plural else "", txt)
    txt = re.sub(r"\{\{[^}]*\}\}", "", txt)
    txt = txt.replace("#1", str(n1)).replace("#2", str(n2) if n2 else "").replace("#3", str(n3))
    txt = re.sub(r"\s+", " ", txt).strip()
    extra = []
    if e.get("duration"):
        extra.append("%s tour%s" % (e["duration"], "s" if e["duration"] > 1 else ""))
    zone = (e.get("zoneDescr") or {})
    shape = ZONES.get(chr(zone["shape"])) if zone.get("shape") else None
    if shape:
        size = zone.get("param1")
        extra.append("zone %s%s" % (shape, " %s" % size if size and "terrain" not in shape else ""))
    if e.get("triggers") and e["triggers"] != "I":
        t = e["triggers"]
        extra.append("quand il subit des dommages" if t.startswith("D") else "déclenché : %s" % t)
    if e.get("random"):
        extra.append("%s %% de chance" % e["random"])
    if e.get("targetMask") in ("C", "c"):
        extra.append("sur soi")
    return txt + (" (%s)" % ", ".join(extra) if extra else "")


def damage_elements(effects):
    """Éléments des effets de dégâts / vol de vie / soins élémentaires."""
    els = set()
    for e in effects:
        d = get("effects/%s" % e["effectId"]) or {}
        el = d.get("elementId", -1)
        if el in ELEMENTS and d.get("category") == 2:
            els.add(ELEMENTS[el])
    return els


def spell_grade_for(m, idx, grade):
    """Grade du sort utilisé par le monstre à son grade donné (champ spellGrades)."""
    try:
        parts = m["spellGrades"][idx].split(";")
        return int(parts[min(grade, len(parts)) - 1].split(",")[0])
    except (IndexError, ValueError, KeyError):
        return 1


def print_spell(spell_id, sgrade):
    sp = get("spells/%s" % spell_id)
    if not sp:
        print("  - sort #%s introuvable" % spell_id)
        return set()
    levels = (get("spell-levels", {"spellId": spell_id, "$limit": 20}) or {}).get("data", [])
    lvl = next((l for l in levels if l.get("grade") == sgrade), levels[0] if levels else None)
    print("\n  ● %s  (sort %s)" % (fr(sp.get("name")) or "?", spell_id))
    if fr(sp.get("description")):
        print("    « %s »" % re.sub(r"\s+", " ", fr(sp["description"])).strip())
    if not lvl:
        return set()
    rng = "%s-%s" % (lvl.get("minRange", 0), lvl.get("range", 0))
    bits = ["%s PA" % lvl.get("apCost"), "portée %s%s" % (rng, " (modifiable)" if lvl.get("rangeCanBeBoosted") else "")]
    if lvl.get("castInLine"):
        bits.append("en ligne")
    if lvl.get("castTestLos") is False:
        bits.append("sans ligne de vue")
    if lvl.get("maxCastPerTurn"):
        bits.append("%s/tour" % lvl["maxCastPerTurn"])
    if lvl.get("maxCastPerTarget"):
        bits.append("%s/cible" % lvl["maxCastPerTarget"])
    if lvl.get("minCastInterval"):
        bits.append("relance %s tours" % lvl["minCastInterval"])
    if lvl.get("initialCooldown"):
        bits.append("1er lancer au tour %s" % (lvl["initialCooldown"] + 1))
    if lvl.get("criticalHitProbability"):
        bits.append("CC %s %%" % lvl["criticalHitProbability"])
    print("    " + " · ".join(bits))
    shown = [e for e in lvl.get("effects", []) if e.get("visibleInTooltip", True)]
    for e in shown:
        t = render_effect(e)
        if t:
            print("    - " + t)
    crit = [e for e in lvl.get("criticalEffect", []) if e.get("visibleInTooltip", True)]
    if crit:
        print("    Critique : " + " ; ".join(t for t in map(render_effect, crit) if t))
    return damage_elements(lvl.get("effects", []))


# ------------------------------------------------------------------ commandes

def cmd_cherche(args):
    found, slug = search_monsters(args.texte, limit=100)
    found.sort(key=lambda m: score(m, slug))
    if not found:
        print("Aucun résultat.")
    races = {}
    for m in found:
        if m["race"] not in races:
            races[m["race"]] = name_of("monster-races", m["race"])
        f = flags(m)
        print("%6s  %-32s race %-22s %s" % (m["id"], fr(m["name"]), races[m["race"]],
                                             ("[" + ", ".join(f) + "]") if f else ""))


def cmd_fiche(args):
    m, others = resolve(args.monstre)
    grades = m.get("grades", [])
    g_idx = min(args.grade or len(grades), len(grades)) if grades else 0
    print("=== %s (id %s) — race %s %s" % (fr(m["name"]), m["id"], name_of("monster-races", m["race"]),
                                          "[" + ", ".join(flags(m)) + "]" if flags(m) else ""))
    print("Image : %s" % m.get("img", "-"))
    print("Page : https://dofusdb.fr/fr/database/monster/%s" % m["id"])
    if others:
        print("Homonymes : " + ", ".join("%s (id %s)" % (fr(o["name"]), o["id"]) for o in others))

    if grades:
        print("\n-- Grades")
        print("  %-5s %4s %6s %3s %3s  %5s %5s %5s %5s %5s" % ("grade", "niv", "PV", "PA", "PM",
                                                             "For", "Int", "Cha", "Agi", "Sag"))
        for g in grades:
            print("  %-5s %4s %6s %3s %3s  %5s %5s %5s %5s %5s" % (
                g["grade"], g["level"], g["lifePoints"], g["actionPoints"], g["movementPoints"],
                g["strength"], g["intelligence"], g["chance"], g["agility"], g["wisdom"]))
        g = grades[g_idx - 1]
        print("\n-- Grade %s (niv %s)" % (g["grade"], g["level"]))
        print("  Résistances % : " + "  ".join("%s %+d" % (lbl, g.get(k, 0)) for k, lbl in RESISTS))
        carac = sorted(CARACS, key=lambda c: -g.get(c[0], 0))
        vals = [g.get(c[0], 0) for c in carac]
        if vals[0] > vals[-1]:
            print("  Caractéristique dominante : %s (élément %s)" % (carac[0][1], carac[0][2]))
        else:
            print("  Caractéristiques équilibrées (%s partout)" % vals[0])
        misc = [("tackleBonus", "Tacle"), ("tackleEvade", "Fuite"), ("paLostDodge", "Esquive PA"),
                ("pmLostDodge", "Esquive PM"), ("criticalHitBonus", "Coups critiques"),
                ("damageReflect", "Renvoi"), ("healBonus", "Soins")]
        misc = ["%s %+d" % (lbl, g[k]) for k, lbl in misc if g.get(k)]
        if misc:
            print("  Autres : " + "  ".join(misc))
    else:
        g_idx = 1

    print("\n-- Sorts (grade du monstre %s)" % g_idx)
    elements = set()
    for i, sid in enumerate(m.get("spells", [])):
        elements |= print_spell(sid, spell_grade_for(m, i, g_idx))
    if not m.get("spells"):
        print("  (aucun sort)")
    if elements:
        print("\n  Éléments des sorts (dégâts, vol, soins) : " + ", ".join(sorted(elements)))

    subs = m.get("subareas", [])
    if subs:
        print("\n-- Zones (%s)" % len(subs))
        for s in subs[:15]:
            d = get("subareas/%s" % s) or {}
            print("  - %s (niv %s)" % (fr(d.get("name")) or s, d.get("level", "?")))
        if len(subs) > 15:
            print("  … et %s autres" % (len(subs) - 15))


def cmd_famille(args):
    m, _ = resolve(args.monstre)
    race = m["race"]
    q = [("race", race), ("$limit", 100)] + [("$select[]", s) for s in
                                             ("id", "name", "isBoss", "isMiniBoss", "hideInBestiary",
                                              "isQuestMonster", "subareas", "grades")]
    data = (get("monsters?" + urllib.parse.urlencode(q, safe="[]$")) or {}).get("data", [])
    print("=== Race %s (%s monstres)" % (name_of("monster-races", race), len(data)))
    for x in sorted(data, key=lambda x: (min((g["level"] for g in x.get("grades", [])), default=0), x["id"])):
        lv = [g["level"] for g in x.get("grades", [])]
        lv = "%s-%s" % (min(lv), max(lv)) if lv else "?"
        f = flags(x)
        print("%6s  %-32s niv %-8s %s" % (x["id"], fr(x["name"]), lv, ("[" + ", ".join(f) + "]") if f else ""))


def main():
    global REFRESH
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--rafraichir", action="store_true", help="ignorer le cache")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("cherche")
    s.add_argument("texte")
    s.set_defaults(func=cmd_cherche)
    s = sub.add_parser("fiche")
    s.add_argument("monstre", help="nom FR ou id DofusDB")
    s.add_argument("--grade", type=int, help="grade à détailler (défaut : le plus haut)")
    s.set_defaults(func=cmd_fiche)
    s = sub.add_parser("famille")
    s.add_argument("monstre", help="nom FR ou id DofusDB d'un membre de la famille")
    s.set_defaults(func=cmd_famille)
    args = p.parse_args()
    REFRESH = args.rafraichir
    args.func(args)


if __name__ == "__main__":
    main()
