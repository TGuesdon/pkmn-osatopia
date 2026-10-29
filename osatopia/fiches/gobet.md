# Famille Gobet

> Petit gobelin violet armé d'une lance ; le Gob Trotteur est le même gobet
> monté sur une bête squelettique. *(Lore de mémoire, à vérifier : éléments
> des sorts et zone du Gobet.)*
> Évolutions : Gobet → Gob Trotteur (niv. 24).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` (famille
Bitouf) ; groupe d'œuf `EGG_GROUP_HUMAN_LIKE`, couleur `BODY_COLOR_PURPLE`.

## Intention

Archétype : **nettoyeur rapide** (revenge killer), avec une pointe de
**perturbateur**. Gobet est un chapardeur sournois ; une fois monté, le Gob
Trotteur frappe vite et fort, finit les cibles affaiblies avec Coup Bas, puis
repart avec Demi-Tour. Il reste fragile.

Référence : **Farfuret** (Ténèbres/Glace, 430), dont il reprend le profil
(Att 95–100, Vit 115–120, défenses basses). **Grimalin** pour le gobelin
sournois au premier stade.

Ténèbres pur aux deux stades. La monture squelettique s'exprime par le
movepool : Os Ombre (Spectre) à l'évolution. Abrakne, l'autre attaquant
Ténèbres custom, est lent et robuste (Vit 70) ; le Gob Trotteur est son
opposé.

## Stades

| | Gobet | Gob Trotteur |
|---|---|---|
| Types | Ténèbres | Ténèbres |
| PV | 42 | 65 |
| Attaque | 65 | 100 |
| Défense | 35 | 60 |
| Atq. Spé | 30 | 45 |
| Déf. Spé | 30 | 55 |
| Vitesse | 83 | 120 |
| **Total** | **285** | **445** |
| Évolution | niv. 24 | – |
| Capture / Exp. | 190 / 58 | 75 / 165 |
| EV | Vit +1 | Att +1, Vit +1 |

Stats sacrifiées : l'AtqSpé (lancier physique) et les défenses, pour garder
un attaquant fragile.

Comparaisons (outil `similaires`) :
- Gobet : Gribouraigne (290), Nirondelle (270) ; côté Osatopia, Moskito (280),
  qui encaisse mieux en spécial et frappe moins fort (Att 48).
- Gob Trotteur : Farfuret (430), Rapasdepic (442), Chaffreux (452) ; côté
  Osatopia, Minoskito (470, Att 75 / DéfSpé 80) et Kwak Vent (500, plus
  complet).

## Talents

| Emplacement | Gobet | Gob Trotteur |
|---|---|---|
| 1 | Tir Vif (Quick Draw) | Tir Vif (Quick Draw) |
| 2 | Filature (Stakeout) | Filature (Stakeout) |
| Caché | Pickpocket (Pickpocket) | Pickpocket (Pickpocket) |

- Tir Vif : 30 % de chances d'agir en premier dans sa tranche de priorité
  avec une attaque offensive (pas de statut).
- Filature : dégâts doublés contre une cible entrée sur le terrain ce tour-ci.
  En aventure, l'IA change rarement ; à tester sur les remplacements après
  K.O.
- Pickpocket : vole l'objet de l'attaquant au contact. Va avec Larcin et
  Sabotage.
- Écartés : Spectro-Bouclier (la carcasse qui encaisse le premier coup),
  Corps Maudit.

## Kit final (Gob Trotteur, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB fort | Génusection (Kowtow Cleave) | Ténèbres | Phys. | 85 | Feint de se prosterner, ne rate jamais |
| Priorité | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 prio+1 | Échoue si la cible n'attaque pas |
| Couverture / monture | Os Ombre (Shadow Bone) | Spectre | Phys. | 85 | Ruade de la monture squelettique |
| Pivot | Demi-Tour (U-turn) | Insecte | Phys. | 70 | Le cavalier frappe et file |

Alternatives dans le learnset ou les CT : Danse Lames, Sabotage, Exécu-Son,
Tranche-Nuit, Lame Sainte, Casse-Brique, Provoc.

## Capacités custom

Aucune. Piste écartée : un talent « Monture » sur le modèle de Tête de Gel
(la monture encaisse un coup puis le gobet combat à pied), trop coûteux
(forme alternative, sprites, code de combat).

## Learnsets

### Gobet

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Furie (Fury Attack) | Normal | Phys. | 15 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 4 | Vive-Attaque (Quick Attack) | Normal | Phys. | 40 prio+1 |
| 7 | Représailles (Payback) | Ténèbres | Phys. | 50 |
| 10 | Larcin (Thief) | Ténèbres | Phys. | 60 |
| 13 | Provoc (Taunt) | Ténèbres | Statut | – |
| 16 | Assurance (Assurance) | Ténèbres | Phys. | 60 |
| 19 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 prio+1 |
| 22 | Tranche-Nuit (Night Slash) | Ténèbres | Phys. | 70 |
| 25 | Sabotage (Knock Off) | Ténèbres | Phys. | 65 |
| 29 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 33 | Fourbette (False Surrender) | Ténèbres | Phys. | 80 |
| 37 | Exécu-Son (Throat Chop) | Ténèbres | Phys. | 80 |

Fourbette est exclusive à Gobet (`P_PRE_EVO_MOVES` à `FALSE`) : une
récompense pour qui garde un Gobet non évolué.

### Gob Trotteur

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Os Ombre (Shadow Bone) | Spectre | Phys. | 85 |
| 1 | Furie (Fury Attack) | Normal | Phys. | 15 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 4 | Vive-Attaque (Quick Attack) | Normal | Phys. | 40 prio+1 |
| 7 | Représailles (Payback) | Ténèbres | Phys. | 50 |
| 10 | Larcin (Thief) | Ténèbres | Phys. | 60 |
| 13 | Provoc (Taunt) | Ténèbres | Statut | – |
| 16 | Assurance (Assurance) | Ténèbres | Phys. | 60 |
| 19 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 prio+1 |
| 22 | Tranche-Nuit (Night Slash) | Ténèbres | Phys. | 70 |
| 27 | Sabotage (Knock Off) | Ténèbres | Phys. | 65 |
| 31 | Demi-Tour (U-turn) | Insecte | Phys. | 70 |
| 35 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 40 | Génusection (Kowtow Cleave) | Ténèbres | Phys. | 85 |
| 45 | Exécu-Son (Throat Chop) | Ténèbres | Phys. | 80 |
| 50 | Lame Sainte (Sacred Sword) | Combat | Phys. | 90 |

Os Ombre (85) arrive au niveau 24, un peu tôt : c'est la signature de
l'évolution, compensée par la fragilité. Rien à 90+ avant le niveau 50.
Points communs avec Abrakne : Groz'Yeux et Coup Bas seulement. Écartées :
Feinte et Poursuite (inutilisables dans le jeu).

## CT, CS et tuteurs

| | Gobet | Gob Trotteur |
|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet (CT) | ✅ | ✅ |
| Zénith, Danse Pluie (CT) | ✅ | ✅ |
| Provoc, Tourmente, Larcin (CT) | ✅ | ✅ |
| Casse-Brique (CT) : couvre Ténèbres et Acier | ✅ | ✅ |
| Aéropique (CT) : coup de lance qui ne rate pas | ✅ | ✅ |
| Tomberoche (CT) : couvre Vol | ✅ | ✅ |
| Tunnel (CT) | ✅ | ✅ |
| Coupe, Éclate-Roc (CS) | ✅ | ✅ |
| Danse Lames, Taillade, Vantardise (tuteurs) | ✅ | ✅ |
| Ténacité, Blabla Dodo, Ronflement, Coud'Boue (tuteurs) | ✅ | ✅ |
| Ultralaser (CT) | – | ✅ |
| Force (CS) : la monture | – | ✅ |
| Éboulement (tuteur) | – | ✅ |
| Damoclès, Plaquage (tuteurs) : charge de la monture | – | ✅ |

Exclus volontairement :
- Séisme : couverture trop forte à Vit 120, Tunnel suffit ;
- Ball'Ombre : spéciale, et Os Ombre couvre déjà la monture ;
- Mitra-Poing et les poings des tuteurs (Poing Feu, Poing Glace,
  Poing Éclair, Ultimapoing, Dynamo-Poing), Queue de Fer : il se bat à la
  lance ;
- Gonflette : Danse Lames suffit comme boost ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée,
  Force Cachée.
