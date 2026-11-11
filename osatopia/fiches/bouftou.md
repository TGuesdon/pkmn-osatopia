# Famille Bouftou

> Moutons gloutons des plaines d'Astrub (Coin des Bouftous, Tainéla, Cour du
> Bouftou Royal) qui mangent tout et n'importe quoi. Sorts Neutre, Feu, Air et
> Terre : morsures, Bêlement (-PM), la charge du Chef de Guerre, puis le soin,
> la morsure vampirique et la Cuirasse Laineuse du Bouftou Royal.
> Évolutions : Boufton → Bouftou (niv. 14) → Chef de Guerre Bouftou (niv. 28)
> → Roi Bouftou (niv. 42). Seule famille à **4 stades**.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Zone : **Route 101** (Boufton niv. 2).

Constantes : `SPECIES_BOUFTON`, `SPECIES_BOUFTOU`, `SPECIES_CDG_BOUFTOU`,
`SPECIES_BOUFTOU_ROYAL`. Refonte d'une famille déjà présente (anciennes
stats 220 / 350 / 455 / 530, évolutions 15 / 30 / 48, sans CT).

Valeurs conservées de l'ancienne version : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_FAST`,
`EGG_GROUP_FIELD`, `BODY_COLOR_WHITE`.

## Intention

Archétype : **tank offensif glouton**, avec en secondaire un **monstre de
niche « mange-tout »** (baies, Stockage). Le Roi Bouftou encaisse avec ses
PV énormes, se soigne (Lait à Boire = Guérison Bouftou), mord (Croque Fort,
Crocs Feu) et peut lancer Cognobidon, que Gloutonnerie et une Baie Sitrus
sécurisent.

Références : **Tauros** pour le Chef de Guerre (rapide, offensif, la charge
de Fureur du Bouftou) et **Ronflex** pour le Roi (énorme, lent, glouton).
La Vitesse remonte au troisième stade puis retombe au Roi.

Différences avec les autres Normal custom : le **Wo Wabbit** est un mur de
soutien et le **Dieubouftou** un tank spécial Électrik. Le Bouftou reste
100 % physique, avec des crocs et des charges.

## Stades

| | Boufton | Bouftou | Chef de Guerre | Roi Bouftou |
|---|---|---|---|---|
| Types | Normal | Normal | Normal | Normal |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 55 / 45 / 45 / 25 / 35 / 35 | 75 / 62 / 60 / 30 / 55 / 48 | 85 / 92 / 75 / 35 / 65 / 78 | 145 / 100 / 95 / 40 / 90 / 50 |
| Total | 240 | 330 | 430 | 520 |
| Talents | Boule de Poils / Gloutonnerie / Herbivore (caché) | idem | idem | idem |
| Capture / Exp. | 255 / 56 | 120 / 130 | 75 / 170 | 45 / 250 |
| EV | 1 PV | 1 PV, 1 Déf | 2 Att | 3 PV |

Stats sacrifiées : l'AtqSpé (famille physique) et la Vitesse du Roi
(compensée par les PV et le soin).

Talents :
- **Boule de Poils** (Fluffy) : la laine, comme Cuirasse Laineuse.
- **Gloutonnerie** (Gluttony) : il mange tout, et fiabilise Cognobidon.
- **Herbivore** (Sap Sipper, caché) : un mouton qui broute.

## Kit final (Roi Bouftou)

| Emplacement | Options |
|---|---|
| STAB fort | **Plaquage** (85, 30 % de paralysie) · Damoclès (120, contrecoup) · Façade (70) |
| Morsure | **Croque Fort** (Ténèbres 80, empêche la fuite, comme Ralliement de Guerre) · Crocs Feu (65, morsure Feu du Bouftou) |
| Soin | **Lait à Boire** (Guérison Bouftou) · Repos · Stockage + Avale |
| Boost / couverture | **Cognobidon** · Gonflette · Séisme · Cavalerie Lourde |

Côté mange-tout : Garde-à-Joues, Stockage, Avale et Thérémonie
(Thérémonie n'est utilisée par aucun autre monstre custom).

## Capacités custom

Aucune.

## Learnsets

Les stades suivants reprennent les attaques de base aux mêmes niveaux.

### Boufton

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Physique | 40 |
| 1 | Rugissement (Growl) | Normal | Statut | – |
| 4 | Boul'Armure (Defense Curl) | Normal | Statut | – |
| 7 | Roulade (Rollout) | Roche | Physique | 30 |
| 10 | Morsure (Bite) | Ténèbres | Physique | 60 |
| 13 | Garde-à-Joues (Stuff Cheeks) | Normal | Statut | – |
| 17 | Écrasement (Stomp) | Normal | Physique | 65 |
| 21 | Stockage (Stockpile) | Normal | Statut | – |
| 21 | Avale (Swallow) | Normal | Statut | – |
| 25 | Crocs Feu (Fire Fang) | Feu | Physique | 65 |
| 29 | Plaquage (Body Slam) | Normal | Physique | 85 |
| 33 | Thérémonie (Teatime) | Normal | Statut | – |
| 38 | Damoclès (Double-Edge) | Normal | Physique | 120 |

### Bouftou

Comme le Boufton, mais Écrasement (Stomp) est appris **à l'évolution** au
lieu du niveau 17.

### Chef de Guerre Bouftou

Base du Boufton, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Bélier (Take Down) | Normal | Physique | 90 |
| 31 | Gonflette (Bulk Up) | Combat | Statut | – |
| 35 | Croque Fort (Jaw Lock) | Ténèbres | Physique | 80 |
| 46 | Mania (Thrash) | Normal | Physique | 120 |

Mania est exclusif : il récompense le joueur qui garde son Chef de Guerre
après le niveau 42.

### Roi Bouftou

Base du Boufton, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Lait à Boire (Milk Drink) | Normal | Statut | – |
| 31 | Gonflette (Bulk Up) | Combat | Statut | – |
| 35 | Croque Fort (Jaw Lock) | Ténèbres | Physique | 80 |
| 46 | Cognobidon (Belly Drum) | Normal | Statut | – |
| 51 | Cavalerie Lourde (High Horsepower) | Sol | Physique | 95 |

## CT, CS et tuteurs

| Attaque | Boufton | Bouftou | Chef de Guerre | Roi |
|---|---|---|---|---|
| Toxik, Abri, Repos, Attraction, Façade, Larcin, Gonflette, Hurlement, Tunnel, Tomberoche | ✓ | ✓ | ✓ | ✓ |
| Force, Éclate-Roc (CS) | ✓ | ✓ | ✓ | ✓ |
| Plaquage, Damoclès, Boul'Armure, Roulade, Ténacité, Blabla Dodo, Ronflement, Vantardise, Coud'Boue (tuteurs) | ✓ | ✓ | ✓ | ✓ |
| Séisme, Éboulement | | ✓ | ✓ | ✓ |
| Provoc, Riposte | | | ✓ | ✓ |

Exclusions volontaires :
- coups de poing, Casse-Brique, Ultimawashi, Frappe Atlas et Queue de Fer :
  physique de mouton ;
- Mur Lumière, Protection et Rune Protect : réservés au rôle de soutien du
  Wo Wabbit ;
- Cage Éclair : identité de la famille Skyboufton ;
- Ultralaser : attaque spéciale, inutile avec 40 d'AtqSpé.
