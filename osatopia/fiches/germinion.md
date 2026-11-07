# Famille Germinion

> Créatures de la Gangrène, la corruption démoniaque : le Germinion en est le
> germe, le Gangredogue le molosse corrompu adulte. *(Lore de mémoire, à
> vérifier : éléments des sorts et zone.)*
> Évolutions : Germinion → Gangredogue (niv. 36).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies : `PERCENT_FEMALE(50)`, `.eggCycles = 15`,
`STANDARD_FRIENDSHIP` (famille Bitouf) ; `GROWTH_SLOW` (comme Dracochon) ;
groupes d'œuf `EGG_GROUP_DRAGON` + `EGG_GROUP_AMORPHOUS` ; couleur
`BODY_COLOR_PURPLE`.

## Intention

Archétype : **démolisseur spécial** (+ statut / poison) · Références :
Kravarech (Dragon/Poison, Draco-Choc + Bombe Beurk, Adaptabilité), Mandrillon
(Dragon/Poison spécial, Machination, Choc Venin), Trioxhydre (bête monstrueuse
spéciale) · Pourquoi : une bête de corruption qui frappe fort sans être rapide
et répand le poison grave partout grâce à Chaîne Toxique.

Premier Dragon/Poison d'Osatopia (seul Dracochon est Dragon). Se distingue de
Morfrelon (Poison spécial rapide et fragile) et de Dieubouftou (spécial lent
et défensif).

## Stades

| | Germinion | Gangredogue |
|---|---|---|
| Constante | `SPECIES_GERMINION` | `SPECIES_GANGREDOGUE` |
| Types | Dragon/Poison | Dragon/Poison |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 65 / 45 / 55 / 80 / 55 / 40 | 90 / 65 / 75 / 115 / 80 / 70 |
| Total | 340 | 495 |
| Évolution | niv. 36 | – |
| Talents | Chaîne Toxique / Pression / *Adaptabilité* | idem |
| Capture / Exp. | 120 / 72 | 45 / 225 |
| EV | AtqSpé +1 | AtqSpé +2, PV +1 |

Stats sacrifiées : l'Attaque (spécial pur) et une partie de la Vitesse
(démolisseur lourd, pas nettoyeur).

Comparaisons (`similaires`) : Kravarech 494, Rafflesia 490 ; custom
Dieubouftou 495, Morfrelon 485.

## Talents

| Emplacement | Talent |
|---|---|
| 1 | **Chaîne Toxique** (Toxic Chain) : 30 % de poison grave sur chaque attaque, cœur du thème |
| 2 | Pression (Pressure) |
| Caché | Adaptabilité (Adaptability) |

Écartés : Corrosion (Mouchame), Cruauté (Ouroboulos), Toxitouche (contact
seulement, inadapté à un attaquant spécial).

## Kit final (niv. 40–50)

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB Dragon | **Draco-Choc** (Dragon Pulse) Spé 85 | Draco-Météore 130, Laser Hasard 80 |
| STAB Poison | **Chaîne Malsaine** (Malignant Chain) Spé 100, 50 % poison grave | Cradovague 95, Bombe Beurk 90, Choc Venin 65 |
| Boost | **Dracacophonie** (Clangorous Soul) +1 partout contre 33 % PV | Machination, Piège de Venin |
| Couverture | **Telluriforce** (Earth Power) Sol Spé 90 : Acier, Poison | Vibrobscur, Lance-Flammes, Ball'Ombre |

Synergies : Chaîne Toxique empoisonne → Choc Venin double, Piège de Venin
affaiblit la cible empoisonnée.

## Capacités custom

Aucune. Piste écartée pour l'instant : **Gangrène** (Dragon, Spé, 80, 100 %,
15 PP, 30 % de poison), variante de Draco-Souffle (`EFFECT_HIT` + effet
secondaire poison), difficulté facile.

## Learnsets

### Germinion

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Purédpois (Smog) | Poison | Spé | 30 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Ouragan (Twister) | Dragon | Spé | 40 |
| 9 | Grimace (Scary Face) | Normal | Statut | – |
| 12 | Draco-Souffle (Dragon Breath) | Dragon | Spé | 60 |
| 16 | Choc Venin (Venoshock) | Poison | Spé | 65 |
| 20 | Pics Toxik (Toxic Spikes) | Poison | Statut | – |
| 24 | Boue-Bombe (Mud Bomb) | Sol | Spé | 65 |
| 28 | Vibrobscur (Dark Pulse) | Ténèbres | Spé | 80 |
| 32 | Piège de Venin (Venom Drench) | Poison | Statut | – |
| 36 | Draco-Choc (Dragon Pulse) | Dragon | Spé | 85 |
| 41 | Cradovague (Sludge Wave) | Poison | Spé | 95 |
| 46 | Machination (Nasty Plot) | Ténèbres | Statut | – |

Cradovague et Machination récompensent un Germinion qu'on ne fait pas évoluer.

### Gangredogue

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Draco-Choc (Dragon Pulse) | Dragon | Spé | 85 |
| 1–32 | Mêmes attaques que Germinion | | | |
| 40 | Telluriforce (Earth Power) | Sol | Spé | 90 |
| 44 | Chaîne Malsaine (Malignant Chain) | Poison | Spé | 100 |
| 48 | Dracacophonie (Clangorous Soul) | Dragon | Statut | – |
| 54 | Draco-Météore (Draco Meteor) | Dragon | Spé | 130 |

## CT, CS et tuteurs

| Attaque | Germinion | Gangredogue |
|---|---|---|
| Toxik, Bombe Beurk, Abri, Repos, Ronflement, Blabla Dodo, Façade, Attraction, Reflet, Ténacité, Vantardise, Provoc, Tourmente, Larcin | ✓ | ✓ |
| Ball'Ombre, Lance-Flammes, Giga-Sangsue, Coud'Boue, Hurlement, Draco-Griffe | ✓ | ✓ |
| Déflagration, Ultralaser, Surf | – | ✓ |

Exclusions volontaires : Laser Glace, Blizzard, Tonnerre, Psyko (hors thème),
Plénitude (garder Dracacophonie / Machination comme boosts), Séisme
(démolisseur spécial ; Telluriforce reste la récompense du niv. 40), coups de
poing.
