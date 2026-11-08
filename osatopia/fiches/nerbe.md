# Famille Nerbe

> Plantes animées de la *Florifaune obscure* (Jungle obscure, Laboratoire du
> Tynril, niv. 126–140), aux caractéristiques parfaitement équilibrées. La
> Nerbe se renforce (*Herbe Hacha*) et brûle autour d'elle (*Mauvaise Herbe*) ;
> la Fécorce repousse (*Écorce Détonante*) et punit chaque action de sa cible
> (*Écorce Malsaine*). Lore DofusDB.
> Évolutions : Nerbe → Fécorce (Pierre Plante).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_GRASS`, couleur `BODY_COLOR_GREEN`.

## Intention

Archétype : **statut / stall**, avec **perturbateur** en secondaire. Monstre
de milieu de jeu, harceleur : il empoisonne, endort et ralentit, puis punit les
cibles affectées (Choc Venin, Châtiment) en se soignant (Giga-Sangsue,
Vole-Force). Stats équilibrées, comme dans Dofus.

Références : **Gaulet** (Amoonguss, harceleur Plante/Poison) et
**Tentacruel** (harceleur équilibré et rapide).

Se distingue de Champagnon (même typage) : spécial et assez rapide là où
Champagnon est physique, lent et plein de PV.

## Stades

| | Nerbe | Fécorce |
|---|---|---|
| Types | Plante / Poison | Plante / Poison |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 60 / 45 / 55 / 55 / 60 / 50 | 85 / 65 / 80 / 80 / 90 / 75 |
| Total | 325 | 475 |
| Évolution | Pierre Plante | – |
| Talents | Corrosion / Point Poison / Cruauté (caché) | idem |
| Capture / Exp. | 120 / 68 | 45 / 172 |
| EV | DéfSpé +1 | DéfSpé +2 |

Stat sacrifiée : l'Attaque. Ses dégâts viennent du poison et d'attaques
spéciales moyennes. Vitesse 75 : assez pour placer son statut en premier.

Comparaisons (`similaires`) : Lombre, Otaria (Nerbe) ; Lamantine, Ludicolo
(Fécorce) ; côté Osatopia, Gobglouton (465), aux types et au rôle différents.

## Kit final

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB Poison | Choc Venin (Venoshock) | Bombe Beurk, Chaîne Malsaine, Bain de Smog |
| STAB Plante / soin | Giga-Sangsue (Giga Drain) | Bombe au Sirop, Vole-Force |
| Statut | Toxik / Fil Toxique | Vampigraine, Poudre Dodo, Bâillement |
| Utilitaire | Châtiment (Hex) | Provoc, Hurlement, Échange, Dévorêve |

Talents : **Corrosion** (empoisonne aussi Acier et Poison), **Point Poison**,
**Cruauté** en caché (critique garanti sur une cible empoisonnée).

## Capacités custom

Aucune. Écorce Détonante (Eau, spéciale, recul façon Draco-Queue) avait été
envisagée ; elle reste une piste.

## Learnsets

Mécanique : la Pierre Plante peut être utilisée à tout niveau. Évoluer tôt
donne Fil Toxique, Bombe au Sirop et Vole-Force ; attendre permet à Nerbe
d'apprendre Bâillement et Synthèse (exclusifs).

### Nerbe

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Vole-Vie (Absorb) | Plante | Spé. | 20 |
| 1 | Purédpois (Smog) | Poison | Spé. | 30 |
| 4 | Poudre Toxik (Poison Powder) | Poison | Statut | – |
| 8 | Méga-Sangsue (Mega Drain) | Plante | Spé. | 40 |
| 12 | Bombe Acide (Acid Spray) | Poison | Spé. | 40 |
| 15 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 19 | Châtiment (Hex) | Spectre | Spé. | 65 |
| 23 | Choc Venin (Venoshock) | Poison | Spé. | 65 |
| 27 | Poudre Dodo (Sleep Powder) | Plante | Statut | – |
| 31 | Giga-Sangsue (Giga Drain) | Plante | Spé. | 75 |
| 35 | Toxik (Toxic) | Poison | Statut | – |
| 39 | Bâillement (Yawn) | Normal | Statut | – |
| 43 | Synthèse (Synthesis) | Plante | Statut | – |
| 47 | Bombe Beurk (Sludge Bomb) | Poison | Spé. | 90 |

### Fécorce

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Fil Toxique (Toxic Thread) | Poison | Statut | – |
| 1 | Bain de Smog (Clear Smog) | Poison | Spé. | 50 |
| 1–35 | Mêmes attaques que Nerbe aux mêmes niveaux | | | |
| 39 | Bombe au Sirop (Syrup Bomb) | Plante | Spé. | 60 |
| 42 | Vole-Force (Strength Sap) | Plante | Statut | – |
| 46 | Bombe Beurk (Sludge Bomb) | Poison | Spé. | 90 |
| 50 | Hurlement (Roar) | Normal | Statut | – |
| 54 | Chaîne Malsaine (Malignant Chain) | Poison | Spé. | 100 |

## CT, CS et tuteurs

| Attaque | Nerbe | Fécorce |
|---|---|---|
| Toxik, Provoc, Tourmente, Vantardise | ✓ | ✓ |
| Abri, Rune Protect, Repos, Blabla Dodo, Ronflement, Ténacité, Attraction | ✓ | ✓ |
| Zénith, Danse Pluie | ✓ | ✓ |
| Giga-Sangsue, Lance-Soleil, Coupe | ✓ | ✓ |
| Mur Lumière, Échange, Ball'Ombre, Hurlement, Dévorêve, Ultralaser | | ✓ |

Exclusions volontaires : **Bombe Beurk** (CT précoce, casserait son arrivée
au niv. 46–47), Cage-Éclair, Danse Lames, Gonflette, coups de poing (hors rôle
et hors physique), Reflet.
