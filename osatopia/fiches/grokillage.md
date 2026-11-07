# Famille Grokillage

> Coquillage des fonds marins qui se brise pour devenir une moule ninja
> (lore et élément des sorts Dofus **à vérifier**). On le trouve dans les
> zones de plongée. — Évolutions : Grokillage → Moumoule (niv. 30).
> Constantes : `SPECIES_GROKILLAGE`, `SPECIES_MOUMOULE`.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`).

## Intention

Archétype : **attaquant à boost** (principal) + **nettoyeur rapide**
(secondaire), **mixte à dominante spéciale**. Références : Coquiperl (profil
de Grokillage, Exuviation), Crustabri (Multi-Coups, Coque Armure, la combinaison
« coquille brisée + attaques multi-coups »), Amphinobi (le ninja aquatique,
Sheauriken).

Pourquoi : Grokillage est une coquille lente et défensive. Moumoule l'a
brisée : il est rapide et fragile, et il brise encore sa protection avec
**Exuviation** pour tout balayer. Il se distingue de **Tortue Bleue**, l'autre
ninja Eau/Combat, qui est physique (Att 115, AtqSpé 45) et utilise Danse Lames.
Moumoule frappe surtout en spécial, avec **Sheauriken** + **Multi-Coups**
(5 × 15, priorité +1), Onde Vide et Aurasphère.

**Plongée** : CS Plongée arrive tard (vers le niveau 40 de l'équipe). Des
Grokillage sauvages trouvés uniquement en plongée seraient donc proches de leur
niveau d'évolution. Piste : Moumoule en plongée, Grokillage en surf ou à la
pêche. À trancher au moment de placer les rencontres.

## Stades

| | Grokillage | Moumoule |
|---|---|---|
| Types | Eau | Eau / Combat |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 50 / 55 / 90 / 65 / 45 / 35 | 65 / 85 / 75 / 105 / 60 / 110 |
| Total | 340 | 500 |
| Talents | Multi-Coups (Skill Link) / Coque Armure (Shell Armor) / (caché) Technicien (Technician) | idem |
| Capture / Exp. | 120 / 70 | 45 / 195 |
| EV | 1 Déf | 2 AtqSpé + 1 Vit |
| Évolution | niv. 30 | – |

Autres valeurs, faute d'indication (reprises de la famille Bitouf) : 50 %
femelle, 15 cycles d'œuf, croissance Medium Slow, amitié standard. Groupe
d'œuf Eau 3 (coquillages), bodyColor gris (Grokillage) et noir (Moumoule).

Comparaison : Coquiperl 35/64/85/74/55/32 (345), Amphinobi 72/95/67/103/71/122
(530), Élecsprint 70/75/60/105/60/105 (475), Kwak Feu 77/82/66/108/70/97 (500),
Tortue Bleue 75/115/80/45/65/100 (480).

## Kit final

| Rôle | Attaque |
|---|---|
| Boost | Exuviation (Shell Smash) |
| STAB Eau fort | Hydrocanon (Hydro Pump), 110 |
| STAB Combat | Aurasphère (Aura Sphere), 80, ne rate jamais |
| Priorité | Sheauriken (Water Shuriken), 15 × 2–5, prio +1 (× 5 avec Multi-Coups) |
| Couverture | Kokiyarme (Shell Side Arm), Laser Glace (CT), Bombe Beurk (CT) |

## Capacités custom

Aucune.

## Learnsets

**Grokillage**

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Pistolet à O (Water Gun) | Eau | Spéciale | 40 |
| 1 | Repli (Withdraw) | Eau | Statut | – |
| 5 | Ultrason (Supersonic) | Normal | Statut | – |
| 9 | Siphon (Whirlpool) | Eau | Spéciale | 35 |
| 13 | Vibraqua (Water Pulse) | Eau | Spéciale | 60 |
| 17 | Détritus (Sludge) | Poison | Spéciale | 65 |
| 21 | Mur de Fer (Iron Defense) | Acier | Statut | – |
| 25 | Onde Boréale (Aurora Beam) | Glace | Spéciale | 65 |
| 29 | Saumure (Brine) | Eau | Spéciale | 65 |

**Moumoule** (reprend les attaques de Grokillage aux mêmes niveaux)

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Sheauriken (Water Shuriken) | Eau | Spéciale | 15, prio +1 |
| 33 | Onde Vide (Vacuum Wave) | Combat | Spéciale | 40, prio +1 |
| 37 | Aurasphère (Aura Sphere) | Combat | Spéciale | 80 |
| 41 | Kokiyarme (Shell Side Arm) | Poison | Spéciale | 90 |
| 45 | Exuviation (Shell Smash) | Normal | Statut | – |
| 49 | Hydrocanon (Hydro Pump) | Eau | Spéciale | 110 |
| 54 | Exploforce (Focus Blast) | Combat | Spéciale | 120 |

Claquoir (Clamp), envisagé au départ, est écarté : il est inutilisable dans
l'expansion.

## CT, CS et tuteurs

| Attaque | Grokillage | Moumoule |
|---|---|---|
| Vibraqua, Toxik, Grêle, Laser Glace, Blizzard, Mur Lumière, Abri, Danse Pluie, Reflet, Protection, Façade, Repos, Attraction | ✓ | ✓ |
| CS Surf, Plongée | ✓ | ✓ |
| Tuteurs Ténacité, Blabla Dodo, Ronflement, Vent Glace | ✓ | ✓ |
| Casse-Brique, Éclate-Roc, Force, Cascade | – | ✓ |
| Bombe Beurk, Provoc, Ultralaser, tuteur Vantardise | – | ✓ |

Exclusions volontaires : Plénitude, Gonflette et Danse Lames (Exuviation reste
le seul boost) ; Mitra-Poing et les tuteurs Poing-Glace, Poing-Éclair et Poing
de Feu (une moule n'a pas de poings) ; Tonnerre, Psyko et Ball'Ombre (pas
cohérents avec le monstre).
