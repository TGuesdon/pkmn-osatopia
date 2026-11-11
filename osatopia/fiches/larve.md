# Famille Larve

> Les Larves Jaunes rampent dans les Prairies d'Astrub (niv. 15) : *Bave
> Affaiblissante* (dégâts Air, la cible subit plus de dégâts) et *Postillon
> Cautérisant* (soin Feu). La Shin Larve, boss du Donjon des Larves, ralentit
> toute la zone (*Enlisement*), invoque des larves et avale puis recrache ses
> ennemis (*Déglutition* : −3 PA, repousse de 4 cases). La Larve Champêtre
> (Champs de Cania) appartient dans Dofus à une autre race : le trio est un
> montage Osatopia.
> Évolutions : Larve → Larveux (niv. 8) → Shin Larve (niv. 15).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs conservées des entrées existantes : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_FAST`,
`EGG_GROUP_BUG`, couleurs (jaune, jaune, blanc).

## Intention

Archétype : **tank offensif**, avec **remplissage de route précoce** en
secondaire. La famille Insecte du début du jeu, qui évolue tôt et devient une
grosse larve lente, robuste, qui frappe au physique. Enroulement (+1 Att, Déf,
Précision) fiabilise Détricanon ; Endurance renforce la Défense à chaque coup.

Références : **Migalos** (Insecte/Poison physique lent), **Chrysapile** (larve
trapue et lente), **Scobolide** (Insecte/Poison qui encaisse).

Insecte/Poison aux trois stades. Combat ×0,25 : Bastien (niv. 19) est facile.
En revanche, faiblesses Feu (neutralisée par Isograisse), Vol, Psy, Roche :
un monstre fort tôt, qui s'essouffle ensuite.

## Stades

| | Larve | Larveux | Shin Larve |
|---|---|---|---|
| Constante | `SPECIES_LARVE_JAUNE` | `SPECIES_LARVE_CHAMPETRE` | `SPECIES_SHIN_LARVE` |
| Types | Insecte/Poison | Insecte/Poison | Insecte/Poison |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 50 / 52 / 45 / 20 / 35 / 38 | 70 / 72 / 63 / 25 / 50 / 40 | 100 / 97 / 82 / 28 / 78 / 30 |
| Total | 240 | 320 | 415 |
| Talents | Mue / Endurance / caché Isograisse | idem | idem |
| Évolution | niv. 8 | niv. 15 | – |
| Capture / Exp. | 255 / 52 | 120 / 125 | 45 / 210 |
| EV | Att +1 | Déf +2 | PV +1, Att +2 |

Stats sacrifiées : l'AtqSpé (purement physique) et la Vitesse, qui retombe à 30
au stade final. Total final limité à 415 (et non 430) parce qu'il est atteint
dès le niveau 15.

Comparaisons : Migalos (400), Chrysapile (400), Simularbre (410) ; côté
Osatopia, Coquelicogne (395, Roche/Spectre, plus offensif).

## Kit final (Shin Larve, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Insecte | Furie-Bond (Lunge) | Insecte | Phys. | 80 | Baisse l'Attaque de la cible |
| STAB Poison | Détricanon (Gunk Shot) | Poison | Phys. | 120 | 80 % de précision, corrigée par Enroulement |
| Boost | Enroulement (Coil) | Poison | Statut | – | +1 Att / Déf / Précision |
| Couverture | Séisme (Earthquake) | Sol | Phys. | 100 | Feu, Roche, Acier, Poison |

Alternatives dans le learnset : Bulldoboule, Direct Toxik, Acidarmure,
Projection (la *Déglutition*), Toile Gluante et Pics Toxik (l'*Enlisement*).

## Capacités custom

Aucune. Piste écartée pour l'instant : **Déglutition** (Insecte, physique,
prio −6, force le changement, `EFFECT_HIT_SWITCH_TARGET` comme Projection).

## Learnsets

`P_PRE_EVO_MOVES` est à `FALSE` : chaque stade a son tableau, les attaques de
base tombent aux mêmes niveaux.

### Larve
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Sécrétion (String Shot) | Insecte | Statut | – |
| 5 | Gaz Toxik (Poison Gas) | Poison | Statut | – |
| 8 | Bond (Pounce) | Insecte | Phys. | 50 |
| 12 | Crochet Venin (Poison Fang) | Poison | Phys. | 50 |
| 16 | Piqûre (Bug Bite) | Insecte | Phys. | 60 |
| 21 | Acidarmure (Acid Armor) | Poison | Statut | – |
| 26 | Toile Gluante (Sticky Web) | Insecte | Statut | – |

### Larveux
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Crochet Venin (Poison Fang) | Poison | Phys. | 50 |
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Sécrétion (String Shot) | Insecte | Statut | – |
| 5 | Gaz Toxik (Poison Gas) | Poison | Statut | – |
| 8 | Bond (Pounce) | Insecte | Phys. | 50 |
| 12 | Piqûre (Bug Bite) | Insecte | Phys. | 60 |
| 16 | Acidarmure (Acid Armor) | Poison | Statut | – |
| 20 | Toile Gluante (Sticky Web) | Insecte | Statut | – |
| 25 | Direct Toxik (Poison Jab) | Poison | Phys. | 80 |
| 30 | Enroulement (Coil) | Poison | Statut | – |

### Shin Larve
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Bulldoboule (Steamroller) | Insecte | Phys. | 65 |
| 1 | Crochet Venin (Poison Fang) | Poison | Phys. | 50 |
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Sécrétion (String Shot) | Insecte | Statut | – |
| 5 | Gaz Toxik (Poison Gas) | Poison | Statut | – |
| 8 | Bond (Pounce) | Insecte | Phys. | 50 |
| 19 | Acidarmure (Acid Armor) | Poison | Statut | – |
| 22 | Toile Gluante (Sticky Web) | Insecte | Statut | – |
| 26 | Direct Toxik (Poison Jab) | Poison | Phys. | 80 |
| 30 | Projection (Circle Throw) | Combat | Phys. | 60 (prio −6) |
| 33 | Furie-Bond (Lunge) | Insecte | Phys. | 80 |
| 37 | Enroulement (Coil) | Poison | Statut | – |
| 41 | Pics Toxik (Toxic Spikes) | Poison | Statut | – |
| 45 | Séisme (Earthquake) | Sol | Phys. | 100 |
| 49 | Détricanon (Gunk Shot) | Poison | Phys. | 120 |

## CT, CS et tuteurs

| Attaque | Larve | Larveux | Shin Larve |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Reflet, Attraction, Larcin (CT) | ✓ | ✓ | ✓ |
| Ronflement, Blabla Dodo, Vantardise, Ténacité (tuteurs) | ✓ | ✓ | ✓ |
| Taillade, Boul'Armure, Roulade (tuteurs) | ✓ | ✓ | ✓ |
| Tunnel, Tomberoche (CT), Éclate-Roc (CS) | | ✓ | ✓ |
| Force (CS), Plaquage, Éboulement, Damoclès (tuteurs) | | | ✓ |
| Séisme (CT) | | | ✓ |

Exclusions volontaires : Danse Lames et Gonflette (Enroulement reste le seul
boost), Bombe Beurk et Ultralaser (spéciales), Séisme avant Shin Larve, poings
et Queue de Fer (pas de membres).
