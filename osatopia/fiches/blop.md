# Famille Blop

> Gelées colorées des plaines de Cania. Les Blops existent en quatre couleurs
> (Coco, Griotte, Indigo, Reinette), une par élément ; le Gloutoblop est le
> gros blop capable d'avaler un adversaire d'un coup. *(Lore de mémoire, à
> vérifier : zone, éléments des sorts, nom du sort d'engloutissement.)*
> Évolutions : Biblop → Blop (niv. 18) → Gloutoblop (niv. 36).

**État : validée et intégrée** (`species_info.h`, `moves_info.h`,
`include/constants/moves.h`, `gen_9.h`, `teachable_learnsets.h`). Capacité
custom : **Gloutage**.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`. Choisies pour
la famille : `EGG_GROUP_AMORPHOUS` (gelée), `BODY_COLOR_BLUE` (Eau).

## Intention

Archétype : **tank à PV lent** avec une mécanique « avale / stocke / relâche »
et un **OHKO** en signature.
Références : **Avaltout** (trio Stockage / Relâche / Avale, gros PV),
**Grotadmorv** (gelée physique), **Coudlangue** (profil de stats).

Dans Dofus, le Gloutoblop avale ses adversaires et les met K.O. d'un coup.
Plutôt qu'une mécanique garantie, on le traduit par un OHKO à 30 % comme
Abîme / Guillotine / Glaciation : il échoue contre une cible de niveau
supérieur et est bloqué par Fermeté (d'où Suc Digestif au niveau 40).
Eau pur, choisi par l'utilisateur malgré le nombre de monstres Eau.
Différence avec Gobglouton, qui a aussi le trio Stockage : Gobglouton se
protège puis passe la main avec Queulonage, Gloutoblop reste en jeu,
encaisse, se soigne avec Avale et tente Gloutage.

## Stades

| | Biblop | Blop | Gloutoblop |
|---|---|---|---|
| Types | Eau | Eau | Eau |
| PV | 65 | 90 | 125 |
| Attaque | 40 | 60 | 80 |
| Défense | 45 | 65 | 85 |
| Atq. Spé | 35 | 50 | 65 |
| Déf. Spé | 45 | 65 | 90 |
| Vitesse | 30 | 40 | 45 |
| **Total** | **260** | **370** | **490** |
| Talents | Poisseux / Glu / Suintement (caché) | idem | idem |
| Évolution | niv. 18 | niv. 36 | – |
| Capture / Exp. | 190 / 60 | 120 / 140 | 45 / 240 |
| EV | PV +1 | PV +2 | PV +3 |

Vitesse et Atq. Spé sacrifiées : un OHKO lent frappe après l'adversaire, il
faut donc encaisser d'abord ; le kit est physique.

Comparaison (stade final) : Avaltout 100/73/83/73/83/55 (467), Grotadmorv
105/105/75/65/100/50 (500), Coudlangue 110/85/95/80/95/50 (515) ; custom le
plus proche : Mamansot 105/55/90/95/85/55 (485, attaquant spécial).

## Kit final

| Rôle | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Signature OHKO | **Gloutage** | Eau | Phys. | OHKO |
| STAB | Aqua-Brèche (Liquidation) | Eau | Phys. | 85 |
| Boost défensif | Stockage (Stockpile) | Normal | Statut | – |
| Soin | Avale (Swallow) | Normal | Statut | – |

Alternatives : Bâillement, Repos, Plaquage, Relâche, Suc Digestif (contre
Fermeté), Aquatacle. Pas d'Hydro-Queue : il n'a pas de queue.

## Capacités custom

**Gloutage** (`MOVE_GLOUTAGE`) — Eau · Physique · OHKO · précision 30 % ·
5 PP · contact. « Avale la cible d'un coup. K.O. en un coup s'il touche. »
Attaque existante la plus proche : Abîme (Fissure), `EFFECT_OHKO`.
Difficulté : **facile** (entrée dans `moves_info.h` + constante). Animation
reprise de Mâchouille (`gBattleAnimMove_Crunch`).

## Learnsets

Les stades suivants reprennent les attaques du premier stade aux mêmes
niveaux. `P_PRE_EVO_MOVES` est à `FALSE` : Gloutoblop ne réapprend pas les
exclusives de Blop, il reçoit donc lui-même Stockage, Relâche et Avale au
niveau 1 (accessibles au Maître des Capacités et sur un Gloutoblop sauvage).

### Biblop

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Écras'Face (Pound) | Normal | Phys. | 40 |
| 1 | Boul'Armure (Defense Curl) | Normal | Statut | – |
| 4 | Pistolet à O (Water Gun) | Eau | Spé. | 40 |
| 8 | Bâillement (Yawn) | Normal | Statut | – |
| 12 | Aqua-Jet (Aqua Jet) | Eau | Phys. | 40 (prio +1) |
| 16 | Acidarmure (Acid Armor) | Poison | Statut | – |

### Blop

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Coup d'Boule (Headbutt) | Normal | Phys. | 70 |
| 1–16 | attaques de Biblop | | | |
| 22 | Stockage (Stockpile) | Normal | Statut | – |
| 22 | Relâche (Spit Up) | Normal | Spé. | var. |
| 22 | Avale (Swallow) | Normal | Statut | – |
| 26 | Plaquage (Body Slam) | Normal | Phys. | 85 |
| 30 | Aqua-Brèche (Liquidation) | Eau | Phys. | 85 |
| 33 | Repos (Rest) | Psy | Statut | – |

### Gloutoblop

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | **Gloutage** | Eau | Phys. | OHKO |
| 1 | Stockage, Relâche, Avale | Normal | | |
| 1–16 | attaques de Biblop | | | |
| 40 | Suc Digestif (Gastro Acid) | Poison | Statut | – |
| 44 | Aqua-Brèche (Liquidation) | Eau | Phys. | 85 |
| 48 | Repos (Rest) | Psy | Statut | – |
| 52 | Aquatacle (Wave Crash) | Eau | Phys. | 120 |

## CT, CS et tuteurs

| Attaque | Biblop | Blop | Gloutoblop |
|---|---|---|---|
| Toxik, Vibraqua, Danse Pluie, Abri, Repos, Attraction, Façade, Reflet, Larcin | ✓ | ✓ | ✓ |
| Surf, Plongée | ✓ | ✓ | ✓ |
| Plaquage, Boul'Armure, Ténacité, Blabla Dodo, Ronflement, Vantardise, Clonage, Coud'Boue, Roulade, Vent Glace | ✓ | ✓ | ✓ |
| Laser Glace, Cascade, Force, Éclate-Roc, Bombe Beurk, Damoclès | | ✓ | ✓ |
| Blizzard, Ultralaser, Séisme | | | ✓ |

Exclusions volontaires : coups de poing et Queue de Fer (ni bras ni queue),
Explosion, Danse Lames, Gonflette, Plénitude (pas de boost offensif : il reste
un tank), Lame d'Air / Aéropique et attaques tranchantes.
