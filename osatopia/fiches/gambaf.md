# Famille Gambaf

> Crevette boxeuse des ruines sous-marines de Dofus (race « Monstres des
> ruines sous-marines », niv. 200–212, id DofusDB **4457** ; l'homonyme #7947
> est un monstre de quête). Carapace verte, yeux sur pédoncules, gros poings
> orange en massue, et des coups de poing d'une rapidité folle, comme la
> crevette-mante réelle. Sorts : *Poing-météore* (se téléporte sur la case
> ciblée puis frappe en zone, Eau), *Pas Chassé Frontal* (avance de 4 puis
> repousse de 4, Terre) et *Enchaînement de Coups de Poings Normaux* (Terre,
> retire 2 à 6 PA). Résistances Terre +30, Air +25, Eau et Neutre +15,
> Feu −5. Zones : Ville submergée, Ancienne Sufokia, Vestiges engloutis,
> Vaisseau du Capitaine Meno. — Sans évolution.

**État** : validée et intégrée.

Constante : `SPECIES_GAMBAF` (1730, créée pour l'occasion, juste après
Granduk ; dex National et Hoenn : après Granduk).

## Intention

Archétype : **attaquant physique rapide** (nettoyeur) · Références :
Farfurex et Dimoret (profil de stats rapide et offensif), Tygnon (le boxeur :
Poing de Fer, Mach Punch, coups de poing élémentaires), Tortue Bleue (même
typage, même rôle) ·
Pourquoi : dans Dofus, Gambaf est très rapide, inspiré des crevettes
boxeuses aux coups de poing fulgurants. Il ressemble à **Tortue Bleue**
(Eau/Combat physique rapide), c'est assumé ; il s'en démarque par les
**coups de poing** et **Poing de Fer** (tout le kit est boosté de 20 %), là où
Tortue Bleue mise sur les critiques (Chanceux, Tranch'Aqua, Coup Croix,
Danse Lames). Gambaf est aussi plus fort (510 contre 480) : c'est un monstre
sans évolution de fin de jeu.

Les deux autres Eau/Combat sont loin : Moumoule est spécial, Grenn est un
tank lent. Pas de pince : Pince-Masse, Guillotine, Hyper Cutter et Coque
Armure restent à la lignée Krabby/Krabboss.

## Stades

| | Gambaf |
|---|---|
| Constante | `SPECIES_GAMBAF` |
| Types | Eau / Combat |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 70 / 130 / 75 / 50 / 65 / 120 |
| Total | 510 |
| Talents | Poing de Fer (Iron Fist) / Querelleur (Scrappy) / caché : Impudence (Moxie) |
| Capture / Exp. | 45 / 190 |
| EV | 2 Att, 1 Vit |
| Évolution | – |

Stats sacrifiées : l'AtqSpé (physique pur) et les défenses (carapace légère :
il frappe avant d'être frappé).

Comparaisons (`similaires`) :

| Monstre | PV / Att / Déf / AtqSpé / DéfSpé / Vit | Total |
|---|---|---|
| **Gambaf** | 70 / 130 / 75 / 50 / 65 / 120 | 510 |
| Farfurex | 80 / 130 / 60 / 40 / 80 / 120 | 510 |
| Dimoret | 70 / 120 / 65 / 45 / 85 / 125 | 510 |
| Tygnon | 50 / 105 / 79 / 35 / 110 / 76 | 455 |
| Tortue Bleue (custom) | 75 / 115 / 80 / 45 / 65 / 100 | 480 |
| Moumoule (custom) | 65 / 85 / 75 / 105 / 60 / 110 | 500 |
| Grenn (custom) | 95 / 115 / 90 / 70 / 85 / 75 | 530 |
| Raul Mops (custom) | 80 / 125 / 70 / 55 / 65 / 120 | 515 |

Autres valeurs : 50 % femelle, 20 cycles d'œuf, `STANDARD_FRIENDSHIP`,
`GROWTH_SLOW` (rare de fin de jeu), groupe d'œuf Eau 3 (crustacés),
`BODY_COLOR_GREEN`. Taille 1,0 m (`.height = 10`), poids 45 kg
(`.weight = 450`), catégorie Pokédex « Boxer Shrimp ».

## Talents

| Emplacement | Talent | Intérêt |
|---|---|---|
| 1 | **Poing de Fer** (Iron Fist) | +20 % à Bond Météore, Poing Sonique, Mach Punch, Poing Glace/Éclair/Feu, Vampi-Poing, Dynamo-Poing |
| 2 | **Querelleur** (Scrappy) | le bagarreur : ses coups Combat touchent les Spectre, immunisé contre Intimidation |
| Caché | **Impudence** (Moxie) | Att +1 à chaque K.O. : le nettoyeur qui s'emballe |

## Kit final (niv. 40–50)

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB Eau 👊 | **Bond Météore** (custom) Eau · Phys · 80 · ne rate jamais | Aqua-Brèche 85, Cascade 80 (CS) |
| STAB Combat fort | **Close Combat** Combat · Phys · 120 · −1 Déf/DéfSpé | Dynamo-Poing 100 👊 (50 %, confusion), Vampi-Poing 75 👊 (soin), Mitra-Poing 150 👊 |
| Priorité 👊 | **Poing Sonique** (Jet Punch) Eau · Phys · 60 · prio +1 | Mach Punch 40 👊 prio +1 (Combat) |
| Couverture 👊 | **Poing Glace** (Ice Punch) Glace · Phys · 75 (Plante, Vol, Dragon) | Poing Éclair 75 👊 (Vol, Eau), Queue de Fer 100 (Fée), Gonflette (boost) |

👊 = coup de poing boosté par Poing de Fer.

Faiblesses Eau/Combat : Plante, Électrik, Vol, Psy, Fée. Poing Glace couvre
Plante et Vol ; Queue de Fer (CT, le telson) est la réponse aux Fée.

## Capacités custom

**Bond Météore** (`MOVE_BOND_METEORE`), inspirée du sort *Poing-météore* —
en jeu : **Meteor Leap** (62 px).
- Eau · Physique · puissance 80 · précision — (ne rate jamais,
  `.accuracy = 0`) · PP 10 · priorité 0 · contact · coup de poing
  (`.punchingMove = TRUE`) · cible `MOVE_TARGET_BOTH` (les deux adversaires
  en double, comme Éboulement).
- Description : « Warps to the foe and punches / both foes. Never misses. »
  (152 px et 126 px).
- La téléportation devient « ne rate jamais », la zone devient « touche les
  deux adversaires ».
- Attaques les plus proches : Aéropique (`EFFECT_HIT`, `.accuracy = 0`),
  Éboulement (`MOVE_TARGET_BOTH`), Poing Sonique (coup de poing Eau).
  Animation : celle de Poing Sonique.
- Difficulté : facile (`EFFECT_HIT`). Pas d'`additionalEffects`, donc rien
  à ajouter à `IsMoveSheerForceBoosted`.
- Nom de conception : le vanilla **Poing Météore** (Meteor Mash, Acier)
  existe déjà, d'où « Bond Météore ».

Pistes écartées : *Enchaînement* (Combat, coup de poing multi-coups, d'après
*Enchaînement de Coups de Poings Normaux*) ; Bond Météore à 90 / 90 % avec
20 % d'Att +1 ; Bond Météore qui ignore Abri.

## Learnsets

### Gambaf
| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| 1 | Éclate-Roc (Rock Smash) | Combat | Phys. | 40 | STAB faible (il brise les coquilles) |
| 1 | Aqua-Jet (Aqua Jet) | Eau | Phys. | 40 prio+1 | STAB faible |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – | |
| 5 | Mach Punch 👊 | Combat | Phys. | 40 prio+1 | |
| 9 | Poing Boost (Power-Up Punch) 👊 | Combat | Phys. | 40 | Att +1 si touche |
| 13 | Poing Sonique (Jet Punch) 👊 | Eau | Phys. | 60 prio+1 | priorité |
| 17 | Projection (Circle Throw) | Combat | Phys. | 60 prio−6 | le *Pas Chassé Frontal* |
| 21 | Vampi-Poing (Drain Punch) 👊 | Combat | Phys. | 75 | soin |
| 25 | Poing Glace (Ice Punch) 👊 | Glace | Phys. | 75 | couverture |
| 29 | **Bond Météore** (custom) 👊 | Eau | Phys. | 80 | signature |
| 33 | Poing Éclair (Thunder Punch) 👊 | Électrik | Phys. | 75 | couverture |
| 37 | Gonflette (Bulk Up) | Combat | Statut | – | boost |
| 41 | Dynamo-Poing (Dynamic Punch) 👊 | Combat | Phys. | 100 | |
| 45 | Close Combat | Combat | Phys. | 120 | STAB fort |

14 attaques. Rien à 90+ avant le niveau 41. Gambaf se capture tard
(routes maritimes de fin de jeu, en surf) : il arrive avec Bond Météore si
son niveau sauvage est de 29 ou plus.

## CT, CS et tuteurs

| Attaque | Source | Gambaf |
|---|---|---|
| Mitra-Poing, Gonflette, Casse-Brique | CT | ✓ |
| Toxik, Provoc, Abri, Danse Pluie, Reflet, Façade, Repos, Attraction, Larcin, Tourmente | CT | ✓ |
| Tomberoche | CT | ✓ |
| Queue de Fer (le telson) | CT | ✓ |
| Surf, Cascade, Plongée, Force, Éclate-Roc | CS | ✓ |
| Poing Feu, Poing Glace, Poing Éclair, Dynamo-Poing, Ultimapoing | Tuteur | ✓ |
| Riposte, Frappe Atlas, Ténacité, Blabla Dodo, Ronflement, Vantardise | Tuteur | ✓ |

Exclusions volontaires : Danse Lames (Gonflette reste le boost ; c'est celui
de Tortue Bleue), Coupe et Faux-Chage (massues, pas de lames ni de pinces),
Séisme et Tunnel (marin), Aéropique et Ailes d'Acier, Ultimawashi (pas de
coup de pied), les CT spéciales (Laser Glace, Blizzard, Vibraqua,
Tonnerre… ; Surf gardée comme CS), Damoclès et Plaquage, Hurlement,
Coud'Boue, Éboulement.

## Rencontre

À placer : routes maritimes de fin de jeu, en surf, rare. Niveau sauvage
conseillé : 29 ou plus (pour qu'il ait Bond Météore).

## Sprites

Récupérés depuis Dofus (id 4457, face direction 3, dos direction 7).
