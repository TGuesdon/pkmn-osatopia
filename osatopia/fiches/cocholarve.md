# Famille Cocholarve

> Dans Dofus, le Dragon Cochon est le boss d'un donjon d'Amakna, entouré de ses Cochons de Farle, et le gardien du Dofus Turquoise, qui augmente les chances de coup critique (à vérifier : éléments des sorts, zone exacte). — Évolutions : Cocholarve (`SPECIES_COCHON_DE_FARLE`) → Dracochon (`SPECIES_DRAGON_COCHON`) au niveau 42.

**État** : validée et intégrée

## Intention
Archétype : tank offensif (secondaire : attaquant à boost, via Puissance) · Références : Draïeul (seul Normal/Dragon, lent et costaud), Drakkarmin (dragon physique lent et robuste) · Pourquoi : un cochon gourmand qui encaisse, dont le dragon ne se réveille qu'à l'évolution tardive du niveau 42. Le talent caché **Turquoise** rappelle le Dofus qu'il garde ; il se combine avec Tranche et Puissance.

## Stades
| | Cocholarve | Dracochon |
|---|---|---|
| Types | Normal | Normal / Dragon |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 75 / 66 / 65 / 40 / 58 / 48 | 105 / 108 / 90 / 62 / 90 / 60 |
| Total | 352 | 515 |
| Talents | Gloutonnerie (Gluttony), Colérique (Anger Point), **Turquoise** (custom, caché) | idem |
| Capture / Exp. | 120 / 72 | 45 / 225 |
| EV | PV +1 | Att +1, PV +1 |
| Groupes d'œuf | Terrestre / Dragon | Terrestre / Dragon |

Stats sacrifiées : l'AtqSpé (monstre physique, 62 laissé pour un souffle d'appoint) et la Vitesse, sans caricature (60) pour ne pas se faire doubler par tout le monde pendant l'aventure. Se distingue de Gligli (Normal/Sol, 110/110/110/35/80/65) par moins de Défense, plus de DéfSpé, et le type Dragon.

Autres champs : 50 % femelle, cycles d'œuf 15, bonheur standard (valeurs Bitouf) ; croissance **lente** (choix de l'utilisateur, comme un dragon) ; couleur rose.

## Kit final
| Rôle | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB Dragon | Draco-Marteau (Dragon Hammer) | Dragon | Phys. | 90 |
| STAB Normal, critique élevé | Tranche (Slash) | Normal | Phys. | 70 |
| Boost | Puissance (Focus Energy) | Normal | Statut | – |
| Couverture contre Acier | Séisme (Earthquake) | Sol | Phys. | 100 |

Avec Turquoise (+1) et Puissance (+2), Tranche (+1) et toutes ses attaques font un critique à coup sûr.

## Talent custom : Turquoise
- Copie de Chanceux (Super Luck) : +1 stade de taux de critique.
- Description : « Coups critiques fréquents. »
- Code : `ABILITY_TURQUOISE`, ajouté à côté de `ABILITY_SUPER_LUCK` dans le calcul des critiques (`battle_script_commands.c`), l'IA (`battle_ai_main.c`) et l'objet tenu des Pokémon sauvages (`pokemon.c`).

## Capacités custom
Aucune.

## Learnsets

### Cocholarve
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Grondement (Howl) | Normal | Statut | – |
| 5 | Coud'Boue (Mud-Slap) | Sol | Spé. | 20 |
| 9 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 13 | Garde-à-Joues (Stuff Cheeks) | Normal | Statut | – |
| 17 | Abattage (Breaking Swipe) | Dragon | Phys. | 60 |
| 21 | Tranche (Slash) | Normal | Phys. | 70 |
| 25 | Bâillement (Yawn) | Normal | Statut | – |
| 29 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 33 | Plaquage (Body Slam) | Normal | Phys. | 85 |
| 37 | Puissance (Focus Energy) | Normal | Statut | – |
| 41 | Tête de Fer (Iron Head) | Acier | Phys. | 80 |
| 47 | Damoclès (Double-Edge) | Normal | Phys. | 120 |

### Dracochon
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | **Draco-Marteau** (Dragon Hammer) | Dragon | Phys. | 90 |
| 1–41 | Mêmes attaques que Cocholarve aux mêmes niveaux | | | |
| 46 | **Séisme** (Earthquake) | Sol | Phys. | 100 |
| 50 | **Draco-Charge** (Dragon Rush) | Dragon | Phys. | 100 |
| 55 | **Charge Glaive** (Glaive Rush) | Dragon | Phys. | 120 |

Damoclès (47) est un lot de consolation pour Cocholarve si on refuse l'évolution ; Dracochon ne l'apprend pas par niveau (`P_PRE_EVO_MOVES` à `FALSE`) mais l'a par tuteur.

## CT, CS et tuteurs
| Attaque | Cocholarve | Dracochon |
|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Hurlement, Larcin, Provoc, Tunnel, Tomberoche (CT) | ✔ | ✔ |
| Force, Éclate-Roc (CS) | ✔ | ✔ |
| Plaquage, Damoclès, Éboulement, Roulade, Boul'Armure, Ténacité, Coud'Boue, Ronflement, Blabla Dodo, Vantardise (tuteurs) | ✔ | ✔ |
| Draco-Griffe (CT) | | ✔ |
| Séisme (CT) | | ✔ |
| Queue de Fer (CT) | | ✔ |
| Lance-Flammes (CT, souffle) | | ✔ |

Exclusions volontaires : Danse Lames et Gonflette (son boost reste Puissance ; Gonflette déjà chez 10 monstres custom), Direct Toxik (trop de couverture) et les coups de poing (pas de poings), Vol (trop lourd), Ultralaser (spécial), Séisme et Draco-Griffe pour Cocholarve (le dragon se réveille à l'évolution).
