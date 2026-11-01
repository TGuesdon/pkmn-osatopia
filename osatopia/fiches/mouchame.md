# Famille Mouchame

> Mouche des tas d'ordures qui devient un frelon venimeux. *(Lore de mémoire,
> à vérifier : éléments des sorts de Mouchame et Morfrelon, zone.)*
> Évolutions : Mouchame → Morfrelon (niv. 32).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_BUG`, couleur `BODY_COLOR_BROWN` (inchangée).

## Intention

Archétype : **attaquant à boost spécial**, avec un peu de **nettoyeur
rapide**. Morfrelon se booste (Hâte, Machination) puis enchaîne STAB Poison
et STAB Vol pour mettre K.O., là où Minoskito use l'adversaire.

Référence : **Nostenfer** (Crobat, Poison/Vol rapide), en version spéciale
et moins robuste (485 contre 535).

Pourquoi : Vol / Poison plutôt qu'Insecte / Poison, plus original et adapté
au gabarit. Le poison spécial était libre parmi les monstres custom :
Minoskito, Serpiplume et Champagnon sont physiques, et aucun n'apprend Bombe
Beurk, Choc Venin ou Cradovague par niveau.

## Stades

| | Mouchame | Morfrelon |
|---|---|---|
| Types | Vol / Poison | Vol / Poison |
| PV | 50 | 70 |
| Attaque | 35 | 60 |
| Défense | 40 | 60 |
| Atq. Spé | 70 | 110 |
| Déf. Spé | 45 | 70 |
| Vitesse | 80 | 115 |
| **Total** | **320** | **485** |
| Évolution | niv. 32 | – |
| Talents | Œil Composé / Corrosion / *Puanteur* | Œil Composé / Corrosion / *Puanteur* |
| Capture / Exp. | 190 / 58 | 75 / 175 |
| EV | AtqSpé +1 | AtqSpé +1, Vit +1 |

Stats sacrifiées : l'Attaque (il est spécial) et la Défense (insecte
fragile). Mouchame est à 320, haut de fourchette, parce qu'il reste seul
jusqu'au niveau 32.

Comparaisons (outil `similaires`) :
- Mouchame : Larméléon (310), Tritox (320) ; côté Osatopia, Bwak Feu (310)
  et Dolbinos (330).
- Morfrelon : Malamandre (480), Fulgulairo (490) ; côté Osatopia, Kwak Feu
  (500, plus lent et plus robuste) et Dokachu (460).

Talents :
- Œil Composé : les yeux à facettes, Vent Violent passe à ~91 % de précision.
- Corrosion : empoisonne Acier et Poison. Avec Toxik, c'est sa réponse aux
  Acier qui bloquent ses deux STAB.
- Puanteur (caché) : la mouche à ordure, 10 % d'apeurer.

## Kit final (Morfrelon, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Poison | Bombe Beurk (Sludge Bomb) | Poison | Spé. | 90 | 30 % de poison |
| STAB Vol | Vent Violent (Hurricane) | Vol | Spé. | 110 | Fiabilisé par Œil Composé |
| Boost | Machination (Nasty Plot) | Ténèbres | Statut | – | +2 AtqSpé |
| Utilitaire | Toxik (Toxic, CT) | Poison | Statut | – | Avec Corrosion, contre les Acier |

Alternatives : Choc Venin, Cradovague, Hâte, Bourdon, Vent Mauvais, Ball'Ombre
(CT). Canicule écartée : pas de feu pour un insecte.

## Capacités custom

Aucune.

## Learnsets

### Mouchame

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Purédpois (Smog) | Poison | Spé. | 30 |
| 1 | Tornade (Gust) | Vol | Spé. | 40 |
| 5 | Gaz Toxik (Poison Gas) | Poison | Statut | – |
| 9 | Survinsecte (Struggle Bug) | Insecte | Spé. | 50 |
| 13 | Bombe Acide (Acid Spray) | Poison | Spé. | 40 |
| 17 | Tranch'Air (Air Cutter) | Vol | Spé. | 60 |
| 21 | Détritus (Sludge) | Poison | Spé. | 65 |
| 25 | Choc Venin (Venoshock) | Poison | Spé. | 65 |
| 29 | Hâte (Agility) | Psy | Statut | – |
| 33 | Lame d'Air (Air Slash) | Vol | Spé. | 75 |
| 38 | Bain de Smog (Clear Smog) | Poison | Spé. | 50 |
| 43 | Vent Arrière (Tailwind) | Vol | Statut | – |

### Morfrelon

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Bourdon (Bug Buzz) | Insecte | Spé. | 90 |
| 1 | Purédpois (Smog) | Poison | Spé. | 30 |
| 1 | Tornade (Gust) | Vol | Spé. | 40 |
| 5 | Gaz Toxik (Poison Gas) | Poison | Statut | – |
| 9 | Survinsecte (Struggle Bug) | Insecte | Spé. | 50 |
| 13 | Bombe Acide (Acid Spray) | Poison | Spé. | 40 |
| 17 | Tranch'Air (Air Cutter) | Vol | Spé. | 60 |
| 21 | Détritus (Sludge) | Poison | Spé. | 65 |
| 25 | Choc Venin (Venoshock) | Poison | Spé. | 65 |
| 29 | Hâte (Agility) | Psy | Statut | – |
| 34 | Lame d'Air (Air Slash) | Vol | Spé. | 75 |
| 38 | Bombe Beurk (Sludge Bomb) | Poison | Spé. | 90 |
| 42 | Vent Mauvais (Ominous Wind) | Spectre | Spé. | 60 |
| 46 | Machination (Nasty Plot) | Ténèbres | Statut | – |
| 50 | Vent Violent (Hurricane) | Vol | Spé. | 110 |
| 55 | Cradovague (Sludge Wave) | Poison | Spé. | 95 |

Rien à 90 de puissance avant l'évolution (niv. 32). Bombe Beurk n'arrive
qu'après l'évolution (temporisation). Toxik n'est pas dans le learnset par
niveau : c'est une CT.

## CT, CS et tuteurs

| | Mouchame | Morfrelon |
|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet (CT) | ✅ | ✅ |
| Zénith, Danse Pluie (CT) | ✅ | ✅ |
| Larcin, Provoc, Tourmente (CT) | ✅ | ✅ |
| Aéropique, Ball'Ombre, Giga-Sangsue (CT) | ✅ | ✅ |
| Météores, Ténacité, Blabla Dodo, Ronflement, Vantardise, Taillade (tuteurs) | ✅ | ✅ |
| Bombe Beurk, Ultralaser (CT) | – | ✅ |
| Vol (CS) | – | ✅ |

Exclus volontairement :
- Bombe Beurk pour Mouchame : récompense de l'évolution ;
- Feu (Lance-Flammes, Déflagration, Surchauffe) : incohérent pour un insecte ;
- Séisme, Tunnel, Psyko, Tonnerre, coups de poing, Ailes d'Acier ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée,
  Force Cachée.
