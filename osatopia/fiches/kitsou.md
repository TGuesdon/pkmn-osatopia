# Famille Kitsou

> Dans le lore Dofus (à vérifier : éléments des sorts, zone), le Kitsou est un renard magique très mobile qui envoie des étoiles. — Évolutions : aucune (stade unique, `SPECIES_KITSOU`).

**État** : validée et intégrée

## Intention
Archétype : balayeur rapide, spécial dominant, canon de verre (secondaire : attaquant mixte léger) · Références : Rubombelle (Vit et AtqSpé), Gob Trotteur (rareté, capture, exp.), Farfaduvet (Fée rapide) · Pourquoi : un renard Fée fragile mais qui frappe le premier ; la mobilité vient de la Vit (120), de Turbo et d'une capacité pivot Fée custom.

## Stade
| | Kitsou |
|---|---|
| Types | Fée |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 60 / 65 / 50 / 90 / 65 / 120 |
| Total | 450 |
| Talents | Magicien (Magician), Garde Magik (Magic Guard), Turbo (Speed Boost, caché) |
| Capture / Exp. | 75 / 165 |
| EV | AtqSpé +1, Vit +1 |

Stats sacrifiées : Déf (50) et PV (60). Pas de doublon avec Gob Trotteur (physique, Ténèbres) ni Minoskito (Insecte/Poison, plus tanky).

## Kit final
| Rôle | Attaque |
|---|---|
| STAB Fée | Pouvoir Lunaire (Moonblast), 95 spé. |
| Couverture | Vibrobscur (Dark Pulse), 80 spé. (Psy / Spectre) |
| Pivot | **Filante** (custom), 70 spé. |
| Boost | Machination (Nasty Plot), AtqSpé +2 |

## Capacités custom
| Nom | Type | Cat. | Puiss. | Préc. | PP | Effet |
|---|---|---|---|---|---|---|
| **Filante** | Fée | Spéciale | 70 | 100 | 20 | Frappe, puis le lanceur change de place avec un coéquipier |

Description : « Une traînée d'étoiles frappe la cible, puis le lanceur file se mettre à l'abri et laisse la place à un coéquipier. »
Attaque la plus proche : Change Éclair (`MOVE_VOLT_SWITCH`), `EFFECT_HIT_ESCAPE`. Difficulté : **facile** (une entrée dans `moves_info.h`, une constante, animation empruntée).

## Learnsets
| Niv. | Attaque FR (EN) | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Vent Féérique (Fairy Wind) | Fée | Spé. | 40 |
| 1 | Vive-Attaque (Quick Attack) | Normal | Phys. | 40 (prio +1) |
| 5 | Charme (Charm) | Fée | Statut | - |
| 9 | Météores (Swift) | Normal | Spé. | 60 |
| 13 | Vampibaiser (Draining Kiss) | Fée | Spé. | 50 |
| 17 | Reflet (Double Team) | Normal | Statut | - |
| 20 | Filante (custom) | Fée | Spé. | 70 |
| 24 | Voix Envoûtante (Alluring Voice) | Fée | Spé. | 80 |
| 28 | Passe-Passe (Switcheroo) | Ténèbres | Statut | - |
| 31 | Dernier Mot (Parting Shot) | Ténèbres | Statut | - |
| 34 | Vibrobscur (Dark Pulse) | Ténèbres | Spé. | 80 |
| 38 | Plénitude (Calm Mind) | Psy | Statut | - |
| 42 | Machination (Nasty Plot) | Ténèbres | Statut | - |
| 46 | Pouvoir Lunaire (Moonblast) | Fée | Spé. | 95 |
| 50 | Éclat Magique (Dazzling Gleam) | Fée | Spé. | 80 |

## CT, CS et tuteurs
| Attaque | Source |
|---|---|
| Toxik, Repos, Abri | CT |
| Protection, Mur Lumière, Rune Protect | CT |
| Provoc, Tourmente, Attraction, Échange, Larcin | CT |
| Façade | CT |
| Psyko, Ball'Ombre, Tonnerre | CT |
| Vantardise, Substitut, Ténacité, Blabla Dodo, Cage-Éclair | Tuteur |
| Coupe | CS |

Exclusions volontaires : Météores en tuteur (déjà niv. 9), Plénitude en CT (déjà niv. 38), Lance-Flammes (hors thème), Danse-Lames et poings élémentaires, Séisme, Surf, Lance-Soleil, Blizzard, Hyper Rayon (renard fragile, spécial). Les tuteurs sont à revérifier dans les scripts à l'intégration.
