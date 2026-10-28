"""Outil de consultation (lecture seule) pour concevoir les monstres d'Osatopia.

    python3 osatopia.py fiche <nom>          # Pokémon ou monstre custom (FR, EN, SPECIES_X, nom en jeu)
    python3 osatopia.py attaques [filtres]   # --type feu --categorie physique --pmin 60 --pmax 90
                                             # --effet SUCKER --texte priorité --prio
    python3 osatopia.py talents [--texte mot]
    python3 osatopia.py similaires PV ATT DEF ATQSPE DEFSPE VIT [--n 10] [--type feu] [--custom]
    python3 osatopia.py custom               # monstres Osatopia déjà créés + learnsets en double
"""
import argparse
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import osatopia_data as od  # noqa: E402

ROOT = od.find_repo_root()
G_MOVES = od.load_glossary("attaques.csv")
G_ABIL = od.load_glossary("talents.csv")
G_MON = od.load_glossary("pokemon.csv")


def move_label(const, moves):
    m = moves.get(const, {})
    g = G_MOVES.get(const, {})
    name = g.get("nom_fr") or m.get("name_en") or const
    cat = od.CATEGORIES_FR.get(m.get("category", ""), "?")
    power = m.get("power") or "-"
    prio = " prio%+d" % m["priority"] if m.get("priority") else ""
    return "%-22s %-9s %-8s %3s%s  (%s)" % (name, od.type_fr(m.get("type", "")), cat, power, prio,
                                            g.get("nom_en") or const)


def mon_name(sp):
    g = G_MON.get(sp["const"])
    if g and g["nom_fr"]:
        return g["nom_fr"]
    return sp["name_game"] or sp["const"]


def ability_name(const):
    g = G_ABIL.get(const)
    return "%s (%s)" % (g["nom_fr"], g["nom_en"]) if g and g["nom_fr"] else const


def stats_line(stats):
    return " / ".join("%s %d" % (lbl, v) for (_, lbl), v in zip(od.STAT_KEYS, stats)) + \
        "  | Total %d" % sum(stats)


def find_species(query, species):
    q = od.norm(query)
    q_const = "SPECIES_" + query.upper().replace("SPECIES_", "")
    if q_const in species:
        return species[q_const]
    for const, g in G_MON.items():
        if q in (od.norm(g["nom_fr"]), od.norm(g["nom_en"])) and const in species:
            return species[const]
    for sp in species.values():
        if od.norm(sp["name_game"]) == q or od.norm(sp["const"].replace("SPECIES_", "")) == q:
            return sp
    cands = [s for s in species.values() if q in od.norm(mon_name(s)) or q in od.norm(s["const"])]
    if len(cands) == 1:
        return cands[0]
    if cands:
        sys.exit("Plusieurs correspondances : " + ", ".join("%s (%s)" % (mon_name(s), s["const"]) for s in cands[:15]))
    sys.exit("Aucun Pokémon trouvé pour « %s »" % query)


def cmd_fiche(args):
    species = od.load_species(ROOT)
    moves = od.load_moves(ROOT)
    sp = find_species(" ".join(args.nom), species)
    print("%s — %s%s" % (mon_name(sp), sp["const"], "  [CUSTOM OSATOPIA]" if sp["custom"] else ""))
    print("Types   : " + " / ".join(od.type_fr(t) for t in sp["types"]))
    print("Stats   : " + stats_line(sp["stats"]))
    print("Talents : " + ", ".join(ability_name(a) for a in sp["abilities"]))
    if sp["evolutions"]:
        print("Évol.   : " + sp["evolutions"])
    learnsets = od.load_level_up_learnsets(ROOT)
    lu = learnsets.get(sp["levelUp"], [])
    print("\nAttaques par niveau (%s) :" % (sp["levelUp"] or "aucune"))
    for lvl, mv in lu:
        print("  %3s  %s" % ("Évo" if lvl == 0 else lvl, move_label(mv, moves)))
    if args.complet:
        for title, key, fname in [("CT/Tuteurs", "teachable", "teachable_learnsets.h"),
                                  ("Attaques œuf", "eggMoves", "egg_moves.h")]:
            lst = od.load_move_lists(ROOT, fname).get(sp[key], [])
            print("\n%s (%d) :" % (title, len(lst)))
            for mv in sorted(lst, key=lambda c: (moves.get(c, {}).get("type", ""), -moves.get(c, {}).get("power", 0))):
                print("       " + move_label(mv, moves))


def cmd_attaques(args):
    moves = od.load_moves(ROOT)
    learnable = od.learnable_move_consts(ROOT)
    cat = None
    if args.categorie:
        c = od.norm(args.categorie)
        cat = "PHYSICAL" if c.startswith("phys") else "SPECIAL" if c.startswith("spe") else "STATUS"
    rows = []
    for const, m in moves.items():
        if const not in learnable or const == "MOVE_NONE":
            continue
        g = G_MOVES.get(const, {})
        if args.type and m["type"] != od.type_const(args.type):
            continue
        if cat and m["category"] != cat:
            continue
        if args.pmin is not None and m["power"] < args.pmin:
            continue
        if args.pmax is not None and m["power"] > args.pmax:
            continue
        if args.prio and m["priority"] <= 0:
            continue
        if args.effet and args.effet.upper() not in m["effect"]:
            continue
        if args.texte and od.norm(args.texte) not in od.norm(g.get("description_fr", "") + g.get("nom_fr", "")):
            continue
        rows.append((m["type"], -m["power"], const, g.get("description_fr", "")))
    for _, _, const, desc in sorted(rows):
        print(move_label(const, moves))
        if args.desc and desc:
            print("      " + desc)
    print("\n%d attaques" % len(rows))


def cmd_talents(args):
    for const, g in sorted(G_ABIL.items(), key=lambda kv: kv[1]["nom_fr"]):
        if args.texte and od.norm(args.texte) not in od.norm(g["description_fr"] + g["nom_fr"] + g["nom_en"]):
            continue
        print("%-22s %-20s %s" % (g["nom_fr"], g["nom_en"], g["description_fr"]))


def cmd_similaires(args):
    target = args.stats
    species = od.load_species(ROOT)
    t_total = sum(target)
    t_norm = [v / t_total for v in target]
    res = []
    for sp in species.values():
        if sp["custom"] != args.custom or sum(sp["stats"]) == 0:
            continue
        if not args.custom and sp["const"] not in G_MON:
            continue  # ignore les formes (Méga, régionales...) sauf si demandé
        if args.type and od.type_const(args.type) not in sp["types"]:
            continue
        total = sum(sp["stats"])
        shape = math.sqrt(sum((a - b / total) ** 2 for a, b in zip(t_norm, sp["stats"])))
        score = shape * 10 + abs(total - t_total) / 100
        res.append((score, sp))
    print("Cible : " + stats_line(target))
    for _, sp in sorted(res, key=lambda r: r[0])[:args.n]:
        print("  %-16s %-18s %s" % (mon_name(sp), "/".join(od.type_fr(t) for t in sp["types"]), stats_line(sp["stats"])))


def cmd_custom(args):
    species = od.load_species(ROOT)
    learnsets = od.load_level_up_learnsets(ROOT)
    customs = [s for s in species.values() if s["custom"] and s["const"] != "SPECIES_NONE"]
    done = [s for s in customs if len(set(s["stats"])) > 1]
    todo = [s for s in customs if len(set(s["stats"])) <= 1]

    # Familles = composantes reliées par les évolutions
    family = {s["const"]: s["const"] for s in customs}

    def find(c):
        while family[c] != c:
            c = family[c]
        return c
    for s in customs:
        for target in re.findall(r"SPECIES_\w+", s["evolutions"]):
            if target in family:
                family[find(target)] = find(s["const"])

    print("Monstres conçus (%d) :" % len(done))
    for sp in done:
        print("  %-14s %-28s %-16s %s" % (mon_name(sp), sp["const"], "/".join(od.type_fr(t) for t in sp["types"]),
                                           stats_line(sp["stats"])))
    print("\nÀ concevoir — stats placeholder (%d) :" % len(todo))
    print("  " + ", ".join(mon_name(s) for s in todo))

    seen = {}
    for sp in done:
        key = tuple(mv for _, mv in learnsets.get(sp["levelUp"], []))
        if key:
            seen.setdefault(key, []).append(sp)
    for group in seen.values():
        if len({find(s["const"]) for s in group}) > 1:
            print("\n⚠ Même learnset dans des familles différentes : " + ", ".join(mon_name(s) for s in group))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("fiche")
    s.add_argument("nom", nargs="+")
    s.add_argument("--complet", action="store_true", help="ajoute CT/tuteurs et attaques œuf")
    s.set_defaults(func=cmd_fiche)
    s = sub.add_parser("attaques")
    s.add_argument("--type")
    s.add_argument("--categorie")
    s.add_argument("--pmin", type=int)
    s.add_argument("--pmax", type=int)
    s.add_argument("--prio", action="store_true")
    s.add_argument("--effet")
    s.add_argument("--texte")
    s.add_argument("--desc", action="store_true", help="affiche la description FR")
    s.set_defaults(func=cmd_attaques)
    s = sub.add_parser("talents")
    s.add_argument("--texte")
    s.set_defaults(func=cmd_talents)
    s = sub.add_parser("similaires")
    s.add_argument("stats", nargs=6, type=int)
    s.add_argument("--n", type=int, default=10)
    s.add_argument("--type")
    s.add_argument("--custom", action="store_true", help="compare aux monstres Osatopia")
    s.set_defaults(func=cmd_similaires)
    s = sub.add_parser("custom")
    s.set_defaults(func=cmd_custom)
    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
