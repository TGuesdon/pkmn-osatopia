# Famille Bourgeon

> Plantes parasites animées des forêts denses autour de Cimetronelle. Elles
> s'enracinent, piègent leurs proies dans leurs lianes et se nourrissent de
> leur sève. *(Lore à vérifier : sorts sans doute Terre.)*
> Évolutions : Bourgeon → Bulbisauge (niv. 33).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises des familles proches : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` (comme
Folle / Bloqueuse), groupe d'œuf `EGG_GROUP_GRASS`, couleur
`BODY_COLOR_GREEN`.

## Intention

Archétype : **tank spécial drainant**, avec une pointe de **statut / stall**.
Bulbisauge encaisse, endort ou paralyse, puis use l'adversaire en drainant.
Plante pure : rien dans son physique n'appelle Spectre. Le cimetière n'est
rappelé que par Châtiment et Ball'Ombre.

Références :
- **Ortide** (Gloom, 395) : lent et assez robuste, avec poudres et drains.
- **Gaulet** (Amoonguss, 464) : le parasite qui encaisse, avec Régé-Force.
- **Bouldeneu** (Tangrowth, 535) : plante pure à lianes, avec Régé-Force.

Deux façons de le jouer, selon le talent :
- **enraciné** (Créa-Herbe ou Feuille Garde) : il entre, le champ herbu se
  pose, il s'enracine avec Racines et ne bouge plus ;
- **pivot parasite** (Régé-Force) : il pose Vampigraine ou une poudre, puis
  sort du combat pour récupérer. Racines bloque la sortie : à éviter dans
  cette variante.

Se distingue de la Bloqueuse (Plante/Psy, mur spécial rapide) par plus
d'AtqSpé et de Défense, et 40 de Vitesse en moins. Se distingue de Champagnon
(Plante/Poison) parce que tout son kit est spécial. Champ Herbu est déjà
appris par les familles Abraknyde et Folle : il ne l'a qu'en talent.

## Stades

| | Bourgeon | Bulbisauge |
|---|---|---|
| Types | Plante | Plante |
| PV | 60 | 105 |
| Attaque | 35 | 55 |
| Défense | 55 | 95 |
| Atq. Spé | 60 | 95 |
| Déf. Spé | 55 | 80 |
| Vitesse | 25 | 30 |
| **Total** | **290** | **460** |
| Évolution | niv. 33 | – |
| Capture / Exp. | 190 / 60 | 75 / 165 |
| EV | PV +1 | PV +1, Atq. Spé +1 |

Stats sacrifiées : la Vitesse (il est enraciné, il encaisse avant de
frapper) et l'Attaque (tout son kit est spécial).

Comparaisons (outil `similaires`) :
- Bourgeon : Obalie (290), Chlorobule (280) ; côté Osatopia, Tigrimas (295)
  et Champchamp (285), profils différents.
- Bulbisauge : Mushana (487), Cocotine (462) ; côté Osatopia, Ronronchon
  (Psy/Fée, 480, plus d'AtqSpé et de Vitesse, moins de Défense) et
  Champagnon (455, physique).

## Talents

| Emplacement | Bourgeon | Bulbisauge |
|---|---|---|
| 1 | Régé-Force (Regenerator) | Régé-Force (Regenerator) |
| 2 | Feuille Garde (Leaf Guard) | Feuille Garde (Leaf Guard) |
| Caché | Créa-Herbe (Grassy Surge) | Créa-Herbe (Grassy Surge) |

- Régé-Force : variante pivot. Aucun monstre custom ne l'a.
- Feuille Garde : protège du statut au soleil. Préférée à Chlorophylle, déjà
  chez 3 monstres custom.
- Créa-Herbe : variante enracinée. Le champ herbu soigne 1/16 des PV par
  tour, renforce Giga-Sangsue et réduit les dégâts de Séisme.

## Kit final (Bulbisauge, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB qui draine | Giga-Sangsue (Giga Drain) | Plante | Spé. | 75 | Rend 50 % des dégâts |
| Soin, tenue | Racines (Ingrain) ou Vole-Force (Strength Sap) | Plante | Statut | – | Racines pour la variante enracinée, Vole-Force sinon |
| Statut | Poudre Dodo (Sleep Powder) | Plante | Statut | – | Prépare Châtiment |
| Couverture | Châtiment (Hex) | Spectre | Spé. | 65 (130) | Puissance doublée si la cible a un statut |

Alternatives dans le learnset ou en CT : Vampigraine, Para-Spore, Synthèse,
Cotogarde, Éco-Sphère, Tempête Verte, Bombe Beurk, Ball'Ombre, Dévorêve,
Toxik.

## Capacités custom

Aucune. Mortier Matcha (Matcha Gotcha) a été envisagé, puis écarté.

## Learnsets

### Bourgeon

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Vole-Vie (Absorb) | Plante | Spé. | 20 |
| 1 | Doux Parfum (Sweet Scent) | Normal | Statut | – |
| 5 | Étreinte (Bind) | Normal | Phys. | 15 |
| 8 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 12 | Méga-Sangsue (Mega Drain) | Plante | Spé. | 40 |
| 15 | Racines (Ingrain) | Plante | Statut | – |
| 18 | Poudre Dodo (Sleep Powder) | Plante | Statut | – |
| 21 | Feuille Magik (Magical Leaf) | Plante | Spé. | 60 |
| 24 | Para-Spore (Stun Spore) | Plante | Statut | – |
| 27 | Giga-Sangsue (Giga Drain) | Plante | Spé. | 75 |
| 33 | Châtiment (Hex) | Spectre | Spé. | 65 |
| 39 | Synthèse (Synthesis) | Plante | Statut | – |

### Bulbisauge

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Vole-Force (Strength Sap) | Plante | Statut | – |
| 1 | Vole-Vie (Absorb) | Plante | Spé. | 20 |
| 1 | Doux Parfum (Sweet Scent) | Normal | Statut | – |
| 5 | Étreinte (Bind) | Normal | Phys. | 15 |
| 8 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 12 | Méga-Sangsue (Mega Drain) | Plante | Spé. | 40 |
| 15 | Racines (Ingrain) | Plante | Statut | – |
| 18 | Poudre Dodo (Sleep Powder) | Plante | Statut | – |
| 21 | Feuille Magik (Magical Leaf) | Plante | Spé. | 60 |
| 24 | Para-Spore (Stun Spore) | Plante | Statut | – |
| 27 | Giga-Sangsue (Giga Drain) | Plante | Spé. | 75 |
| 33 | Châtiment (Hex) | Spectre | Spé. | 65 |
| 39 | Synthèse (Synthesis) | Plante | Statut | – |
| 42 | Cotogarde (Cotton Guard) | Plante | Statut | – |
| 46 | Éco-Sphère (Energy Ball) | Plante | Spé. | 90 |
| 50 | Tempête Verte (Leaf Storm) | Plante | Spé. | 130 |

Rien à 90+ avant le niveau 46. Châtiment (130 sur une cible sous statut)
arrive après Norman. Temporisation : Bourgeon n'aura jamais Vole-Force, qui
marque l'évolution. Recoupements avec les custom limités à Racines (famille
Pousse, Champchamp), Para-Spore et Giga-Sangsue.

## CT, CS et tuteurs

| | Bourgeon | Bulbisauge |
|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet (CT) | ✅ | ✅ |
| Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✅ | ✅ |
| Giga-Sangsue, Lance-Soleil, Zénith, Rune Protect (CT) | ✅ | ✅ |
| Coupe (CS) : ses lianes | ✅ | ✅ |
| Bombe Beurk (CT) : le côté parasite | ✅ | ✅ |
| Ball'Ombre (CT) : Cimetronelle | ✅ | ✅ |
| Mur Lumière, Protection (CT) : rôle de tank de soutien | ✅ | ✅ |
| Dévorêve (tuteur) : il endort puis dévore la cible | ✅ | ✅ |

Exclus volontairement :
- Danse Lames, Balle Graine, Plaquage, Séisme, Tunnel : physiques, inutiles
  avec 55 en Attaque ;
- Ultralaser : un tank ne doit pas rester bloqué un tour à recharger ;
- Explosion : contraire au thème de la régénération ;
- Force, Éclate-Roc et tous les coups de poing : pas de bras ;
- inutilisables : Flash, Saisie, Retour, Frustration, Puissance Cachée,
  Force Cachée.
