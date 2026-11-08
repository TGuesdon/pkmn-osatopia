# Famille Kaniglou

> Loup humanoïde vorace de la Forêt des Pins Perdus, sur l'île glacée de
> Frigost. Dans Dofus, ses sorts *Glouglou* (frappe plus fort quand il lui
> manque des PV), *Kaniglouton* (attire et applique Érosion) et *Frigogol*
> (+40 % de critique) en font un prédateur qui mise sur le coup critique.
> Évolutions : Kanigloups → Kaniglou (niv. 34).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Réutilise le talent custom **Rage Fauve** (créé pour
Chacha). Pas de capacité custom.

Famille miroir de [Glouragan](glouragan.md) : même total et même niveau
d'évolution, mais un profil inversé (rapide et offensif contre robuste et lent).

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_FIELD` ; couleur `BODY_COLOR_WHITE`.

À vérifier : **Kanigloups** (le premier stade) n'existe pas dans DofusDB.
C'est un bébé propre à Osatopia.

## Intention

Archétype : **attaquant à boost / critique** · Références : Dimoret (rapide,
physique, Glace), Lougaroc (loup qui frappe vite) · Pourquoi : le loup glouton
de Frigost qui s'aiguise (*Frigogol*), frappe plus fort quand il est blessé
(*Glouglou*) et dévore sa Baie avant les autres (*Kaniglouton*).

Type **Glace pur** sur les deux stades (choix de l'utilisateur : pas de double
type).

## Stades

| | Kanigloups | Kaniglou |
|---|---|---|
| Constante | `SPECIES_KANIGLOUPS` | `SPECIES_KANIGLOU` |
| Types | Glace | Glace |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 60 / 75 / 50 / 35 / 48 / 62 | 85 / 120 / 66 / 50 / 71 / 108 |
| Total | 330 | 500 |
| Évolution | niv. 34 | – |
| Talents | Gloutonnerie / Chasse-Neige / *Rage Fauve* | idem |
| Capture / Exp. | 120 / 66 | 60 / 178 |
| EV | Att +1 | Att +2 |

Stats sacrifiées : l'AtqSpé (attaquant physique) et les défenses. La Vitesse a
été baissée de 22 points par rapport à la première proposition (130), au
profit des PV, de la Déf et de la DéfSpé.

Comparaisons (outil `similaires`) : Dimoret (510), Farfurex (510) ; customs
Corbomaître (Vol/Ténèbres), Kwak Vent (Vol), Raul Mops (Eau/Ténèbres). Aucun
n'est de type Glace.

## Talents

| Emplacement | Talent |
|---|---|
| 1 | **Gloutonnerie** (Gluttony) : mange sa Baie dès la moitié de ses PV. Avec une Baie Lansat (+critique), on retrouve *Frigogol*. |
| 2 | **Chasse-Neige** (Slush Rush) : Vitesse ×2 sous la neige. |
| Caché | **Rage Fauve** (`ABILITY_RAGE_FAUVE`, custom) : copie de Courroupace sans la carapace. Sous la moitié des PV : Att, AtqSpé et Vit +1, Déf et DéfSpé −1. Va bien avec Contre. |

## Kit final

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB fort | **Chute Glace** (85, peut apeurer) | Bise Glaciaire, Cryo-Pirouette, Crocs Givre |
| Boost (*Frigogol*) | **Puissance** (taux de critique +2) | Aiguisage, Danse Lames |
| *Glouglou* | **Contre** (plus fort avec peu de PV) | Gigotage |
| Couverture | **Tranche-Nuit** (critique élevé) | Éclats Glace, Lame de Roc, Mâchouille |

## Capacités custom

Aucune.

## Learnsets

### Kanigloups

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Poudreuse (Powder Snow) | Glace | Spé | 40 |
| 1 | Grimace (Scary Face) | Normal | Statut | – |
| 4 | Éclats Glace (Ice Shard) | Glace | Phy | 40, prio +1 |
| 8 | Morsure (Bite) | Ténèbres | Phy | 60 |
| 12 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 16 | Crocs Givre (Ice Fang) | Glace | Phy | 65 |
| 20 | Tranche-Nuit (Night Slash) | Ténèbres | Phy | 70 |
| 24 | Coup Bas (Sucker Punch) | Ténèbres | Phy | 70, prio +1 |
| 28 | Mâchouille (Crunch) | Ténèbres | Phy | 80 |
| 32 | Puissance (Focus Energy) | Normal | Statut | – |

### Kaniglou

Reprend toutes les attaques de Kanigloups aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Chute Glace (Icicle Crash) | Glace | Phy | 85 |
| 38 | Contre (Reversal) | Combat | Phy | var. |
| 42 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 46 | Lame de Roc (Stone Edge) | Roche | Phy | 100 |
| 52 | Bise Glaciaire (Mountain Gale) | Glace | Phy | 100 |

## CT, CS et tuteurs

| Attaque | Kanigloups | Kaniglou |
|---|---|---|
| Toxik, Grêle, Abri, Repos, Attraction, Façade, Reflet, Laser Glace | ✓ | ✓ |
| Éclate-Roc, Force, Coupe (CS) | ✓ | ✓ |
| Tunnel, Casse-Brique, Aéropique, Queue de Fer, Larcin, Tourmente, Provoc, Hurlement | ✓ | ✓ |
| Ténacité, Ronflement, Blabla Dodo, Vantardise, Vent Glace (tuteurs) | ✓ | ✓ |
| Ultralaser | – | ✓ |

Exclusions volontaires :
- Séisme et Gonflette : réservés à l'identité de Glouragan.
- Les coups de poing : on garde l'identité griffes et crocs.
- Le tuteur Danse Lames, pour qu'il arrive au niveau 42 et pas avant.
- Blizzard : la famille est physique.
