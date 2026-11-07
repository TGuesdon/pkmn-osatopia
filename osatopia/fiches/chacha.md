# Famille Chacha

> Félin sauvage de la jungle. Le Chacha, petit chat colérique, devient le
> Chagouar, un jaguar qui s'enrage quand il est blessé. *(Lore de mémoire, à
> vérifier : éléments des sorts et zone.)*
> Évolutions : Chacha → Chagouar (niv. 25).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Nouveau talent **Rage Fauve**. Pas de capacité
custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_FIELD` ; couleur `BODY_COLOR_YELLOW`.

## Intention

Archétype : **démolisseur enragé** · Référence : Mangriff (félin Normal
physique, griffes, Close Combat/Danse Lames) · Pourquoi : un monstre de milieu
de partie qui frappe très fort et devient dangereux une fois blessé.

Le profil de Mangriff tel quel doublerait Leolhyène (Ténèbres, 455, Att 105 /
Vit 105, Colérique). Chagouar s'en distingue par une Vitesse plus basse, plus
de PV et d'Attaque, et une colère qui monte avec les dégâts reçus (Rage
Fauve) plutôt qu'avec les K.O. ou les critiques.

## Stades

| | Chacha | Chagouar |
|---|---|---|
| Constante | `SPECIES_CHACHA` | `SPECIES_CHAGOUAR` |
| Types | Normal | Normal |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 55 / 75 / 50 / 30 / 40 / 60 | 90 / 125 / 75 / 40 / 65 / 80 |
| Total | 310 | 475 |
| Évolution | niv. 25 | – |
| Talents | Rage Fauve / Cran / *Griffe Dure* | idem |
| Capture / Exp. | 120 / 62 | 60 / 175 |
| EV | Att +1 | Att +2 |

Stats sacrifiées : l'AtqSpé (attaquant physique) et la Vitesse, que Rage Fauve
compense une fois sous la moitié des PV.

Comparaisons (outil `similaires`) :
- Chagouar : Karaclée (465), Quartermac (490), Étouraptor (485) ; customs
  Cactoblongo (465, Plante/Ténèbres, plus rapide et plus fragile), Milirat
  (440, Normal/Ténèbres, moins offensif).
- Chacha : Carabing (315), Ouistempo (310) ; customs Raphaela, Pampactus.

## Talents

| Emplacement | Chacha / Chagouar |
|---|---|
| 1 | **Rage Fauve** (`ABILITY_RAGE_FAUVE`, custom) |
| 2 | Cran (Guts) |
| Caché | Griffe Dure (Tough Claws) |

- **Rage Fauve** : copie exacte de Courroupace (Anger Shell), renommée pour un
  jaguar qui n'a pas de carapace. Quand une attaque le fait passer sous la
  moitié de ses PV : Déf et DéfSpé −1, Att, AtqSpé et Vit +1. Description en
  jeu : « Enrage à la moitié de ses PV. »
  Intégration : constante dans `include/constants/abilities.h` (section
  Osatopia), entrée dans `src/data/abilities.h`, `case` ajouté à côté de
  `ABILITY_ANGER_SHELL` dans `src/battle_util.c` (même script
  `BattleScript_AngerShellActivates`). Difficulté : facile.
- Cran : Att ×1,5 sous altération de statut, le fauve qu'on énerve.
- Griffe Dure : attaques directes ×1,3, aucun autre custom ne l'a.

## Kit final (niv. 40–50)

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB fort « rage » | **Mania** (Thrash) Normal · Phys · 120 | Damoclès 120, Taurogne 90, Plaquage 85 |
| STAB fiable / griffes | **Éclate Griffe** (Crush Claw) Normal · Phys · 75 | Façade, Vengeance, Gigotage |
| Couverture | **Plaie Croix** (X-Scissor) Insecte · Phys · 80 | Cent Rancunes, Griffe Ombre, Casse-Brique (CT) |
| Boost | **Gonflette** (Bulk Up) | Grondement, Cognobidon, Ténacité |

Mécanique clé : Rage Fauve + Cent Rancunes (puissance doublée si ses stats
ont baissé pendant le tour, ce qui arrive quand Rage Fauve se déclenche) et
Ténacité + Gigotage en fin de learnset.

## Capacités custom

Aucune.

## Learnsets

### Chacha

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Griffe (Scratch) | Normal | Phys | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Vive-Attaque (Quick Attack) | Normal | Phys | 40, prio +1 |
| 9 | Combo-Griffe (Fury Swipes) | Normal | Phys | 18 ×2–5 |
| 12 | Morsure (Bite) | Ténèbres | Phys | 60 |
| 15 | Grondement (Howl) | Normal | Statut | – |
| 18 | Taillade (Fury Cutter) | Insecte | Phys | 40 |
| 21 | Tranche (Slash) | Normal | Phys | 70 |
| 24 | Éclate Griffe (Crush Claw) | Normal | Phys | 75 |
| 29 | Vengeance (Retaliate) | Normal | Phys | 70 |
| 34 | Gonflette (Bulk Up) | Combat | Statut | – |
| 38 | Mania (Thrash) | Normal | Phys | 120 |

### Chagouar

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Cent Rancunes (Lash Out) | Ténèbres | Phys | 75 |
| 1–24 | comme Chacha | | | |
| 28 | Vengeance (Retaliate) | Normal | Phys | 70 |
| 32 | Gonflette (Bulk Up) | Combat | Statut | – |
| 36 | Plaie Croix (X-Scissor) | Insecte | Phys | 80 |
| 40 | Mania (Thrash) | Normal | Phys | 120 |
| 44 | Ténacité (Endure) | Normal | Statut | – |
| 48 | Gigotage (Flail) | Normal | Phys | variable |
| 52 | Damoclès (Double-Edge) | Normal | Phys | 120 |

Retarder l'évolution donne Mania 2 niveaux plus tôt (38 au lieu de 40).

## CT, CS et tuteurs

| Attaque | Chacha | Chagouar |
|---|---|---|
| Abri, Repos, Blabla Dodo, Ronflement, Toxik, Attraction, Vantardise, Reflet | ✓ | ✓ |
| Façade, Larcin, Ténacité, Plaquage | ✓ | ✓ |
| Coupe, Force, Éclate-Roc | ✓ | ✓ |
| Casse-Brique, Aéropique, Tunnel, Queue de Fer | ✓ | ✓ |
| Riposte, Hurlement, Tourmente | ✓ | ✓ |
| Ultralaser | – | ✓ |

Exclusions volontaires :
- Gonflette (CT) : garde son apprentissage aux niv. 32–34.
- Damoclès (tuteur) : reste la récompense du niv. 52.
- Éboulement, Tomberoche, Séisme : n'ont pas de sens pour ce monstre.
- Danse Lames : niche de Leolhyène.
- Poings élémentaires, Ultimapoing, Ultimawashi : c'est un félin.
