# Famille Moskito

> Moustique agressif qui vole des PV en piquant ; le Minoskito est sa forme
> de l'île du Minotoror, d'où son nom. *(Lore de mémoire, à vérifier :
> éléments des sorts du Moskito.)*
> Évolutions : Moskito → Minoskito (niv. 20).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe
d'œuf `EGG_GROUP_BUG`, couleur `BODY_COLOR_BROWN` (inchangée).

## Intention

Archétype : **perturbateur**, avec une pointe de **statut**. Minoskito agit
presque toujours en premier : il empoisonne, vole des PV, empêche l'adversaire
de se booster ou de se soigner. Il gagne par l'usure plutôt que par la force
brute.

Références : **Nostenfer** (Crobat, Poison/Vol rapide, Infiltration), en
moins fort (470 contre 535), et **Nosferalto** pour le stade final d'une
famille courte (capture, expérience, EV).

Le type Insecte/Poison est déjà porté par la famille Larve : Shin Larve est
lente (Vit 33) et encaisse, Minoskito est son opposé, rapide et fragile en
Défense.

## Stades

| | Moskito | Minoskito |
|---|---|---|
| Types | Insecte / Poison | Insecte / Poison |
| PV | 45 | 75 |
| Attaque | 48 | 75 |
| Défense | 35 | 60 |
| Atq. Spé | 32 | 55 |
| Déf. Spé | 42 | 80 |
| Vitesse | 78 | 125 |
| **Total** | **280** | **470** |
| Évolution | niv. 20 | – |
| Capture / Exp. | 255 / 55 | 90 / 160 |
| EV | Vit +1 | Vit +2 |

Stats sacrifiées : l'Attaque, modeste pour un rapide (un perturbateur n'a pas
besoin de gros dégâts, et ça l'éloigne de Kwak Vent, Att 108), et l'AtqSpé
(attaques offensives physiques).

Comparaisons (outil `similaires`) :
- Moskito : Miaouss (290), Gribouraigne (290) ; côté Osatopia, Bwak Vent
  (310) et Tofu (250), d'autres types.
- Minoskito : Pashmilla (470), Chaffreux (452) ; côté Osatopia, Kwak Vent
  (500), bien plus offensif.

## Talents

| Emplacement | Moskito | Minoskito |
|---|---|---|
| 1 | Infiltration (Infiltrator) | Infiltration (Infiltrator) |
| 2 | Cruauté (Merciless) | Cruauté (Merciless) |
| Caché | Corps Maudit (Cursed Body) | Corps Maudit (Cursed Body) |

- Infiltration : la piqûre passe à travers Clonage, Protection et Mur Lumière.
- Cruauté : coup critique garanti contre une cible empoisonnée, se combine
  avec Toxik et Multitoxik.
- Corps Maudit : le moustique agaçant qui désactive l'attaque qui le touche.
- Écarté : Point Poison (déjà chez Shin Larve), Farceur (redondant avec
  Vit 125).

## Kit final (Minoskito, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Insecte | Vampirisme (Leech Life) | Insecte | Phys. | 80 | Rend 50 % des dégâts |
| STAB Poison | Multitoxik (Barb Barrage) | Poison | Phys. | 60 | Puissance doublée sur une cible empoisonnée |
| Perturbation | Provoc (Taunt) | Ténèbres | Statut | – | Bloque soins et boosts |
| Usure | Toxik (Toxic) | Poison | Statut | – | Prépare Multitoxik et Cruauté |

Alternatives dans le learnset : Demi-Tour, Encore, Entrave, Pics Toxik,
Direct Toxik, Gaz Corrosif, Vantardise.

## Capacités custom

Aucune.

## Learnsets

### Moskito

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 1 | Ultrason (Supersonic) | Normal | Statut | – |
| 5 | Picpic (Peck) | Vol | Phys. | 35 |
| 8 | Harcèlement (Infestation) | Insecte | Spé. | 20 |
| 11 | Dard-Nuée (Pin Missile) | Insecte | Phys. | 25 |
| 14 | Dard Mortel (Fell Stinger) | Insecte | Phys. | 50 |
| 17 | Entrave (Disable) | Normal | Statut | – |
| 19 | Multitoxik (Barb Barrage) | Poison | Phys. | 60 |
| 23 | Toxik (Toxic) | Poison | Statut | – |
| 27 | Demi-Tour (U-turn) | Insecte | Phys. | 70 |
| 31 | Vampirisme (Leech Life) | Insecte | Phys. | 80 |

### Minoskito

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Provoc (Taunt) | Ténèbres | Statut | – |
| 1 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 1 | Ultrason (Supersonic) | Normal | Statut | – |
| 5 | Picpic (Peck) | Vol | Phys. | 35 |
| 8 | Harcèlement (Infestation) | Insecte | Spé. | 20 |
| 11 | Dard-Nuée (Pin Missile) | Insecte | Phys. | 25 |
| 14 | Dard Mortel (Fell Stinger) | Insecte | Phys. | 50 |
| 17 | Entrave (Disable) | Normal | Statut | – |
| 19 | Multitoxik (Barb Barrage) | Poison | Phys. | 60 |
| 23 | Toxik (Toxic) | Poison | Statut | – |
| 27 | Demi-Tour (U-turn) | Insecte | Phys. | 70 |
| 31 | Vampirisme (Leech Life) | Insecte | Phys. | 80 |
| 35 | Encore (Encore) | Normal | Statut | – |
| 39 | Pics Toxik (Toxic Spikes) | Poison | Statut | – |
| 43 | Direct Toxik (Poison Jab) | Poison | Phys. | 80 |
| 47 | Gaz Corrosif (Corrosive Gas) | Poison | Statut | – |
| 51 | Vantardise (Swagger) | Normal | Statut | – |

Rien au-dessus de 60 de puissance avant le niveau 27, premier 80 au
niveau 31. Écartée : Double Dard (inutilisable dans le jeu).

## CT, CS et tuteurs

| | Moskito | Minoskito |
|---|---|---|
| Abri, Repos, Attraction, Reflet, Façade, Toxik (CT) | ✅ | ✅ |
| Larcin, Tourmente (CT) | ✅ | ✅ |
| Aéropique (CT) : couvre Combat et Plante | ✅ | ✅ |
| Giga-Sangsue (CT) : un drain de plus, comme Nostenfer | ✅ | ✅ |
| Échange (CT) : échange les talents | ✅ | ✅ |
| Vantardise, Blabla Dodo, Taillade (tuteurs) | ✅ | ✅ |
| Provoc (CT) | – | ✅ |
| Ailes d'Acier (CT) : couvre la Roche | – | ✅ |

Exclus volontairement :
- Provoc avant l'évolution (effacerait l'attaque d'évolution) ;
- Vol (CS) : insecte trop petit ;
- Cage Éclair, Vent Glace (perturbation en trop, ou spéciale) ;
- Danse Lames (ferait un attaquant à boost) ;
- Bombe Beurk et autres attaques spéciales fortes : il reste physique ;
- Séisme, Tunnel, Tomberoche, Éboulement, coups de poing, Force,
  Éclate-Roc, Coupe, Surf, météo, Ultralaser ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée,
  Force Cachée.
