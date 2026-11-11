#!/usr/bin/env python3
"""Calcule pokemonScale / pokemonOffset / trainerScale / trainerOffset (comparaison
de taille du Pokédex) à partir de `.height` et du sprite de face.

Produit en croix sur la hauteur *visible* du sprite (pixels non transparents de la
première frame), calibré sur les Pokémon des générations 1 à 3 :
    pokemonScale / trainerScale = hauteur visible (px) / (3.94 × height (dm))
La plus petite des deux échelles vaut 256 (taille réelle) ; l'autre rétrécit.

À lancer depuis la racine du dépôt :

    python3 .claude/skills/concevoir-monstre/scripts/echelle_pokedex.py SPECIES_TOFU SPECIES_GWO_TOFU
    python3 .claude/skills/concevoir-monstre/scripts/echelle_pokedex.py --ecrire SPECIES_TOFU

Sans --ecrire, affiche les valeurs ; avec --ecrire, les écrit dans species_info.h.
"""
import re
import sys

import numpy as np
from PIL import Image

K = 3.94          # px visibles par dm, à échelle 256 (médiane vanilla)
SOL = 61          # ligne de sol (px) quand le Pokémon est rétréci
SOL_256 = 62      # ligne de sol (px) à taille réelle
ESPECES = 'src/data/pokemon/species_info.h'


def hauteur_visible(png):
    a = np.array(Image.open(png))[:64, :64]
    ys = np.nonzero(a != 0)[0]
    return ys.min(), ys.max() + 1


def echelles(height, haut, bas):
    r = (bas - haut) / (K * height)
    if r >= 1:
        ps, ts = round(256 * r), 256
        po = round(SOL - (32 + (bas - 32) * 256 / ps))
    else:
        ps, ts = 256, round(256 / r)
        po = int(SOL_256 - bas)
    to = max(0, round(25.2 * (1 - 256 / ts) - 1)) if ts > 256 else 0
    return {'pokemonScale': ps, 'pokemonOffset': po, 'trainerScale': ts, 'trainerOffset': to}


def main():
    ecrire = '--ecrire' in sys.argv
    cibles = [a for a in sys.argv[1:] if a.startswith('SPECIES_')]
    if not cibles:
        print(__doc__)
        return
    gfx = open('src/data/graphics/pokemon.h', encoding='utf-8').read()
    src = open(ESPECES, encoding='utf-8').read()
    parts = re.split(r'(\n    \[SPECIES_\w+\]\s*=\s*\n    \{)', src)
    for i in range(1, len(parts), 2):
        cle = re.search(r'SPECIES_\w+', parts[i]).group(0)
        if cle not in cibles:
            continue
        corps = parts[i + 1]
        height = int(re.search(r'\.height = (\d+)', corps).group(1))
        sym = re.search(r'\.frontPic = (gMonFrontPic_\w+)', corps).group(1)
        dossier = re.search(sym + r'\[\] = INCBIN_U32\("(graphics/pokemon/[^"]+?)/anim_front', gfx).group(1)
        haut, bas = hauteur_visible(dossier + '/anim_front.png')
        valeurs = echelles(height, haut, bas)
        print(cle, valeurs)
        for champ, v in valeurs.items():
            corps = re.sub(r'(\.%s = )-?\d+' % champ, lambda m: m.group(1) + str(v), corps, count=1)
        parts[i + 1] = corps
    if ecrire:
        open(ESPECES, 'w', encoding='utf-8').write(''.join(parts))


if __name__ == '__main__':
    main()
