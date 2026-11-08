# Famille Mol Usk

> Limace des ruines sous-marines (Ville submergée, Ancienne Sufokia, Vestiges
> engloutis, Vaisseau du Capitaine Meno ; niv. 200–212). Sorts : *Bave Acide*
> (dégâts Air, -2 PA), *Traînée Collante* (pose un glyphe-aura, dégâts Feu),
> *Roulemboule* (dégâts Neutre, Érosion). Beaucoup de PV, +40 Fuite.
> — Évolutions : aucune.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; `.eggCycles = 20`, groupes d'œuf
`EGG_GROUP_WATER_1` / `EGG_GROUP_AMORPHOUS`, couleur `BODY_COLOR_PURPLE`.

## Intention

Archétype : **poseur de pièges** (+ usure). Les glyphes de Dofus deviennent
des pièges : **Pics Toxik** (poison à l'entrée) et **Toile Gluante** (la
*Traînée Collante*, -1 Vitesse à l'entrée). Lent et très résistant en spécial,
il pose, empoisonne, se soigne.

Références : **Prédastérie** (usure par le statut), **Tritosor** (Gastrodon,
la limace de mer massive, Glu), **Tentacruel** (même typage, Pics Toxik,
Suintement).

Eau/Poison : seul monstre custom avec ce typage. Faiblesses : Électrik, Sol,
Psy. Résistances : Feu, Eau, Glace, Combat, Poison, Insecte, Acier, Fée.

## Stades

| | Mol Usk |
|---|---|
| Types | Eau/Poison |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 110 / 50 / 80 / 80 / 120 / 35 |
| Total | 475 |
| Talents | Suintement (Liquid Ooze) / Glu (Sticky Hold) / caché : Lavabo (Storm Drain) |
| Capture / Exp. | 45 / 170 |
| EV | 2 DéfSpé |

Stats sacrifiées : Attaque (kit spécial ou de statut) et Vitesse (limace qui
pose ses pièges en encaissant). Comparé à Mamansot (custom le plus proche) :
+35 DéfSpé, moins d'AtqSpé et de Vitesse.

## Kit final

| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Glyphe : poison | Pics Toxik (Toxic Spikes) | Poison | Statut | – |
| Glyphe : ralentir | Toile Gluante (Sticky Web) | Insecte | Statut | – |
| STAB principal | Ébullition (Scald) | Eau | Spé | 80 |
| Récupération | Soin (Recover) | Normal | Statut | – |

Alternatives : Choc Venin (combo avec Pics Toxik), Bombe Beurk, Bain de Smog
(contre les boosts), Gaz Corrosif (rappel de *Bave Acide*), Anneau Hydro.

Talents : **Suintement** (bave toxique contre les voleurs de PV), **Glu**
(limace collante), **Lavabo** caché (absorbe les attaques Eau des zones
sous-marines). Aucun des trois n'est pris par un autre monstre custom.

## Capacités custom

Aucune.

## Learnsets

| Niv. | Attaque FR (EN) | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Pistolet à O (Water Gun) | Eau | Spé | 40 |
| 1 | Acide (Acid) | Poison | Spé | 40 |
| 5 | Sécrétion (String Shot) | Insecte | Statut | – |
| 9 | Bombe Acide (Acid Spray) | Poison | Spé | 40 |
| 13 | Vibraqua (Water Pulse) | Eau | Spé | 60 |
| 17 | Saumure (Brine) | Eau | Spé | 65 |
| 20 | Pics Toxik (Toxic Spikes) | Poison | Statut | – |
| 23 | Anneau Hydro (Aqua Ring) | Eau | Statut | – |
| 26 | Bain de Smog (Clear Smog) | Poison | Spé | 50 |
| 29 | Choc Venin (Venoshock) | Poison | Spé | 65 |
| 32 | Toile Gluante (Sticky Web) | Insecte | Statut | – |
| 35 | Ébullition (Scald) | Eau | Spé | 80 |
| 38 | Gaz Corrosif (Corrosive Gas) | Poison | Statut | – |
| 41 | Soin (Recover) | Normal | Statut | – |
| 44 | Bombe Beurk (Sludge Bomb) | Poison | Spé | 90 |
| 48 | Acidarmure (Acid Armor) | Poison | Statut | – |
| 52 | Hydrocanon (Hydro Pump) | Eau | Spé | 110 |

## CT, CS et tuteurs

| Groupe | Attaques |
|---|---|
| Statut et survie (CT) | Toxik, Abri, Repos, Façade, Attraction, Reflet, Mur Lumière, Protection, Rune Protect |
| Météo (CT) | Danse Pluie, Grêle |
| STAB (CT, CS) | Vibraqua, Bombe Beurk, Surf, Plongée, Cascade |
| Couverture (CT) | Laser Glace, Blizzard, Giga-Sangsue |
| Tuteurs | Vent Glace, Roulade, Boul'Armure (*Roulemboule*), Ténacité, Blabla Dodo, Ronflement, Vantardise |

Exclusions volontaires : Provoc et Cage-Éclair (pas un perturbateur) ;
Séisme, Psyko, Tonnerre, Ball'Ombre (couverture trop large) ; Ultralaser ;
coups de poing, Danse Lames, Explosion (pas de membres) ; Éclate-Roc, Force,
Coupe, Vol.
