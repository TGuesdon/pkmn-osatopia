# Famille Scorpique

> Scorpions des déserts, enfouis dans le sable, une pince pour saisir et un dard
> venimeux pour achever. *(Lore de mémoire, à vérifier : éléments des sorts —
> probablement Terre — et zone des deux monstres.)*
> Évolutions : Scorpique → Scordion (niv. 30).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies : `PERCENT_FEMALE(50)`, `.eggCycles = 20`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` (famille Bitouf) ; groupe d'œuf
`EGG_GROUP_BUG` (comme Rapion et Drascore), couleur `BODY_COLOR_BROWN`
(conservée du placeholder).

## Intention

Archétype : **tank offensif**, avec **météo (lanceur de tempête de sable)** en
secondaire. Scordion encaisse les coups physiques, déclenche la tempête (talent
Expul'Sable ou Sable Volant, ou l'attaque Tempête de Sable), se soigne avec
Amass'Sable (2/3 des PV sous la tempête) et frappe au physique.

Références : **Drascore** (profil équilibré et cuirassé de scorpion),
**Scorvol** (scorpion Sol robuste, Voile Sable) et **Hippodocus** (lanceur de
tempête, Amass'Sable).

Sol/Poison aux deux stades, comme Nidoking : le type Sol rend la famille
insensible aux dégâts de la tempête. Faiblesses : Eau, Glace, Sol, Psy.
Résistances : Poison ×4, Combat, Insecte, Roche, Fée ; immunité Électrik.

Évolution au niveau 30 : capture dans le désert vers les niveaux 20–25,
évolution entre Adriane et Norman.

## Stades

| | Scorpique | Scordion |
|---|---|---|
| Types | Sol/Poison | Sol/Poison |
| PV | 50 | 75 |
| Attaque | 65 | 100 |
| Défense | 65 | 110 |
| Atq. Spé | 25 | 40 |
| Déf. Spé | 45 | 75 |
| Vitesse | 50 | 85 |
| **Total** | **300** | **485** |
| Évolution | niv. 30 | – |
| Capture / Exp. | 120 / 66 | 45 / 180 |
| EV | Déf +1 | Att +1, Déf +1 |

Stats sacrifiées : l'AtqSpé (attaquant purement physique) et une DéfSpé
moyenne : la carapace protège des coups, pas des attaques spéciales Eau ou Psy.

Comparaisons (outil `similaires`) :
- Scorpique : Raphaela (310), Bwak Terre (310), Arakne (256).
- Scordion : Scorvol (510), Drascore (500), Tauros (490) ; côté Osatopia,
  Serpiplume (500, plus offensif) et Phossile (500, plus de PV, plus lent).

## Talents

| Emplacement | Scorpique | Scordion |
|---|---|---|
| 1 | Expul'Sable (Sand Spit) | Expul'Sable (Sand Spit) |
| 2 | Point Poison (Poison Point) | Point Poison (Poison Point) |
| Caché | Sable Volant (Sand Stream) | Sable Volant (Sand Stream) |

- Expul'Sable : la tempête se lève quand on le frappe, cohérent avec le tank.
- Point Poison : le dard empoisonne au contact.
- Sable Volant : pose la tempête dès l'entrée en combat.
- Aucun autre monstre custom n'a ces talents de sable. Force Sable est déjà
  pris (Bwak/Kwak Terre, Sherpoa, Phossile) et a été écarté.

## Kit final (Scordion, niv. 40–55)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Sol | Séisme (Earthquake) | Sol | Phys. | 100 | Niv. 46, Scordion seulement (et CT) |
| STAB Poison | Poison Croix (Cross Poison) | Poison | Phys. | 70 | Critique élevé, peut empoisonner ; à l'évolution |
| Durabilité | Amass'Sable (Shore Up) | Sol | Statut | – | Soin 1/2, 2/3 sous la tempête |
| Couverture | Plaie Croix (X-Scissor) | Insecte | Phys. | 80 | Contre les Psy |

Options écartées : Tunnelier, Cavalerie Lourde, Assaut Frontal (Sol) ;
Griffes Funestes, Direct Toxik, Détricanon (Poison) ; Tempête de Sable, Pics
Toxik, Toxik (utilitaires, présents dans le learnset ou en CT) ; Lame de Roc,
Acupression, Danse Lames (couverture et boost).

## Capacités custom

Aucune.

## Learnsets

### Scorpique

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 1 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 4 | Force Poigne (Vise Grip) | Normal | Phys. | 55 |
| 8 | Tourbi-Sable (Sand Tomb) | Sol | Phys. | 35 |
| 12 | Queue-Poison (Poison Tail) | Poison | Phys. | 50 |
| 16 | Piqûre (Bug Bite) | Insecte | Phys. | 60 |
| 20 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 24 | Trépignement (Stomping Tantrum) | Sol | Phys. | 75 |
| 28 | Pics Toxik (Toxic Spikes) | Poison | Statut | – |
| 32 | Tempête de Sable (Sandstorm) | Roche | Statut | – |
| 36 | Plaie Croix (X-Scissor) | Insecte | Phys. | 80 |
| 40 | Amass'Sable (Shore Up) | Sol | Statut | – |
| 44 | Tunnelier (Drill Run) | Sol | Phys. | 80 |

### Scordion

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Poison Croix (Cross Poison) | Poison | Phys. | 70 |
| 1 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 1 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 4 | Force Poigne (Vise Grip) | Normal | Phys. | 55 |
| 8 | Tourbi-Sable (Sand Tomb) | Sol | Phys. | 35 |
| 12 | Queue-Poison (Poison Tail) | Poison | Phys. | 50 |
| 16 | Piqûre (Bug Bite) | Insecte | Phys. | 60 |
| 20 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 24 | Trépignement (Stomping Tantrum) | Sol | Phys. | 75 |
| 28 | Pics Toxik (Toxic Spikes) | Poison | Statut | – |
| 33 | Tempête de Sable (Sandstorm) | Roche | Statut | – |
| 36 | Plaie Croix (X-Scissor) | Insecte | Phys. | 80 |
| 40 | Amass'Sable (Shore Up) | Sol | Statut | – |
| 46 | Séisme (Earthquake) | Sol | Phys. | 100 |
| 52 | Détricanon (Gunk Shot) | Poison | Phys. | 120 |

Temporisation (`P_PRE_EVO_MOVES` à `FALSE`) : Poison Croix et Séisme
n'existent que chez Scordion ; Scorpique non évolué garde Tunnelier. Rien à 90
ou plus avant le niveau 46.

## CT, CS et tuteurs

| Attaque | Scorpique | Scordion |
|---|---|---|
| Toxik, Abri, Repos, Façade, Reflet, Attraction | ✓ | ✓ |
| Larcin, Provoc, Hurlement | ✓ | ✓ |
| Tempête de Sable, Séisme, Tunnel, Tomberoche | ✓ | ✓ |
| Queue de Fer, Coupe, Force, Éclate-Roc | ✓ | ✓ |
| Éboulement, Taillade, Coud'Boue, Riposte (tuteurs) | ✓ | ✓ |
| Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✓ | ✓ |
| Ultralaser | – | ✓ |

Exclusions volontaires :
- **Danse Lames** : Aiguisage reste son seul boost (et 8 monstres custom ont
  déjà Danse Lames).
- **Bombe Beurk** : attaque spéciale, il est physique.
- **Zénith**, **Danse Pluie** : contraires à la tempête de sable.
