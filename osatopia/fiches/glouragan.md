# Famille Glouragan

> Ours glouton qui vit dans la Ruche des Gloursons, sur l'île glacée de
> Frigost. Dans Dofus, ses sorts *Gloursonde* (retire des PM), *Glourdavu*
> (dégâts et soins pour les alliés) et *Glours poursuite* (riposte quand il est
> frappé) en font un tank. Les autres Gloursons apportent le miel : *Miellat*,
> *Nectar* et *Pollen* chez le Meliglours.
> Évolutions : Bisouglours → Glouragan (niv. 34).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de talent ni de capacité custom.

Famille miroir de [Kaniglou](kaniglou.md) : même total et même niveau
d'évolution, mais un profil inversé (robuste et lent contre rapide et offensif).

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_FAST` (comme Teddiursa et Polarhume) ; groupe d'œuf
`EGG_GROUP_FIELD` ; couleur `BODY_COLOR_BROWN`.

À vérifier : **Bisouglours** (le premier stade) n'existe pas dans DofusDB.
C'est un bébé propre à Osatopia.

## Intention

Archétype : **tank offensif + soutien** · Références : Ursaring et Ursaking
(gros ours physique), Polagriffe (ours Glace), Apireine (ruche robuste),
Teddiursa (Cherche Miel) · Pourquoi : un gardien de ruche qui encaisse,
ralentit l'adversaire avec du sirop (*Gloursonde*), se soigne (*Nectar*) et
riposte (*Glours poursuite*). Le miel est son originalité.

Type **Glace pur** sur les deux stades (choix de l'utilisateur : pas de double
type).

## Stades

| | Bisouglours | Glouragan |
|---|---|---|
| Constante | `SPECIES_BISOUGLOURS` | `SPECIES_GLOURAGAN` |
| Types | Glace | Glace |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 70 / 65 / 55 / 40 / 52 / 48 | 108 / 95 / 93 / 60 / 84 / 60 |
| Total | 330 | 500 |
| Évolution | niv. 34 | – |
| Talents | Cherche Miel / Corps Gel / *Nectar Mielleux* | Nectar Mielleux / Corps Gel / *Cherche Miel* |
| Capture / Exp. | 120 / 66 | 60 / 178 |
| EV | PV +1 | PV +1, Déf +1 |

Stat sacrifiée : la Vitesse. Elle a été remontée de 20 points par rapport à la
première proposition (40), en baissant légèrement les PV, la Déf et la DéfSpé.

Comparaisons (outil `similaires`) : Grotadmorv, Frison ; customs Dracochon
(Normal/Dragon), Phossile (Sol), Karnhell (Vol/Spectre). Aucun n'est de type
Glace.

## Talents

| Emplacement | Bisouglours | Glouragan |
|---|---|---|
| 1 | **Cherche Miel** (Honey Gather) : trouve parfois du Miel après un combat | **Nectar Mielleux** (Supersweet Syrup) : en entrant au combat, baisse l'Esquive de l'adversaire |
| 2 | Corps Gel (Ice Body) : récupère des PV quand il neige | idem |
| Caché | Nectar Mielleux | Cherche Miel |

## Kit final

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB fort | **Marteau de Glace** (100, baisse sa propre Vit) | Poing Glace, Avalanche |
| Ralentir (*Gloursonde*) | **Bombe au Sirop** (baisse la Vit de la cible pendant 3 tours) | Piétisol, Tomberoche |
| Soin (*Nectar*) | **Paresse** (50 % des PV) | Repos |
| Couverture | **Séisme** | Marto-Poing, Riposte |

## Capacités custom

Aucune.

## Learnsets

### Bisouglours

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phy | 40 |
| 1 | Doux Parfum (Sweet Scent) | Normal | Statut | – |
| 5 | Ball'Glace (Ice Ball) | Glace | Phy | 30 |
| 9 | Bâillement (Yawn) | Normal | Statut | – |
| 13 | Piétisol (Bulldoze) | Sol | Phy | 60 |
| 17 | Avalanche | Glace | Phy | 60, prio −4 |
| 21 | Bombe au Sirop (Syrup Bomb) | Plante | Spé | 60 |
| 25 | Coup d'Boule (Headbutt) | Normal | Phy | 70 |
| 29 | Paresse (Slack Off) | Normal | Statut | – |
| 33 | Poing Glace (Ice Punch) | Glace | Phy | 75 |

### Glouragan

Reprend toutes les attaques de Bisouglours aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Marteau de Glace (Ice Hammer) | Glace | Phy | 100 |
| 38 | Riposte (Counter) | Combat | Phy | – |
| 43 | Séisme (Earthquake) | Sol | Phy | 100 |
| 48 | Gonflette (Bulk Up) | Combat | Statut | – |
| 52 | Marto-Poing (Hammer Arm) | Combat | Phy | 100 |

## CT, CS et tuteurs

| Attaque | Bisouglours | Glouragan |
|---|---|---|
| Toxik, Grêle, Abri, Repos, Attraction, Façade, Reflet, Laser Glace | ✓ | ✓ |
| Éclate-Roc, Force, Surf (CS) | ✓ | ✓ |
| Séisme, Casse-Brique, Gonflette, Tomberoche, Hurlement, Mitra-Poing | ✓ | ✓ |
| Plaquage, Éboulement, Roulade, Poing Glace, Poing Feu, Poing Éclair, Ultimapoing, Damoclès, Riposte (tuteurs) | ✓ | ✓ |
| Ténacité, Ronflement, Blabla Dodo, Vantardise, Vent Glace (tuteurs) | ✓ | ✓ |
| Ultralaser | – | ✓ |

Exclusions volontaires :
- Danse Lames et Provoc : réservés à l'identité de Kaniglou.
- Blizzard : la famille est physique.
