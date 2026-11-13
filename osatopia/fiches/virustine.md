# Famille Virustine

> Krobes du Ventre de la Baleine (aussi Roc des Salbatroces et les deux
> Expéditions du Ventre de la Baleine ; niv. 200–212). Trois microbes de même
> niveau dans Dofus, qui se distinguent par la mobilité : **Virustine** (id
> 3826 ; 7 PM, Tacle -50 ; *Contamination*, Feu, « tue la cible » + Érosion ;
> *Boulet Viral*, Air, dégâts selon les PM restants), **Bacterrib** (id 3825 ;
> 5 PM, Tacle -20 ; *Sécrétion*, Air, -3 PM et -3 Portée ; *Danse répulsive*,
> Terre, repousse de 3 cases), **Tabacille** (id 3823 ; 4 PM, Tacle +20 ;
> *Échange subtil*, Neutre, échange de positions ; *Remontée gastrique*, Eau,
> durée des effets -1). 1 000 PV, 12 PA, caractéristiques égales, aucune
> résistance. — Évolutions : Virustine → Bacterrib (niv. 24) → Tabacille
> (niv. 40).

**État : validée et intégrée** (`include/constants/species.h`,
`include/constants/pokedex.h`, `src/pokemon.c`, `pokedex_orders.h`,
`species_info.h`, `gen_9.h`, `teachable_learnsets.h`, `graphics/pokemon.h`,
sprites Dofus). Pas de capacité custom (choix de l'utilisateur).

Orthographe Dofus : **Bacterrib** (deux *r*, pas « Bactérib »).

Espèces créées pour l'occasion : `SPECIES_VIRUSTINE` (1733),
`SPECIES_BACTERRIB` (1734), `SPECIES_TABACILLE` (1735). Les numéros 1730–1732
sont réservés à Gambaf, Crabe et Crustorail (intégrés sur d'autres branches).
Dex National et Hoenn : à la suite de Granduk.

Valeurs non discutées, choisies à l'intégration : `MON_GENDERLESS`
(microbes), `.eggCycles = 20`, `STANDARD_FRIENDSHIP`, `GROWTH_SLOW` (comme Tentacool)
(comme Bitouf), groupes d'œuf `EGG_GROUP_WATER_1` + `EGG_GROUP_AMORPHOUS`
(comme Mol Usk), couleur `BODY_COLOR_RED`. Pokédex : catégories *Virus*,
*Bacterium*, *Bacillus* ; tailles 0,4 / 0,9 / 1,5 m ; poids 3 / 18 / 65 kg.

## Intention

Archétype : **perturbateur contagieux** (+ pivot et nettoyeur de terrain).
C'est le Tentacool → Tentacruel d'Osatopia, le monstre qu'on croise partout
en surf : il infecte (poison grave, talent contagieux), nettoie les pièges,
puis s'en va avec Eau Revoir.

Références : **Tentacruel** (même typage, rôle de route maritime, Tour Rapide
et DéfSpé haute), **Ludicolo / Tarpaud** (profil de stats du stade final,
outil `similaires`), **Grotadmorv d'Alola** (usure par le poison, sans soin).

Démarcation avec **Mol Usk** (seul autre Eau/Poison) : Mol Usk est un mur
spécial lent qui **pose** des pièges (Pics Toxik, Toile Gluante) et se soigne.
Tabacille les **enlève** (Toupie Éclat), ne se soigne pas, change de place
(Eau Revoir) et frappe un peu plus fort. Les deux se complètent dans une
équipe et s'opposent en combat. Côté Eau, aucun autre monstre custom n'a ce
trio poison grave / nettoyage / pivot ; Crabe → Crustorail et Gambaf, conçus
en parallèle, sont physiques.

Les trois stades restent Eau/Poison (demande de l'utilisateur). Dans Dofus,
seul Tabacille a un sort Eau (*Remontée gastrique*) ; aucun n'a d'élément
« poison », qui vient du thème microbien.

Progression : les trois Krobes ont le même niveau dans Dofus, la progression
repose donc sur la corpulence, comme Bwak ou Mansot. Rendus Ankama (mis à
l'échelle automatiquement, donc tailles absolues inconnues) : Virustine est
une petite boule à pointes flottante (2 antennes), Bacterrib une « chaussette »
à 6 antennes, Tabacille un gros corps recourbé à ~9 antennes, la silhouette
la plus large. Les PM qui baissent (7 → 5 → 4) et le Tacle qui monte (-50 →
-20 → +20) vont dans le même sens : l'ordre Virustine → Bacterrib → Tabacille
colle.

## Stades

| | Virustine | Bacterrib | Tabacille |
|---|---|---|---|
| Types | Eau/Poison | Eau/Poison | Eau/Poison |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 40 / 30 / 35 / 50 / 45 / 60 | 70 / 50 / 65 / 70 / 80 / 65 | 95 / 55 / 70 / 90 / 110 / 75 |
| Total | 260 | 400 | 495 |
| Évolution | niv. 24 | niv. 40 | – |
| Talents | Odeur Tenace (Lingering Aroma) / Médic Nature (Natural Cure) / caché : Hydratation (Hydration) | idem | idem |
| Capture / Exp. | 190 / 58 | 120 / 135 | 45 / 225 |
| EV | Vit +1 | DéfSpé +2 | DéfSpé +2, PV +1 |

Stats sacrifiées : l'Attaque (kit spécial et de statut ; Toupie Éclat et Eau
Revoir servent pour leur effet, pas leurs dégâts). La Vitesse est la stat la
plus haute de Virustine (7 PM), puis devient moyenne : Tabacille (4 PM) est un
pivot lent, ce qui fait entrer son partenaire en sécurité après Eau Revoir.

| | PV | Att | Déf | AtqSpé | DéfSpé | Vit | Total |
|---|---|---|---|---|---|---|---|
| **Tabacille** | 95 | 55 | 70 | 90 | 110 | 75 | 495 |
| Tentacruel | 80 | 70 | 65 | 80 | 120 | 100 | 515 |
| Tarpaud (`similaires`) | 90 | 75 | 75 | 90 | 100 | 70 | 500 |
| Ludicolo (`similaires`) | 80 | 70 | 70 | 90 | 100 | 70 | 480 |
| Mol Usk (custom) | 110 | 50 | 80 | 80 | 120 | 35 | 475 |
| Fecorce (custom, `--custom`) | 85 | 65 | 80 | 80 | 90 | 75 | 475 |

Autres comparaisons : Virustine ≈ Arakdo, Sonistrelle, El Scarador (custom) ;
Bacterrib ≈ Mesmérella, Papilusion, Scarafeuille Bleu (custom, Insecte/Eau,
plus lent et plus spécial).

## Talents

- **Odeur Tenace** (Lingering Aroma) : un attaquant qui le touche au contact
  perd son talent au profit d'Odeur Tenace. C'est la contagion : l'infection
  passe d'un Pokémon à l'autre. Aucun monstre custom ne l'a (Halbardent a
  Momie, l'équivalent, en caché).
- **Médic Nature** (Natural Cure) : soigne son statut en quittant le combat,
  synergie avec Eau Revoir. Aucun monstre custom ne l'a.
- Caché : **Hydratation** (Hydration) : soigne le statut sous la pluie (Danse
  Pluie par CT). Aucun monstre custom ne l'a.

Alternatives : Corps Sain (Clear Body, talent de Tentacool), Corrosion (la
*Contamination* touche aussi Acier et Poison, déjà chez Mouchame et Nerbe),
Cuvette (Rain Dish). Suintement est déjà pris par Mol Usk.

## Kit final (Tabacille, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Poison / usure | Choc Venin (Venoshock) | Poison | Spé. | 65 | ×2 (130) sur une cible empoisonnée par Toupie Éclat, Fil Toxique ou Toxik |
| STAB Eau | Tir de Précision (Snipe Shot) | Eau | Spé. | 80 | taux de critique élevé, ignore les redirections ; le tireur à distance de *Sécrétion* |
| Nettoyeur | Toupie Éclat (Mortal Spin) | Poison | Phys. | 30 | enlève pièges et Vampigraine, empoisonne |
| Pivot | Eau Revoir (Flip Turn) | Eau | Phys. | 60 | *Échange subtil* : change de place |

Alternatives par emplacement :
- STAB Poison : Cradovague (95, appris au 47), Bombe Beurk (90, CT),
  Toxik.
- STAB Eau : Surf (CS, 90), Hydrocanon (110), Bulles d'O (65), Saumure (65).
- Nettoyeur : Tour Rapide (Rapid Spin, +1 Vit), Anti-Brume (Defog).
- Pivot / perturbation : Suc Digestif (Gastro Acid, *Remontée gastrique*),
  Fil Toxique (Toxic Thread), Échange (Skill Swap, CT), Provoc (CT),
  Châtiment (Hex).

## Capacités custom

Aucune (choix de l'utilisateur). La *Contamination* de Dofus est rendue par
Choc Venin, qui punit une cible déjà infectée. Pistes écartées : une attaque
custom *Contamination* (poison grave), *Boulet Viral* (puissance selon la
Vitesse, comme Boule Élek), *Danse répulsive* (force le changement, comme
Draco-Queue).

## Learnsets

Tronc commun aux trois stades (mêmes niveaux) :

| Niv. | Attaque FR (EN) | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Pistolet à O (Water Gun) | Eau | Spé. | 40 |
| 1 | Purédpois (Smog) | Poison | Spé. | 30 |
| 5 | Ultrason (Supersonic) | Normal | Statut | – |
| 9 | Siphon (Whirlpool) | Eau | Spé. | 35 |
| 13 | Bulles d'O (Bubble Beam) | Eau | Spé. | 65 |
| 17 | Douche Froide (Chilling Water) | Eau | Spé. | 50 |
| 21 | Choc Venin (Venoshock) | Poison | Spé. | 65 |
| 26 | Toupie Éclat (Mortal Spin) | Poison | Phys. | 30 |
| 29 | Châtiment (Hex) | Spectre | Spé. | 65 |
| 33 | Piège de Venin (Venom Drench) | Poison | Statut | – |
| 36 | Tir de Précision (Snipe Shot) | Eau | Spé. | 80 |

### Virustine
Le tronc seul (11 attaques). Siphon : le *Tacle*, il piège ; Bulles d'O : il
ralentit, comme *Boulet Viral* joue sur les PM.

### Bacterrib

| Niv. | Attaque FR (EN) | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Fil Toxique (Toxic Thread) | Poison | Statut | – |
| 1–36 | *tronc commun* | | | |
| 40 | Bombe Beurk (Sludge Bomb) | Poison | Spé. | 90 |
| 45 | Hydrocanon (Hydro Pump) | Eau | Spé. | 110 |

Fil Toxique = *Sécrétion* (poison et -1 Vitesse). Temporisation : Bombe Beurk
et Hydrocanon arrivent plus tôt chez Bacterrib que chez Tabacille.

### Tabacille

| Niv. | Attaque FR (EN) | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Eau Revoir (Flip Turn) | Eau | Phys. | 60 |
| 1–36 | *tronc commun* | | | |
| 43 | Suc Digestif (Gastro Acid) | Poison | Statut | – |
| 47 | Cradovague (Sludge Wave) | Poison | Spé. | 95 |
| 52 | Hydrocanon (Hydro Pump) | Eau | Spé. | 110 |

15 attaques. Eau Revoir = *Échange subtil* ; Suc Digestif = *Remontée
gastrique* (« durée des effets -1 », ici le talent adverse neutralisé). Rien
à 90+ avant le niveau 40. Proche de Tentacruel par endroits (Ultrason, Bulles
d'O, Châtiment, Cradovague, Hydrocanon), en clin d'œil ; peu de points
communs avec Mol Usk (Pistolet à O, Hydrocanon).

Écume (Bubble) écartée : inutilisable dans l'expansion.

## CT, CS et tuteurs

| | Virustine | Bacterrib | Tabacille |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet, Rune Protect (CT) | ✅ | ✅ | ✅ |
| Danse Pluie, Grêle, Vibraqua, Laser Glace, Blizzard (CT) | ✅ | ✅ | ✅ |
| Bombe Beurk, Giga-Sangsue, Mur Lumière, Échange (CT) | ✅ | ✅ | ✅ |
| Surf, Plongée, Cascade (CS) | ✅ | ✅ | ✅ |
| Vent Glace, Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✅ | ✅ | ✅ |
| Provoc (CT) | – | ✅ | ✅ |
| Ultralaser (CT) | – | – | ✅ |

Échange (Skill Swap) : l'*Échange subtil*, et avec Odeur Tenace une façon de
« contaminer » volontairement.

Exclusions volontaires : Hurlement (pas de cri ; la *Danse répulsive* n'est
pas reprise), Cage-Éclair, Séisme, Tonnerre, Psyko, Ball'Ombre,
Lance-Flammes (couverture trop large), coups de poing, Danse Lames,
Explosion, Force, Coupe, Éclate-Roc, Vol ; inutilisables (Saisie, Flash,
Retour, Frustration, Puissance Cachée, Force Cachée).

## Sprites

Récupérés depuis Dofus (`fetch`, face direction 3, dos direction 7, vraies
vues de dos pour les trois), sans alerte d'audit (l'ombre de Virustine, qui
flotte, est bien retirée).

| Stade | id DofusDB | Taille | Icône |
|---|---|---|---|
| Virustine | 3826 | petit | palette 3 |
| Bacterrib | 3825 | moyen | palette 3 |
| Tabacille | 3823 | grand | palette 3 |

## Reste à faire

- Rencontres : les placer en surf sur les routes maritimes
  (`src/data/wild_encounters.json`), comme Tentacool / Tentacruel.
- Fusion avec les branches Gambaf et Crabe / Crustorail : conflits attendus
  dans `species.h` (`SPECIES_EGG` doit pointer sur la dernière espèce),
  `pokedex.h` (enums et `*_DEX_COUNT`), `pokemon.c` et `pokedex_orders.h`.
