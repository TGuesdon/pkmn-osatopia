# Famille Tilamproie

> Dans Dofus, Tilamproie (lamproie, sorts Eau/Terre : *Succion Attractive*,
> *Morsure Filtrante*) et Mantaze (raie manta, sorts Air/Feu/Neutre : *Éclair
> Obscur*, *Électrochoc*, *Foudre Marine*) sont deux monstres niv. 200 des
> Vestiges engloutis (race « Monstres des ruines sous-marines »). Ils ne
> forment pas une évolution dans Dofus : la chaîne est un choix Osatopia.
> Évolutions : Tilamproie → Mantaze (niv. 30).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

## Intention

Archétype : attaquant à boost spécial, secondaire météo (profiteur de pluie).
Références : Lanturn (movepool), Staross (profil Eau spécial rapide et
fragile), Démanta (physique de raie, Glissade).

Monstre de milieu de jeu, commun sur les routes maritimes. Contrairement à
Lanturn, il n'est **pas** un encaisseur : les PV de Lanturn sont redistribués
en AtqSpé et en Vitesse. Avec **Glissade**, **Danse Pluie** double sa Vitesse,
rend **Fatal-Foudre** précis à 100 % et booste **Hydrocanon**.

## Stades

| | Tilamproie | Mantaze |
|---|---|---|
| Types | Eau / Électrik | Eau / Électrik |
| PV | 50 | 75 |
| Attaque | 35 | 45 |
| Défense | 40 | 55 |
| Atq. Spé | 75 | 115 |
| Déf. Spé | 45 | 70 |
| Vitesse | 70 | 105 |
| **Total** | **315** | **465** |
| Évolution | niv. 30 | – |
| Talents | Glissade / Absorbe-Volt / Lumiattirance (caché) | idem |
| Capture / Exp. | 190 / 66 | 75 / 170 |
| EV | AtqSpé +1 | AtqSpé +2, Vit +1 |

Comparaisons (`similaires`) : Larméléon (310) pour la base ; Élecsprint (475),
Malamandre (480), Lanturn (460) pour le final. Côté Osatopia, Dokachu
(Vol/Électrik, 460) et Morfrelon (Vol/Poison, 485) : Mantaze a plus d'AtqSpé,
moins de Vitesse brute (compensée par la pluie) et des types différents.
Stats sacrifiées : l'Attaque (purement spécial) et la Défense (une raie
fragile, faible au Sol).

Placeholders remplacés par défaut (valeurs Bitouf) : 50 % femelle,
`eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`. Groupe d'œuf
Eau 2 (comme Lanturn), couleur bleue (à ajuster selon les sprites).

## Kit final

| Emplacement | Choix | Type · Cat. | Puiss. |
|---|---|---|---|
| STAB Électrik | **Fatal-Foudre** (Thunder) | Électrik · Spé. | 110 |
| STAB Eau | **Hydrocanon** (Hydro Pump) | Eau · Spé. | 110 |
| Boost | **Danse Pluie** (Rain Dance) ou **Machination** (Nasty Plot) | Eau / Ténèbres · Statut | – |
| Couverture | **Laser Glace** (Ice Beam) | Glace · Spé. | 90 |

Alternatives : Boule Élek, Voltageôle, Saumure, Ocroupi, Chargeur, Onde Folie.

Talents : Glissade (Swift Swim), Absorbe-Volt (Volt Absorb), Lumiattirance
(Illuminate) en talent caché, rare et utile hors combat.

## Capacités custom

Aucune. Clins d'œil aux sorts Dofus : Parabocharge (*Succion Attractive*),
Saumure (*Électrochoc*, dégâts sur cible entamée), Voltageôle (*Éclair
Obscur*), Fatal-Foudre (*Foudre Marine*).

## Learnsets

Mantaze reprend les attaques de Tilamproie jusqu'au niv. 28 aux mêmes
niveaux. Machination et Fatal-Foudre sont exclusives à Mantaze.

### Tilamproie

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| 1 | Pistolet à O (Water Gun) | Eau | Spé. | 40 | STAB faible |
| 1 | Éclair (Thunder Shock) | Électrik | Spé. | 40 | STAB faible |
| 1 | Ultrason (Supersonic) | Normal | Statut | – | Confusion |
| 5 | Cage Éclair (Thunder Wave) | Électrik | Statut | – | Paralysie |
| 9 | Vibraqua (Water Pulse) | Eau | Spé. | 60 | STAB |
| 13 | Boule Élek (Electro Ball) | Électrik | Spé. | var. | STAB selon la Vitesse |
| 17 | Onde Folie (Confuse Ray) | Spectre | Statut | – | Perturbation |
| 21 | Parabocharge (Parabolic Charge) | Électrik | Spé. | 65 | Drain |
| 25 | Saumure (Brine) | Eau | Spé. | 65 | ×2 sous 50 % PV |
| 28 | Chargeur (Charge) | Électrik | Statut | – | Boost |
| 32 | Ocroupi (Muddy Water) | Eau | Spé. | 90 | STAB fort |
| 36 | Ondes Étranges (Eerie Impulse) | Électrik | Statut | – | AtqSpé −2 |
| 40 | Danse Pluie (Rain Dance) | Eau | Statut | – | Météo |
| 45 | Hydrocanon (Hydro Pump) | Eau | Spé. | 110 | STAB final |

### Mantaze

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| Évo | Voltageôle (Thunder Cage) | Électrik | Spé. | 80 | Attaque d'évolution, piège |
| 1 | Ondes Étranges (Eerie Impulse) | Électrik | Statut | – | Rappel |
| 1–28 | *mêmes attaques que Tilamproie* | | | | |
| 33 | Ocroupi (Muddy Water) | Eau | Spé. | 90 | STAB fort |
| 37 | Danse Pluie (Rain Dance) | Eau | Statut | – | Météo |
| 41 | Machination (Nasty Plot) | Ténèbres | Statut | – | Boost (exclusif) |
| 45 | Hydrocanon (Hydro Pump) | Eau | Spé. | 110 | STAB final |
| 50 | Fatal-Foudre (Thunder) | Électrik | Spé. | 110 | Attaque finale (exclusive) |

## CT, CS et tuteurs

| | Tilamproie | Mantaze |
|---|---|---|
| Toxik, Abri, Repos, Façade, Reflet, Attraction, Faux-Chage | ✅ | ✅ |
| Mur Lumière, Rune Protect, Danse Pluie | ✅ | ✅ |
| Vibraqua, Surf, Plongée, Cascade | ✅ | ✅ |
| Onde de Choc, Tonnerre | ✅ | ✅ |
| Laser Glace, Ball'Ombre | ✅ | ✅ |
| Blabla Dodo, Ronflement, Ténacité, Vantardise, Vent Glace, Météores (tuteurs) | ✅ | ✅ |
| Fatal-Foudre | – | ✅ |
| Blizzard, Ultralaser | – | ✅ |

Exclus volontairement :
- **Fatal-Foudre** en CT pour Tilamproie : récompense de Mantaze ;
- coups de poing (Poing-Éclair, Poing-Glace…), Casse-Brique : pas de membres ;
- Séisme, Tunnel, Vol : incohérents ;
- Psyko : pour se distinguer de Dokachu ;
- attaques Plante, Grêle (en conflit avec la pluie) ;
- Provoc, Tourmente : pas de rôle de perturbateur ;
- Cage Éclair en tuteur : déjà apprise par niveau.

## Annexe — bloc C

Voir `src/data/pokemon/species_info.h` (`SPECIES_TILAMPROIE`,
`SPECIES_MANTAZE`).
