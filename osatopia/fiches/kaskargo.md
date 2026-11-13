# Famille Kaskargo

> Escargots de l'île de Moon, rapides et virevoltants : ils font des
> pirouettes et tournent comme des toupies. Leur bave posait autrefois un
> glyphe au sol qui mettait K.O. d'un coup (sort retiré de Dofus). Dans le
> Dofus actuel, Kaskargo vit dans la Canopée du Kimbo (niv. 152–160) avec
> *Bave* (téléportation), *Coopération Baveuse* (échange de place) et *Mucus*
> (dégâts multi-éléments, -2 PM). Kokulte est absent de DofusDB (monstre
> retiré, **à vérifier**). — Évolutions : Kokulte → Kaskargo (niveau 30).

**État** : validée et intégrée.

## Intention
Archétype : nettoyeur rapide + monstre de niche (OHKO) ·
Références : Kapoera (les pirouettes : Triple Pied, Tour Rapide, Technicien),
Shaofouine (Combat pur rapide et fragile), Limaspeed (l'escargot rapide et
fragile, Délestage) ·
Pourquoi : premier Combat pur d'Osatopia. Un escargot n'a pas de bras mais un
« pied » (gastéropode) : il frappe en coups de pied et en pirouettes, jamais
au poing. Sa signature est la bave mortelle, Bave Fatale.

## Stades
| | Kokulte | Kaskargo |
|---|---|---|
| Constante | `SPECIES_KOKULTE` | `SPECIES_KASKARGO` |
| Types | Combat | Combat |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 40 / 65 / 30 / 25 / 50 / 80 | 55 / 115 / 40 / 35 / 75 / 135 |
| Total | 290 | 455 |
| Talents | Téméraire / Technicien / caché Délestage | idem |
| Capture / Exp. | 190 / 58 | 75 / 165 |
| EV | Vit +1 | Vit +2 |

Stats sacrifiées : Déf et PV (fragile), AtqSpé (tout est physique). DéfSpé
correcte grâce au mucus et à la coquille, ce qui le distingue de Gob Trotteur
(65/100/60/45/55/120).

Autres champs (valeurs Bitouf) : 50 % femelle, 15 cycles d'œuf,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_FAST` (comme Debugant et Limaspeed). Groupe d'œuf Insecte (comme
Escargaume / Limaspeed), couleur marron (à vérifier sur les sprites).

## Kit final
| Rôle | Attaque | Alternatives |
|---|---|---|
| STAB fort | Pied Voltige (Combat 130) | Talon-Marteau, Triple Pied, Sacrifice |
| Pirouette / vitesse | Tour Rapide (Normal 50, Vit +1) | — |
| Couverture | Acrobatie (Vol 55, ×2 sans objet) | Coup Bas (prio), Aéropique |
| Signature | Bave Fatale (Poison, OHKO) | Contre + Ténacité |

Synergies : Téméraire → Pied Voltige, Sacrifice, Damoclès ; Technicien →
Triple Pied, Tour Rapide, Toupie Éclat ; Délestage → Acrobatie sans objet.

## Capacités custom
**Bave Fatale** (`MOVE_BAVE_FATALE`) — Poison · Physique · puissance OHKO ·
précision 30 · PP 5 · sans contact. « Glyphe de bave mortel. Met K.O. sur le
coup. » Reprend `EFFECT_OHKO` (comme Abîme, Guillotine, Empal'Korne) :
échoue si la cible est de plus haut niveau, l'Acier est immunisé.
Animation : Toxik. Difficulté : facile.

## Learnsets
### Kokulte
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Double Pied (Double Kick) | Combat | Phys. | 30 |
| 1 | Repli (Withdraw) | Eau | Statut | – |
| 4 | Sécrétion (String Shot) | Insecte | Statut | – |
| 8 | Tour Rapide (Rapid Spin) | Normal | Phys. | 50 |
| 12 | Acidarmure (Acid Armor) | Poison | Statut | – |
| 16 | Balayette (Low Sweep) | Combat | Phys. | 65 |
| 20 | Triple Pied (Triple Kick) | Combat | Phys. | 10 |
| 24 | Toupie Éclat (Mortal Spin) | Poison | Phys. | 30 |
| 28 | Sacrifice (Submission) | Combat | Phys. | 80 |
| 33 | Hâte (Agility) — exclusive | Psy | Statut | – |
| 38 | Contre (Reversal) | Combat | Phys. | var. |

### Kaskargo
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Acrobatie (Acrobatics) | Vol | Phys. | 55 |
| 1–28 | mêmes que Kokulte | | | |
| 32 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 prio+1 |
| 36 | Ténacité (Endure) | Normal | Statut | – |
| 40 | Contre (Reversal) | Combat | Phys. | var. |
| 44 | Pied Voltige (High Jump Kick) | Combat | Phys. | 130 |
| 50 | Bave Fatale (custom) | Poison | Phys. | OHKO |

Hâte reste exclusive à Kokulte : retarder l'évolution jusqu'au niveau 33
permet de la garder (`P_PRE_EVO_MOVES` à `FALSE`).

## CT, CS et tuteurs
| Attaque | Kokulte | Kaskargo |
|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet, Blabla Dodo, Ronflement, Vantardise, Ténacité*, Provoc, Larcin | ✓ | ✓ |
| Danse Pluie, Boul'Armure*, Roulade* | ✓ | ✓ |
| Casse-Brique, Éclate-Roc (CS), Riposte* | ✓ | ✓ |
| Aéropique | ✓ | ✓ |
| Ultimawashi* (Mega Kick) | | ✓ |
| Damoclès* | | ✓ |
| Ultralaser | | ✓ |

\* tuteur. Exclusions volontaires : Danse Lames et Gonflette (pas de lames ni
de muscles), tous les coups de poing (pas de bras), Coupe (pas de griffes),
Frappe Atlas (il ne peut pas agripper), Séisme, Tunnel, Vol, Surf, et les
attaques spéciales hors Ultralaser.
