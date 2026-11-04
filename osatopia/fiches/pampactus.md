# Famille Pampactus

> Cactus bandits des terres désertiques, qui détroussent les voyageurs en
> maniant deux sabres. *(Lore de mémoire, à vérifier : élément des sorts —
> probablement Terre — et zone des deux monstres.)*
> Évolutions : Pampactus → Cactoblongo (niv. 30).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies : `PERCENT_FEMALE(50)`, `.eggCycles = 20`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` (comme Bitouf et Scorpique) ;
groupes d'œuf `EGG_GROUP_GRASS` et `EGG_GROUP_HUMAN_LIKE` (comme Cacnea),
couleur `BODY_COLOR_GREEN`.

## Intention

Archétype : **attaquant à boost** physique, avec **priorité** en secondaire.
Cactoblongo est un duelliste : il pose Danse Lames, frappe avec des attaques
tranchantes renforcées par le talent Incisif (×1,5), et achève les adversaires
affaiblis avec Coup Bas.

Références : **Cacnea / Cacturne** (cactus Plante/Ténèbres, Voile Sable,
Absorbe-Eau, Lien du Destin, Coup Bas), **Mangriff** et **Étouraptor**
(profil d'attaquant physique rapide).

Plante/Ténèbres aux deux stades. Faiblesses : Insecte ×4, Feu, Glace, Vol,
Poison, Combat, Fée. Résistances : Eau, Électrik, Plante, Sol, Spectre,
Ténèbres ; immunité Psy.

Évolution au niveau 30, comme Scorpique, l'autre famille du désert : capture
vers les niveaux 20–25, évolution entre Adriane et Norman.

## Stades

| | Pampactus | Cactoblongo |
|---|---|---|
| Types | Plante/Ténèbres | Plante/Ténèbres |
| PV | 50 | 75 |
| Attaque | 80 | 130 |
| Défense | 45 | 70 |
| Atq. Spé | 40 | 50 |
| Déf. Spé | 35 | 55 |
| Vitesse | 55 | 85 |
| **Total** | **305** | **465** |
| Évolution | niv. 30 | – |
| Capture / Exp. | 190 / 60 | 45 / 175 |
| EV | Att +1 | Att +2 |

Stats sacrifiées : l'AtqSpé (il se bat au sabre) et la DéfSpé (bandit fragile
face aux sorts). Plus lent que Tortue Bleue et Raul Mops, mais 130 en Attaque.

Comparaisons (outil `similaires`) :
- Pampactus : Carabing (315), Flambino (310), Grillepattes (305) ; côté
  Osatopia, Raphaela (310) et Dagon (285).
- Cactoblongo : Étouraptor (485), Mangriff (458), Pohmarmotte (490) ; côté
  Osatopia, Tortue Bleue (480, plus rapide et plus robuste), Sarkapwane (465)
  et Raul Mops (515, beaucoup plus rapide).

## Talents

| Emplacement | Pampactus | Cactoblongo |
|---|---|---|
| 1 | Incisif (Sharpness) | Incisif (Sharpness) |
| 2 | Voile Sable (Sand Veil) | Voile Sable (Sand Veil) |
| Caché | Absorbe-Eau (Water Absorb) | Absorbe-Eau (Water Absorb) |

- Incisif : +50 % aux attaques tranchantes. Raul Mops l'a aussi, mais en
  talent caché ; ici c'est le talent principal.
- Voile Sable : esquive sous la tempête, en synergie avec Scordion (même
  désert) et Tempête de Sable dans son learnset.
- Absorbe-Eau : hérité de Cacnea.

## Kit final (Cactoblongo, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Plante | Lame Feuille (Leaf Blade) | Plante | Phys. | 90 | Tranchante, critique élevé ; niv. 40 |
| STAB Ténèbres | Vagues à Lames (Ceaseless Edge) | Ténèbres | Phys. | 65 | Tranchante, pose des Picots ; aucun autre custom |
| Boost | Danse Lames (Swords Dance) | Normal | Statut | – | +2 Att ; niv. 33 |
| Priorité | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 | Priorité +1 ; niv. 36 |

Options écartées : Lame Solaire, Encornebois (Plante) ; Tranche-Nuit,
Génusection, Sabotage (Ténèbres) ; Gonflette, Pico-Défense (boost) ; Plaie
Croix, Lame Sainte, Aéropique (couverture, présentes dans le learnset).

## Capacités custom

Aucune (« Sabres Jumeaux », Plante 2×40 tranchante, a été proposée puis
écartée).

## Learnsets

Attaques tranchantes (boostées par Incisif) marquées ✂.

### Pampactus

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 1 | Feuillage (Leafage) | Plante | Phys. | 40 |
| 4 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 7 | Taillade (Fury Cutter) ✂ | Insecte | Phys. | 40 |
| 10 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 13 | Tranch'Herbe (Razor Leaf) ✂ | Plante | Phys. | 55 |
| 16 | Représailles (Payback) | Ténèbres | Phys. | 50 |
| 19 | Aéropique (Aerial Ace) ✂ | Vol | Phys. | 60 |
| 22 | Tempête de Sable (Sandstorm) | Roche | Statut | – |
| 25 | Vagues à Lames (Ceaseless Edge) ✂ | Ténèbres | Phys. | 65 |
| 28 | Sabotage (Knock Off) | Ténèbres | Phys. | 65 |
| 33 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 36 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 |
| 39 | Plaie Croix (X-Scissor) ✂ | Insecte | Phys. | 80 |
| 42 | Lame Feuille (Leaf Blade) ✂ | Plante | Phys. | 90 |
| 46 | Lien du Destin (Destiny Bond) | Spectre | Statut | – |

### Cactoblongo

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Plaie Croix (X-Scissor) ✂ | Insecte | Phys. | 80 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 1 | Feuillage (Leafage) | Plante | Phys. | 40 |
| 4 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 7 | Taillade (Fury Cutter) ✂ | Insecte | Phys. | 40 |
| 10 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 13 | Tranch'Herbe (Razor Leaf) ✂ | Plante | Phys. | 55 |
| 16 | Représailles (Payback) | Ténèbres | Phys. | 50 |
| 19 | Aéropique (Aerial Ace) ✂ | Vol | Phys. | 60 |
| 22 | Tempête de Sable (Sandstorm) | Roche | Statut | – |
| 25 | Vagues à Lames (Ceaseless Edge) ✂ | Ténèbres | Phys. | 65 |
| 28 | Sabotage (Knock Off) | Ténèbres | Phys. | 65 |
| 33 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 36 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 |
| 40 | Lame Feuille (Leaf Blade) ✂ | Plante | Phys. | 90 |
| 44 | Lame Sainte (Sacred Sword) ✂ | Combat | Phys. | 90 |
| 48 | Lien du Destin (Destiny Bond) | Spectre | Statut | – |
| 52 | Lame Solaire (Solar Blade) ✂ | Plante | Phys. | 125 |

Temporisation (`P_PRE_EVO_MOVES` à `FALSE`) : Plaie Croix arrive à
l'évolution (les deux sabres croisés) au lieu du niveau 39 ; Lame Sainte et
Lame Solaire n'existent que chez Cactoblongo, qui obtient aussi Lame Feuille
deux niveaux plus tôt. Rien à 90 ou plus avant le niveau 40.

## CT, CS et tuteurs

| Attaque | Pampactus | Cactoblongo |
|---|---|---|
| Abri, Toxik, Repos, Façade, Attraction, Reflet | ✓ | ✓ |
| Zénith (pour Lame Solaire), Tempête de Sable | ✓ | ✓ |
| Balle Graine, Giga-Sangsue | ✓ | ✓ |
| Larcin, Provoc, Tourmente | ✓ | ✓ |
| Aéropique, Casse-Brique, Tunnel, Tomberoche | ✓ | ✓ |
| Coupe, Force, Éclate-Roc (CS) | ✓ | ✓ |
| Taillade, Éboulement, Riposte (tuteurs) | ✓ | ✓ |
| Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✓ | ✓ |
| Ultralaser | – | ✓ |

Exclusions volontaires :
- **Danse Lames** (tuteur) et **Gonflette** (CT) : casseraient l'arrivée du
  boost au niveau 33.
- **Mitra-Poing, Dynamo-Poing, Poing Éclair, Ultimapoing** : il se bat au
  sabre, pas aux poings (contrairement à Cacturne).
- **Séisme** : trop fort, hors thème.
- **Lance-Soleil, Ball'Ombre, Météores** : attaques spéciales, AtqSpé 50.
