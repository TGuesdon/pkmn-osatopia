# Famille Arakne

> Araignée très commune d'Amakna, l'un des premiers monstres croisés par les
> aventuriers ; l'Abrakne est sa cousine de la forêt des Abraknydes, couverte
> d'écorce. *(Lore de mémoire, à vérifier : éléments des sorts, et origine
> d'Araknotron, inconnu dans Dofus.)*
> Évolutions : Arakne → Araknotron (niv. 18) → Abrakne (niv. 34).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`, talent dans `abilities.h` et `battle_util.c`).
Une capacité custom : le talent **Sève Avide**.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe
d'œuf `EGG_GROUP_BUG`, couleur `BODY_COLOR_BROWN` (inchangée).

## Intention

Archétype : **tank offensif vampirique**. Bonne Attaque, Défense solide
(l'écorce), Vitesse moyenne ; l'araignée tient sur le terrain en drainant
ses adversaires plutôt qu'avec un soin dédié. Coup Bas compense la Vitesse,
Toile Gluante est le clin d'œil araignée.

Références : **Gambex** (Lokix, Insecte/Ténèbres, attaquant physique,
Lentiteintée) et **Migalos** (Ariados, araignée aux défenses moyennes,
Danse Lames). Stats volontairement rehaussées par rapport à ces références,
peu jouables dans les jeux officiels.

Le type Plante a été écarté (le jeu en aura beaucoup) ; le lien avec les
Abraknydes passe par Encornebois et le talent Sève Avide.

## Stades

| | Arakne | Araknotron | Abrakne |
|---|---|---|---|
| Types | Insecte | Insecte / Ténèbres | Insecte / Ténèbres |
| PV | 45 | 72 | 90 |
| Attaque | 58 | 90 | 115 |
| Défense | 48 | 76 | 95 |
| Atq. Spé | 25 | 38 | 45 |
| Déf. Spé | 40 | 62 | 80 |
| Vitesse | 40 | 60 | 70 |
| **Total** | **256** | **398** | **495** |
| Évolution | niv. 18 | niv. 34 | – |
| Capture / Exp. | 255 / 56 | 120 / 142 | 45 / 220 |
| EV | Att +1 | Att +2 | Att +2, Déf +1 |

Stats sacrifiées : l'AtqSpé (attaquant physique) et la Vitesse (araignée
d'écorce, compensée par Coup Bas).

Comparaisons (outil `similaires`) :
- Arakne : Ratentif (255), Ponchiot (275) ; côté Osatopia, Sousouris (239),
  Tronknyde (265).
- Araknotron : Machopeur (405), Tiboudet (385) ; Crapodo (407), Milirat (440).
- Abrakne : Torgamord (485), Mastouffe (500) ; Kwak Terre (500), plus rapide
  et moins robuste. Milirat, l'autre Ténèbres physique, est bien plus fragile.

## Talents

Le talent se transmet par emplacement à l'évolution :

| Emplacement | Arakne | Araknotron | Abrakne |
|---|---|---|---|
| 1 | Essaim (Swarm) | Essaim (Swarm) | **Sève Avide** (custom) |
| 2 | Peau Dure (Rough Skin) | Peau Dure (Rough Skin) | Peau Dure (Rough Skin) |
| Caché | Filature (Stakeout) | Filature (Stakeout) | Filature (Stakeout) |

- Peau Dure : l'écorce rugueuse use l'attaquant pendant que l'araignée se soigne.
- Filature : l'araignée qui guette ; se combine avec Toile Gluante.

## Kit final (Abrakne, niv. 40–50)

Variante retenue : **tank vampire**.

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Insecte | Vampirisme (Leech Life) | Insecte | Phys. | 80 | Drain 50 %, renforcé par Sève Avide |
| STAB Ténèbres | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70, prio +1 | Compense la Vitesse |
| Boost | Gonflette (Bulk Up) | Combat | Statut | – | +1 Att / +1 Déf |
| Couverture | Encornebois (Horn Leech) | Plante | Phys. | 75 | 2ᵉ drain, l'écorce ; couvre Eau, Sol, Roche |

Alternatives dans le learnset : Toile Gluante, Mâchouille, Croque Fort,
Furie-Bond, Escarmouche.

## Capacités custom

### Talent : Sève Avide

- **Effet** : les capacités qui drainent des PV rendent 50 % de PV en plus
  (cumulable avec la Grosse Racine).
- **Le plus proche** : objet Grosse Racine (`HOLD_EFFECT_BIG_ROOT`, +30 %),
  traité dans `GetDrainedBigRootHp` (`src/battle_util.c`).
- **Intégration** : `ABILITY_SEVE_AVIDE` (après les talents de 9ᵉ génération,
  `include/constants/abilities.h`), entrée « Sève Avide » / « Drains plus
  efficaces. » dans `src/data/abilities.h`, et un ×1,5 dans
  `GetDrainedBigRootHp`. Cette fonction sert aux attaques de drain
  (`EFFECT_ABSORB`, `MOVEEND_ABSORB`) mais aussi, comme la Grosse Racine, à
  Vampigraine, Racines et Anneau Hydro : Sève Avide les renforce aussi.
  Contre Suintement, le contrecoup est amplifié de la même façon.
  L'IA le traite comme la Grosse Racine (`AI_HasDrainBoost` dans
  `battle_ai_main.c`) : petit bonus de score aux attaques de drain.
- Écartée : l'attaque custom *Saignée* (drain Ténèbres), jugée trop
  caricaturale.

## Learnsets

### Arakne

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Taillade (Fury Cutter) | Insecte | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 9 | Toile (Spider Web) | Insecte | Statut | – |
| 12 | Piqûre (Bug Bite) | Insecte | Phys. | 60 |
| 15 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |

### Araknotron

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 1 | Taillade (Fury Cutter) | Insecte | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 9 | Toile (Spider Web) | Insecte | Statut | – |
| 12 | Piqûre (Bug Bite) | Insecte | Phys. | 60 |
| 15 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 22 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 |
| 26 | Toile Gluante (Sticky Web) | Insecte | Statut | – |
| 29 | Vampirisme (Leech Life) | Insecte | Phys. | 80 |
| 33 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |

### Abrakne

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Encornebois (Horn Leech) | Plante | Phys. | 75 |
| 1 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 1 | Taillade (Fury Cutter) | Insecte | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 9 | Toile (Spider Web) | Insecte | Statut | – |
| 12 | Piqûre (Bug Bite) | Insecte | Phys. | 60 |
| 15 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 22 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 |
| 26 | Toile Gluante (Sticky Web) | Insecte | Statut | – |
| 29 | Vampirisme (Leech Life) | Insecte | Phys. | 80 |
| 33 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 38 | Gonflette (Bulk Up) | Combat | Statut | – |
| 42 | Croque Fort (Jaw Lock) | Ténèbres | Phys. | 80 |
| 46 | Furie-Bond (Lunge) | Insecte | Phys. | 80 |
| 50 | Escarmouche (First Impression) | Insecte | Phys. | 90 |

Repères : Coup Bas (70) au niv. 22, avant Voltère ; Vampirisme (80) au
niv. 29 ; aucune attaque à 90+ avant le niv. 50. Encornebois et Gonflette
sont exclusifs à Abrakne (temporisation : Gonflette 4 niveaux après
l'évolution). Recouvrements limités avec Shin Larve (Toile Gluante, Piqûre,
Vampirisme à d'autres niveaux) ; aucun avec Milirat (Tricherie écartée).

## CT, CS et tuteurs

| | Arakne | Araknotron | Abrakne |
|---|---|---|---|
| Abri, Repos, Attraction, Reflet, Façade, Toxik | ✅ | ✅ | ✅ |
| Larcin, Provoc, Tourmente | ✅ | ✅ | ✅ |
| Vantardise, Blabla Dodo, Taillade (tuteurs) | ✅ | ✅ | ✅ |
| Tunnel (l'araignée terrée, couvre Feu) | ✅ | ✅ | ✅ |
| Coupe, Éclate-Roc (CS) | ✅ | ✅ | ✅ |
| Force (CS) | – | ✅ | ✅ |
| Gonflette (CT) | – | – | ✅ |
| Riposte (tuteur) | – | – | ✅ |

Exclus volontairement :
- Gonflette avant Abrakne (casserait la temporisation du niv. 38) ;
- Danse Lames (ferait un sweeper au lieu d'un tank) ;
- Séisme (couverture trop large) ;
- Tomberoche, Éboulement (pas cohérents avec le monstre) ;
- Giga-Sangsue (drain spécial, AtqSpé 45) ;
- coups de poing, de queue, attaques volantes, spéciales et météo ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée.
