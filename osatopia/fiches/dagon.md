# Famille Dagon

> Famille de requins des mers ; le Raul Mops, stade final, chasse armé d'une
> lance. *(Lore de mémoire, à vérifier : éléments des sorts et zone des trois
> monstres.)*
> Évolutions : Dagon → Pichon (niv. 20) → Raul Mops (niv. 36).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_WATER_2` (comme Sharpedo), couleur `BODY_COLOR_BLUE`.

## Intention

Archétype : **nettoyeur rapide** (revenge killer) + **attaquant à boost**.
Raul Mops frappe en premier grâce à sa Vitesse : Branchicrok double alors sa
puissance. Deux styles selon le talent : la **gueule** (Prognathe, morsures)
ou la **lance** (Incisif, coups tranchants).

Références : **Sharpedo** (kit Morsure → Mâchouille → Aqua-Brèche, Crocs
Givre, Hâte), avec de meilleures stats et des défenses moins fragiles.

Eau aux deux premiers stades, Eau/Ténèbres au stade final, pour se distinguer
de Tortue Bleue (Eau/Combat, poings, Danse Lames, Glissade). Faiblesses de
Raul Mops : Plante, Électrik, Combat, Insecte, Fée. Résistances : Feu, Eau,
Glace, Acier, Spectre, Ténèbres ; immunité Psy.

## Stades

| | Dagon | Pichon | Raul Mops |
|---|---|---|---|
| Types | Eau | Eau | Eau/Ténèbres |
| PV | 50 | 65 | 80 |
| Attaque | 70 | 95 | 125 |
| Défense | 35 | 50 | 70 |
| Atq. Spé | 30 | 40 | 55 |
| Déf. Spé | 35 | 50 | 65 |
| Vitesse | 65 | 90 | 120 |
| **Total** | **285** | **390** | **515** |
| Évolution | niv. 20 | niv. 36 | – |
| Capture / Exp. | 190 / 61 | 90 / 142 | 45 / 257 |
| EV | Att +1 | Att +2 | Att +2, Vit +1 |

Stats sacrifiées : l'AtqSpé (purement physique) et les défenses, moyennes.
Raul Mops reste fragile mais encaisse un coup, contrairement à Sharpedo
(460 : 70/120/40/95/40/95).

Comparaisons (outil `similaires`) : Farfurex (510), Dimoret (510), Ptéra
(515) ; côté Osatopia, Kwak Vent (500, Vol) et Tortue Bleue (480, plus lente
et plus robuste).

## Talents

| Emplacement | Dagon / Pichon / Raul Mops |
|---|---|
| 1 | Prognathe (Strong Jaw) |
| 2 | Impudence (Moxie) |
| Caché | Incisif (Sharpness) |

- Prognathe : +50 % sur Morsure, Crochet Venin, Crocs Givre, Mâchouille,
  Branchicrok.
- Impudence : Att +1 à chaque K.O., pour enchaîner en fin de combat.
- Incisif : +50 % sur Coqui-Lame, Génusection, Plaie Croix, Coupe, Taillade,
  Aéropique : la lance de Raul Mops.
- Écartés : Turbo, Peau Dure (Sharpedo, déjà utilisés), Glissade (Tortue
  Bleue).

## Kit final (Raul Mops, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Eau | Branchicrok (Fishious Rend) | Eau | Phys. | 85 | ×2 s'il agit en premier ; morsure |
| STAB Ténèbres | Génusection (Kowtow Cleave) | Ténèbres | Phys. | 85 | Ne rate jamais ; tranchante |
| Boost | Aiguisage (Hone Claws) | Ténèbres | Statut | – | Att +1, Précision +1 |
| Couverture | Crocs Givre (Ice Fang) | Glace | Phys. | 65 | Contre Plante, Dragon ; morsure |

Version « lance » (Incisif) : Coqui-Lame et Plaie Croix à la place de
Branchicrok et Crocs Givre. Alternatives : Mâchouille, Aquatacle, Hâte,
Séisme, Aqua-Jet.

Écartées : Danse Lames (Tortue Bleue), Lame Sainte et Tranche-Nuit (déjà chez
Gob Trotteur, avec Génusection).

## Capacités custom

Aucune.

## Learnsets

### Dagon

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Aqua-Jet (Aqua Jet) | Eau | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Claquoir (Clamp) | Eau | Phys. | 35 |
| 9 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 13 | Grimace (Scary Face) | Normal | Statut | – |
| 16 | Crochet Venin (Poison Fang) | Poison | Phys. | 50 |
| 19 | Crocs Givre (Ice Fang) | Glace | Phys. | 65 |

### Pichon

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Coqui-Lame (Razor Shell) | Eau | Phys. | 75 |
| 1–19 | *attaques de Dagon, mêmes niveaux* | | | |
| 24 | Grincement (Screech) | Normal | Statut | – |
| 28 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 32 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 40 | Branchicrok (Fishious Rend) | Eau | Phys. | 85 |
| 48 | Hâte (Agility) | Psy | Statut | – |
| 52 | Aquatacle (Wave Crash) | Eau | Phys. | 120 |

### Raul Mops

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Génusection (Kowtow Cleave) | Ténèbres | Phys. | 85 |
| 1 | Coqui-Lame (Razor Shell) | Eau | Phys. | 75 |
| 1–32 | *attaques de Pichon, mêmes niveaux* | | | |
| 40 | Branchicrok (Fishious Rend) | Eau | Phys. | 85 |
| 44 | Plaie Croix (X-Scissor) | Insecte | Phys. | 80 |
| 48 | Hâte (Agility) | Psy | Statut | – |
| 52 | Aquatacle (Wave Crash) | Eau | Phys. | 120 |

16 attaques. Rien à 90+ avant le niveau 52 ; STAB 80–85 à 28, 36 et 40.
Plaie Croix est exclusive à Raul Mops. Seul recoupement notable avec un
autre monstre custom : Génusection (Gob Trotteur).

## CT, CS et tuteurs

| | Dagon | Pichon | Raul Mops |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet (CT) | ✅ | ✅ | ✅ |
| Danse Pluie, Provoc, Tourmente, Larcin (CT) | ✅ | ✅ | ✅ |
| Surf, Plongée, Cascade, Éclate-Roc, Coupe (CS) | ✅ | ✅ | ✅ |
| Taillade, Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✅ | ✅ | ✅ |
| Séisme, Queue de Fer (CT) | – | ✅ | ✅ |
| Aéropique, Casse-Brique, Ultralaser (CT) | – | – | ✅ |
| Damoclès (tuteur) | – | – | ✅ |

Exclus volontairement :
- Danse Lames (tuteur) : Aiguisage reste le boost, et Tortue Bleue l'a déjà ;
- poings élémentaires (tuteurs), Laser Glace, Blizzard, Vent Glace,
  Vibraqua : monstre purement physique ;
- Force, Plaquage, Tunnel, Éboulement : peu cohérents pour un requin ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée,
  Force Cachée.
