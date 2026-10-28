"""Génère les glossaires FR (attaques, talents, Pokémon) dans ../data/.

Usage :
    python3 generer_glossaires.py <dossier_csv_pokeapi>

Le dossier doit contenir les CSV de PokeAPI
(https://github.com/PokeAPI/pokeapi/tree/master/data/v2/csv) :
moves, move_names, move_flavor_text, abilities, ability_names,
ability_flavor_text, pokemon_species, pokemon_species_names.
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import osatopia_data as od  # noqa: E402

FR = "5"
EN = "9"

# Constantes de l'expansion dont le nom diffère de l'identifiant PokeAPI.
ALIASES = {
    "MOVE_SOFTBOILED": "soft-boiled",
    "MOVE_SELF_DESTRUCT": "self-destruct",
    "MOVE_U_TURN": "u-turn",
    "MOVE_V_CREATE": "v-create",
    "MOVE_X_SCISSOR": "x-scissor",
    "MOVE_WILL_O_WISP": "will-o-wisp",
    "MOVE_DOUBLE_EDGE": "double-edge",
    "MOVE_LOCK_ON": "lock-on",
    "MOVE_WAKE_UP_SLAP": "wake-up-slap",
    "MOVE_MUD_SLAP": "mud-slap",
    "MOVE_SAND_ATTACK": "sand-attack",
    "MOVE_VISE_GRIP": "vice-grip",
    "MOVE_HI_JUMP_KICK": "high-jump-kick",
    "MOVE_SMELLING_SALTS": "smelling-salts",
    "MOVE_FAINT_ATTACK": "feint-attack",
    "MOVE_FEINT_ATTACK": "feint-attack",
    "MOVE_ROLE_PLAY": "role-play",
    "MOVE_SOLAR_BEAM": "solar-beam",
    "MOVE_SOLAR_BLADE": "solar-blade",
    "MOVE_SPIKES": "spikes",
    "ABILITY_COMPOUND_EYES": "compound-eyes",
}


def read_csv(folder, name):
    with open(os.path.join(folder, name + ".csv"), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def names_by_id(rows, id_col, lang):
    return {r[id_col]: r["name"] for r in rows if r["local_language_id"] == lang}


def flavor_by_id(rows, id_col, lang_col):
    """Description FR la plus récente."""
    best = {}
    for r in rows:
        if r[lang_col] != FR:
            continue
        vg = int(r["version_group_id"])
        if r[id_col] not in best or vg >= best[r[id_col]][0]:
            txt = r["flavor_text"].replace("\xad\n", "").replace("\\n", " ").replace("\n", " ").replace("\x0c", " ")
            best[r[id_col]] = (vg, " ".join(txt.split()))
    return {k: v[1] for k, v in best.items()}


def to_const(prefix, identifier):
    return prefix + identifier.upper().replace("-", "_")


def build_index(rows, prefix):
    """constante -> id PokeAPI."""
    idx = {to_const(prefix, r["identifier"]): r["id"] for r in rows}
    by_ident = {r["identifier"]: r["id"] for r in rows}
    for const, ident in ALIASES.items():
        if const.startswith(prefix) and ident in by_ident:
            idx[const] = by_ident[ident]
    # Variante sans underscores (ex. SOFTBOILED vs SOFT_BOILED)
    loose = {od.norm(k): v for k, v in idx.items()}
    return idx, loose


def lookup(const, idx, loose):
    return idx.get(const) or loose.get(od.norm(const))


def write_csv(name, header, rows):
    os.makedirs(od.DATA_DIR, exist_ok=True)
    with open(os.path.join(od.DATA_DIR, name), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    folder = sys.argv[1]
    root = od.find_repo_root()
    missing = []

    # Attaques
    moves = read_csv(folder, "moves")
    idx, loose = build_index(moves, "MOVE_")
    names = read_csv(folder, "move_names")
    fr, en = names_by_id(names, "move_id", FR), names_by_id(names, "move_id", EN)
    flav = flavor_by_id(read_csv(folder, "move_flavor_text"), "move_id", "language_id")
    learnable = od.learnable_move_consts(root)
    rows = []
    for const, m in od.load_moves(root).items():
        if const == "MOVE_NONE" or const not in learnable:
            continue
        pid = lookup(const, idx, loose)
        if not pid or pid not in fr:
            missing.append(const)
        rows.append([
            const, fr.get(pid, ""), en.get(pid, m["name_en"]), od.type_fr(m["type"]),
            od.CATEGORIES_FR.get(m["category"], m["category"]), m["power"] or "",
            m["accuracy"] or "", m["pp"], m["priority"], m["effect"], flav.get(pid, ""),
        ])
    rows.sort(key=lambda r: r[1] or r[2])
    write_csv("attaques.csv", ["constante", "nom_fr", "nom_en", "type", "categorie", "puissance",
                               "precision", "pp", "priorite", "effet", "description_fr"], rows)
    n_moves = len(rows)

    # Talents
    abil = read_csv(folder, "abilities")
    idx, loose = build_index(abil, "ABILITY_")
    names = read_csv(folder, "ability_names")
    fr, en = names_by_id(names, "ability_id", FR), names_by_id(names, "ability_id", EN)
    flav = flavor_by_id(read_csv(folder, "ability_flavor_text"), "ability_id", "language_id")
    rows = []
    for const, a in od.load_abilities(root).items():
        if const == "ABILITY_NONE":
            continue
        pid = lookup(const, idx, loose)
        if not pid or pid not in fr:
            missing.append(const)
        rows.append([const, fr.get(pid, ""), en.get(pid, a["name_en"]), flav.get(pid, "")])
    rows.sort(key=lambda r: r[1] or r[2])
    write_csv("talents.csv", ["constante", "nom_fr", "nom_en", "description_fr"], rows)
    n_abil = len(rows)

    # Pokémon (espèces de base, hors formes et monstres custom)
    spec = read_csv(folder, "pokemon_species")
    idx, loose = build_index(spec, "SPECIES_")
    names = read_csv(folder, "pokemon_species_names")
    fr, en = names_by_id(names, "pokemon_species_id", FR), names_by_id(names, "pokemon_species_id", EN)
    rows = []
    for r in spec:
        const = to_const("SPECIES_", r["identifier"])
        rows.append([const, fr.get(r["id"], ""), en.get(r["id"], "")])
    write_csv("pokemon.csv", ["constante", "nom_fr", "nom_en"], rows)

    print("attaques.csv : %d | talents.csv : %d | pokemon.csv : %d" % (n_moves, n_abil, len(rows)))
    if missing:
        print("Sans traduction FR (%d) : %s" % (len(missing), " ".join(missing)))


if __name__ == "__main__":
    main()
