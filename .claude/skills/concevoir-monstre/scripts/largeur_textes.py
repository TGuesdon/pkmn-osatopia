#!/usr/bin/env python3
"""Vérifie que les noms et descriptions de talents et d'attaques tiennent à l'écran.

Reproduit les limites de test/text.c (largeur en pixels, polices du jeu) sans
lancer `make check`. À lancer depuis la racine du dépôt :

    python3 .claude/skills/concevoir-monstre/scripts/largeur_textes.py
    python3 .claude/skills/concevoir-monstre/scripts/largeur_textes.py "Texte à mesurer"

Sans argument, liste les textes trop larges ; avec des arguments, affiche la
largeur de chacun en FONT_NORMAL (talents : 146 px, attaques : 152 px par ligne).
"""
import re
import sys

ROOT = '.'


def charger_charmap():
    cm = {}
    for line in open(f'{ROOT}/charmap.txt', encoding='utf-8'):
        m = re.match(r"^'(\\?.)'\s*=\s*([0-9A-Fa-f]{2})\b", line)
        if m:
            ch = m.group(1)
            if ch.startswith('\\'):
                ch = ch[1:]
            cm.setdefault(ch, int(m.group(2), 16))
    return cm


def charger_police(nom):
    src = open(f'{ROOT}/src/fonts.c', encoding='utf-8').read()
    m = re.search(nom + r"\[\] = \{(.*?)\};", src, re.S)
    return [int(x) for x in re.findall(r'\d+', m.group(1))]


CM = charger_charmap()
POLICES = {
    'normal': charger_police('gFontNormalLatinGlyphWidths'),
    'narrower': charger_police('gFontNarrowerLatinGlyphWidths'),
    'small_narrower': charger_police('gFontSmallNarrowerLatinGlyphWidths'),
}


def largeur(texte, police='normal'):
    """Largeur de la ligne la plus longue, en pixels."""
    best = 0
    for ligne in texte.replace('\\n', '\n').split('\n'):
        w = 0
        for c in ligne:
            if c not in CM:
                print(f'  caractère inconnu de charmap.txt : {c!r}', file=sys.stderr)
                w += 6
                continue
            w += POLICES[police][CM[c]]
        best = max(best, w)
    return best


CHAINE = r'"((?:[^"\\]|\\.)*)"'


def verifier(etiquette, texte, motif, police, limite):
    for m in re.finditer(motif, texte):
        s = ''.join(re.findall(CHAINE, m.group(1))) if m.group(1).startswith('"') else m.group(1)
        w = largeur(s, police)
        if w > limite:
            print(f'{etiquette} {w} > {limite} px : {s}')


def main():
    if len(sys.argv) > 1:
        for s in sys.argv[1:]:
            print(f'{largeur(s)} px : {s}')
        return
    talents = open(f'{ROOT}/src/data/abilities.h', encoding='utf-8').read()
    attaques = open(f'{ROOT}/src/data/moves_info.h', encoding='utf-8').read()
    # Seules les attaques Osatopia : la fin du fichier contient les capacités Z/Max,
    # que les tests de noms ignorent.
    debut = attaques.index('// Osatopia')
    fin = attaques.index('[MOVE_BREAKNECK_BLITZ]')
    attaques = attaques[debut:fin]
    verifier('Description de talent', talents, r'\.description = COMPOUND_STRING\(' + CHAINE + r'\)', 'normal', 146)
    verifier('Nom de talent', talents, r'\.name = _\(' + CHAINE + r'\)', 'normal', 144)
    verifier('Nom de talent (pop-up)', talents, r'\.name = _\(' + CHAINE + r'\)', 'small_narrower', 76)
    verifier('Description d\'attaque', attaques,
             r'\.description = COMPOUND_STRING\(\s*((?:"(?:[^"\\]|\\.)*"\s*)+)\)', 'normal', 152)
    verifier('Nom d\'attaque', attaques, r'\.name = COMPOUND_STRING\(' + CHAINE + r'\)', 'narrower', 72)
    especes = open(f'{ROOT}/src/data/pokemon/species_info.h', encoding='utf-8').read()
    verifier('Description Pokédex', especes,
             r'\.description = COMPOUND_STRING\(\s*((?:"(?:[^"\\]|\\.)*"\s*)+)\)', 'normal', 224)
    for m in re.finditer(r'\.description = COMPOUND_STRING\(\s*((?:"(?:[^"\\]|\\.)*"\s*)+)\)', especes):
        lignes = ''.join(re.findall(CHAINE, m.group(1))).split('\\n')
        if len(lignes) > 4:
            print(f'Description Pokédex sur {len(lignes)} lignes (max 4) : {lignes[0]}')
    for m in re.finditer(r'\.categoryName = _\(' + CHAINE + r'\)', especes):
        if len(m.group(1)) > 12:
            print(f'Catégorie Pokédex de {len(m.group(1))} caractères (max 12) : {m.group(1)}')


if __name__ == '__main__':
    main()
