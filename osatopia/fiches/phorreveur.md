# Famille Phorreveur

> Taupes chercheuses d'or du monde de Dofus (lore **à vérifier** : élément
> des sorts et zone exacts). Trois stades — Évolutions : Phorreveur →
> (niv. 18) Metaphorreur → (niv. 36) Phossile.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`, `moves_info.h`, `include/constants/moves.h`).
Aucun code de combat : Filon d'Or réutilise `EFFECT_HIT` et
`MOVE_EFFECT_PAYDAY`.

Constantes : `SPECIES_PHORREVEUR`, `SPECIES_METAPHORREUR`,
`SPECIES_PHOSSILE`. Les trois existent en placeholder dans
`src/data/pokemon/species_info.h` (Plante, 10 partout).

Valeurs non choisies, reprises de la famille Bitouf et de Sanglier :
`PERCENT_FEMALE(50)`, `.eggCycles = 15`, `STANDARD_FRIENDSHIP`,
`GROWTH_MEDIUM_SLOW`, groupe d'œuf `EGG_GROUP_FIELD`, couleur
`BODY_COLOR_BROWN` (à ajuster selon le sprite).

## Intention

Archétype : **tank offensif physique** (Sol pur). Il encaisse, boost avec
Danse Lames, puis frappe fort. Côté lore, des attaques d'argent
(Jackpot, Filon d'Or) et un talent caché de ramasseur.

Références : **Minotaupe** (Excadrill) pour le kit de fouisseur (Tunnel,
Tunnelier, Éboulement, Danse Lames, Séisme), **Mastouffe** (500) pour le
profil de tank offensif équilibré, **Sablaireau** pour la robustesse
d'un Sol physique. Se distingue de Kwak Terre (Sol/Vol, plus rapide) par sa
Vitesse de 70, ses PV et sa Défense de 100, et l'absence de Vol.

Placement : famille « commune » de 3 stades, totaux 255 / 375 / 500.

## Stades

| | Phorreveur | Metaphorreur | Phossile |
|---|---|---|---|
| Types | Sol | Sol | Sol |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 50 / 55 / 45 / 30 / 35 / 40 | 75 / 80 / 70 / 40 / 55 / 55 | 100 / 105 / 100 / 50 / 75 / 70 |
| Total | **255** | **375** | **500** |
| Talents | Force Sable / Brise Moule · caché : Ramassage | idem | idem |
| Capture / Exp. | 190 / 58 | 100 / 135 | 45 / 230 |
| EV | 1 Attaque | 1 Attaque + 1 Défense | 2 Attaque + 1 Défense |

Stats sacrifiées : l'Attaque Spéciale est très faible (monstre purement
physique) et la Défense Spéciale reste moyenne.

## Kit final

Kit conseillé de Phossile : **Séisme** (STAB), **Danse Lames** (boost),
**Éboulement** ou Lame de Roc (couverture), **Tête de Fer** (couverture
Acier). **Filon d'Or** peut remplacer Tête de Fer pour l'argent.

| Rôle | Options étudiées |
|---|---|
| STAB fort | Séisme (100), Cavalerie Lourde (95), Force Chtonienne (90), Tunnelier (80), Filon d'Or (75) |
| Boost / utilitaire | Danse Lames, Aiguisage, Tempête de Sable, Repos |
| Couverture | Éboulement (75), Lame de Roc (100), Tête de Fer (80), Éclate Griffe (75), Casse-Brique (75) |
| Thème or | Filon d'Or (custom), Jackpot (40), Étrennes |

Talents : **Force Sable** (boost Sol/Roche/Acier sous tempête de sable),
**Brise Moule**, et **Ramassage** en talent caché.

## Capacités custom

### Filon d'Or (Sol, Physique)

| Champ | Valeur |
|---|---|
| Type / catégorie | Sol / Physique |
| Puissance / précision / PP | 75 / 100 / 15 |
| Effet | Dégâts directs ; de l'argent est récupéré après le combat |
| Proche de | Jackpot (`MOVE_PAY_DAY`, Normal, 40) |
| Implémentation | `MOVE_FILON_DOR` (`MOVES_COUNT_GEN9 + 1`), `EFFECT_HIT` + `MOVE_EFFECT_PAYDAY` dans `.additionalEffects`, animation de Jackpot |
| Difficulté | **facile** : une entrée dans `moves_info.h` + une constante |

Description FR conseillée : « Lance des pépites sur l'ennemi. Permet
d'obtenir de l'argent à la fin du combat. » Le nom tient en 11 caractères.

## Learnsets

Les stades suivants reprennent les attaques du premier stade aux mêmes
niveaux. `P_PRE_EVO_MOVES` est à `FALSE` : Phossile ne réapprend pas les
attaques exclusives de Metaphorreur (Tunnel, Éclate Griffe, Filon d'Or,
Éboulement, Aiguisage), mais il les conserve s'il les a apprises avant
d'évoluer. Séisme arrive 12 niveaux après l'évolution, comme chez Gwotofu.

### Phorreveur

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Griffe (Scratch) | Normal | Phys. | 40 |
| 1 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 5 | Tourbi-Sable (Sand Tomb) | Sol | Phys. | 35 |
| 9 | Jackpot (Pay Day) | Normal | Phys. | 40 |
| 13 | Massd'Os (Bone Club) | Sol | Phys. | 65 |
| 17 | Tempête de Sable (Sandstorm) | Roche | Statut | – |

### Metaphorreur

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Tunnel (Dig) | Sol | Phys. | 80 |
| 1 | Griffe, Jet de Sable | | | |
| 5, 9, 13, 17 | Tourbi-Sable, Jackpot, Massd'Os, Tempête de Sable | | | |
| 22 | Éclate Griffe (Crush Claw) | Normal | Phys. | 75 |
| 26 | **Filon d'Or** | Sol | Phys. | 75 |
| 30 | Éboulement (Rock Slide) | Roche | Phys. | 75 |
| 33 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |

### Phossile

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Tunnelier (Drill Run) | Sol | Phys. | 80 |
| 1 | Griffe, Jet de Sable | | | |
| 5, 9, 13, 17 | Tourbi-Sable, Jackpot, Massd'Os, Tempête de Sable | | | |
| 40 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 44 | Tête de Fer (Iron Head) | Acier | Phys. | 80 |
| 48 | Séisme (Earthquake) | Sol | Phys. | 100 |
| 54 | Lame de Roc (Stone Edge) | Roche | Phys. | 100 |

## CT, CS et tuteurs

| Attaque | Source | Phorreveur | Metaphorreur | Phossile |
|---|---|---|---|---|
| Protection (Protect) | CT | ✔ | ✔ | ✔ |
| Repos (Rest) | CT | ✔ | ✔ | ✔ |
| Reflet (Double Team) | CT | ✔ | ✔ | ✔ |
| Attraction (Attract) | CT | ✔ | ✔ | ✔ |
| Façade (Facade) | CT | ✔ | ✔ | ✔ |
| Coupe (Cut) | CS | ✔ | ✔ | ✔ |
| Éclate-Roc (Rock Smash) | CS | ✔ | ✔ | ✔ |
| Force (Strength) | CS | ✔ | ✔ | ✔ |
| Vol (Thief) | CT | ✔ | ✔ | ✔ |
| Tempête de Sable (Sandstorm) | CT | ✔ | ✔ | ✔ |
| Ténacité (Endure) | tuteur | ✔ | ✔ | ✔ |
| Blabla Dodo (Sleep Talk) | tuteur | ✔ | ✔ | ✔ |
| Ronflement (Snore) | tuteur | ✔ | ✔ | ✔ |
| Coud'Boue (Mud-Slap) | tuteur | ✔ | ✔ | ✔ |
| Vantardise (Swagger) | tuteur | | ✔ | ✔ |
| Tomberoche (Rock Tomb) | CT | | ✔ | ✔ |
| Tunnel (Dig) | CT | | ✔ | ✔ |
| Casse-Brique (Brick Break) | CT | | ✔ | ✔ |
| Plaquage (Body Slam) | tuteur | | ✔ | ✔ |
| Éboulement (Rock Slide) | tuteur | | ✔ | ✔ |
| Frappe Atlas (Seismic Toss) | tuteur | | | ✔ |
| Toxik (Toxic) | CT | | | ✔ |
| Séisme (Earthquake) | CT | | | ✔ |
| Ultralaser (Hyper Beam) | CT | | | ✔ |

Exclusions volontaires :
- Coups de poing (Feu, Glace, Foudre, Dynamo-Poing) : des taupes à griffes.
- Séisme en CT pour les deux premiers stades : il casserait la
  temporisation du learnset.
- Danse Lames en tuteur, Aiguisage, Gonflette : le boost reste au niveau 40.
- Queue de Fer et Damoclès : elles feraient de l'ombre à Tête de Fer et
  Filon d'Or.
- Aéropique et Zénith : sans rapport avec une taupe.
