# Famille Craquelope

> Golems de pierre des zones rocheuses (Plaines Rocheuses, Cania), lents et
> cogneurs, aux sorts surtout Terre. Le Craqueboule est une boule de roche qui
> roule. *(Lore de mémoire, à vérifier : éléments des sorts et zone.)*
> Évolutions : Craquelope → Craqueboule (niv. 24) → Craqueleur (niv. 40).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_MINERAL` ; couleur `BODY_COLOR_BROWN`.

## Intention

Archétype : **tank offensif** (+ poseur de pièges) · Références : Gigalithe
(lenteur, robustesse, Piège de Roc), Grolem (Boul'Armure / Roulade,
Destruction / Explosion) · Pourquoi : un golem humanoïde Roche pur qui encaisse
et frappe avec ses poings.

Cameliache (Roche/Spectre, 498) occupe déjà le créneau « Roche lent et
offensif ». Craqueleur s'en distingue par plus de PV/Déf, moins de Vitesse,
le talent **Poing de Fer** et un kit de coups de poing ; pas de Gonflette ni
de Distorsion. Poing Boost, Gonflette et Danse Lames sont exclus : trop forts
sur un monstre déjà robuste et offensif.

## Stades

| | Craquelope | Craqueboule | Craqueleur |
|---|---|---|---|
| Constante | `SPECIES_CRAQUELOPE` | `SPECIES_CRAQUEBOULE` | `SPECIES_CRAQUELEUR` |
| Types | Roche | Roche | Roche |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 55 / 70 / 70 / 25 / 40 / 20 | 75 / 95 / 100 / 35 / 55 / 25 | 105 / 130 / 120 / 40 / 75 / 30 |
| Total | 280 | 385 | 500 |
| Évolution | niv. 24 | niv. 40 | – |
| Talents | Poing de Fer / Solide Roc / *Force Sable* | idem | idem |
| Capture / Exp. | 190 / 60 | 90 / 135 | 45 / 240 |
| EV | Déf +1 | Déf +2 | Att +2, Déf +1 |

Stats sacrifiées : l'AtqSpé (physique pur) et la Vitesse (il encaisse le
premier coup ; Malédiction et Marto-Poing ne lui coûtent rien).

Comparaisons (`similaires`) : Gigalithe 515, Grolem 495, Gigansel 500 ;
custom Cameliache 498.

## Talents

| Emplacement | Talent |
|---|---|
| 1 | **Poing de Fer** (Iron Fist) : aucun autre custom ne l'a |
| 2 | Solide Roc (Solid Rock) : compense ses nombreuses faiblesses |
| Caché | Force Sable (Sand Force) |

## Kit final (niv. 40–50)

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB fort | **Roc-Boulet** (Rock Wrecker) Roche · Phys · 150 | Lame de Roc 100, Éboulement 75 |
| Boost | **Malédiction** (Curse) Att+1, Déf+1, Vit−1 | Boul'Armure, Armure |
| Couverture 👊 | **Marto-Poing** (Hammer Arm) Combat · Phys · 100 | Assaut Frontal 120, Poing Feu / Glace / Éclair (tuteurs) |
| Utilitaire | **Piège de Roc** (Stealth Rock) | Explosion, Goudronnage, Tempête de Sable |

👊 = coup de poing boosté par Poing de Fer.

## Capacités custom

Aucune (Poing Roc envisagé puis écarté).

## Learnsets

### Craquelope
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Poing Comète (Comet Punch) | Normal | Phys. | 18×2-5 |
| 1 | Armure (Harden) | Normal | Statut | – |
| 6 | Jet-Pierres (Rock Throw) | Roche | Phys. | 50 |
| 9 | Éclate-Roc (Rock Smash) | Combat | Phys. | 40 |
| 13 | Tomberoche (Rock Tomb) | Roche | Phys. | 60 |
| 17 | Goudronnage (Tar Shot) | Roche | Statut | – |
| 21 | Ultimapoing (Mega Punch) | Normal | Phys. | 80 |
| 28 | Éboulement (Rock Slide) | Roche | Phys. | 75 |
| 32 | Piège de Roc (Stealth Rock) | Roche | Statut | – |

### Craqueboule
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | **Roulade** (Rollout) | Roche | Phys. | 30 |
| 1–21 | *tronc commun de Craquelope* | | | |
| 25 | **Boul'Armure** (Defense Curl) | Normal | Statut | – |
| 28 | Éboulement (Rock Slide) | Roche | Phys. | 75 |
| 32 | Piège de Roc (Stealth Rock) | Roche | Statut | – |
| 36 | **Destruction** (Self-Destruct) | Normal | Phys. | 200 |
| 44 | **Lame de Roc** (Stone Edge) | Roche | Phys. | 100 |

### Craqueleur
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | **Marto-Poing** (Hammer Arm) | Combat | Phys. | 100 |
| 1–32 | *tronc commun de Craquelope* | | | |
| 42 | **Malédiction** (Curse) | Spectre | Statut | – |
| 46 | **Assaut Frontal** (Headlong Rush) | Sol | Phys. | 120 |
| 52 | **Roc-Boulet** (Rock Wrecker) | Roche | Phys. | 150 |
| 56 | **Explosion** | Normal | Phys. | 250 |

`P_PRE_EVO_MOVES` étant à `FALSE`, Craqueleur ne réapprend pas Roulade,
Boul'Armure ni Destruction : choix Destruction (36) ou Explosion (56).

## CT, CS et tuteurs

| Attaque | Source | Craquelope | Craqueboule | Craqueleur |
|---|---|---|---|---|
| Mitra-Poing, Hurlement, Toxik, Provoc, Abri, Séisme, Tunnel, Casse-Brique, Reflet, Protection, Tempête de Sable, Tomberoche, Façade, Repos, Attraction, Larcin, Tourmente | CT | ✅ | ✅ | ✅ |
| Force, Éclate-Roc | CS | ✅ | ✅ | ✅ |
| Riposte, Boul'Armure, Roulade, Ténacité, Éboulement, Frappe Atlas, Coud'Boue, Blabla Dodo, Ronflement, Vantardise | Tuteur | ✅ | ✅ | ✅ |
| Poing Feu, Poing Glace, Poing Éclair, Dynamo-Poing | Tuteur | ✅ | ✅ | ✅ |
| Damoclès, Plaquage | Tuteur | – | ✅ | ✅ |

Exclusions volontaires : Gonflette, Danse Lames (boosts trop forts, cf. Poing
Boost), Explosion en tuteur (préserve le choix Destruction / Explosion),
Ultimapoing en tuteur (déjà au niv. 21), Ultimawashi (coup de pied), Queue de
Fer, Ailes d'Acier, CT spéciales, Danse Pluie / Zénith, CS de déplacement.
