# Saignement

> Statut Osatopia : une plaie qui saigne à chaque tour. Plus la victime est rapide, plus elle saigne (« se déplacer en étant blessé aggrave les dégâts »).

## Règles
- **Statut majeur** (`STATUS1_BLEED`), comme Brûlure ou Poison :
  - exclusif avec les autres statuts ;
  - icône **SAI** rouge sombre ;
  - persiste après un changement et dans la sauvegarde.
- **Dégâts en fin de tour** : de 1/16 à 1/8 des PV max selon la **Vitesse de base de l'espèce**.
  - Vitesse ≤ 50 → 1/16 ; Vitesse ≥ 110 → 1/8 ; linéaire entre les deux.
  - Formule : `PV max × (Vitesse bornée + 10) / 960`.
  - Exemples : Qulbutoké (33) 1/16 ; Pikachu (90) ≈ 1/9,6 ; Voltali (130) 1/8.
- **Immunités** : types Spectre, Acier et Roche (pas de sang). Garde Magik bloque les dégâts.
- **Soins** :
  - Total Soin, Guérison, Baie Prine, Repos, Centre Pokémon ;
  - talents qui soignent tous les statuts (Mue, Hydratation, Médic Nature…).
  - Les soins ciblés (Antidote, Anti-Brûle…) ne le soignent pas.
- **Interactions** :
  - Façade double sa puissance en saignant ;
  - Psycho Transfert transmet le Saignement ;
  - pas d'animation dédiée : il réutilise celle de la Brûlure.

## Capacités et talent
| | Type | Cat. | Puiss. | Préc. | PP | Effet |
|---|---|---|---|---|---|---|
| **Déchirure** | Ténèbres | Statut | — | 85 | 15 | Fait saigner la cible (comme Feu Follet) |
| **Lacération** | Ténèbres | Phys. | 75 | 100 | 15 | 10 % de faire saigner. Contact, tranchante (Incisif) |

**Hémorragie** (talent) : 20 % de chances de faire saigner la cible à chaque attaque physique qui touche.

## Monstres
| Monstre | Déchirure | Lacération | Hémorragie |
|---|---|---|---|
| Blerodoudou / Wolvero / Blerom | niv. 27 | niv. 24 | talent caché |
| Chagouar | niv. 34 | niv. 30 | — |
| Raul Mops | niv. 46 | niv. 36 | — |
| Leolhyene | niv. 26 | — | — |

## Code
- **Constantes** : `STATUS1_BLEED`, `MOVE_EFFECT_BLEED` (avant `MOVE_EFFECT_CONFUSION` pour rester un statut majeur), `ENDTURN_BLEED`, `AILMENT_BLD`.
- **Fonctions** : `CanBleed` et `GetBleedDamage` dans `src/battle_util.c` ; dégâts dans `HandleEndTurnBleed` (`src/battle_end_turn.c`).
- **Sauvegarde** : `STATUS1_BLEED` est ajouté **à la fin** de `sCompressedStatuses` (`src/pokemon.c`) pour ne pas casser les sauvegardes.
- **Icônes** : nouvelle ligne en bas de `graphics/battle_interface/status*.png` et de `graphics/interface/status_icons.png`.
- **Tests** : `test/battle/status1/bleed.c` (`make check TESTS="Bleed"`).
