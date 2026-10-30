# Famille Sarkapwane

> Dans le lore Dofus (à vérifier : zone, éléments des sorts), le Sarkapwane est une créature aquatique inspirée du kappa japonais, qui attaque à la sarbacane. — Évolutions : aucune (stade unique, `SPECIES_SARKAPWANE`).

**État** : validée et intégrée

## Intention
Archétype : tireur physique rapide (attaquant à boost), fragile mais protégé par sa coupelle · Références : Ludicolo (kappa Eau/Plante, Cuvette), Nigosier (tireur qui recrache des projectiles), Colossinge / Denticrisse (profil de stats) · Pourquoi : le kappa tire sa force de la coupelle d'eau sur son crâne ; tant qu'elle est pleine (PV au max), il encaisse le premier coup, ce qui lui laisse le temps de se booster et de mitrailler avec des attaques à coups multiples.

## Stade
| | Sarkapwane |
|---|---|
| Types | Plante / Eau |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 70 / 100 / 60 / 60 / 70 / 105 |
| Total | 465 |
| Talents | **Coupelle Pleine** (custom), Multi-Coups (Skill Link), Cuvette (Rain Dish, caché) |
| Capture / Exp. | 75 / 165 |
| EV | Att +2, Vit +1 |

Stats sacrifiées : Déf (60) et PV (70), compensées par Coupelle Pleine. Faiblesses : Vol et Poison seulement ; aucune couverture Roche ou Glace (ni par niveau, ni par CT/tuteur) pour ne pas couvrir sa double faiblesse. Pas de doublon avec Tortue Bleue (Eau/Combat, plus brute et robuste) ni Gob Trotteur (Ténèbres, plus rapide).

Autres champs : 50 % femelle, cycles d'œuf 15, bonheur standard, croissance moyenne-lente, groupes d'œuf Eau 1 / Plante, couleur verte.

## Kit final
| Rôle | Attaque |
|---|---|
| STAB Eau | **Sarbacane** (custom), 25 × 2–5 coups (125 avec Multi-Coups) |
| STAB Plante | Balle Graine (Bullet Seed), 25 × 2–5 coups (125 avec Multi-Coups) |
| Boost | Exuviation (Shell Smash) : la coupelle compense la baisse des défenses |
| Utilitaire | Bluff (Fake Out), la « révérence » du kappa — ou Direct Toxik (Poison Jab) en couverture |

## Talent custom : Coupelle Pleine
- Clone de Multiécaille (Multiscale) : dégâts subis divisés par 2 quand le Pokémon a tous ses PV. Cassable par Brise Moule.
- `ABILITY_COUPELLE_PLEINE` ajouté à côté de `ABILITY_MULTISCALE` dans `GetDefenderAbilitiesModifier` (`battle_util.c`) et dans la logique de pivot de l'IA (`battle_ai_util.c`).

## Capacités custom
| Nom | Type | Cat. | Puiss. | Préc. | PP | Effet | Modèle |
|---|---|---|---|---|---|---|---|
| Sarbacane | Eau | Physique | 25 | 100 | 20 | Frappe 2 à 5 fois, projectile (ballistic) | Balle Graine, `EFFECT_MULTI_HIT` (facile) |

Animation : celle de Pistolet à O.

## Learnsets
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Feuillage (Leafage) | Plante | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Repli (Withdraw) | Eau | Statut | – |
| 7 | Aqua-Jet (Aqua Jet) | Eau | Phys. | 40 prio+1 |
| 11 | Bluff (Fake Out) | Normal | Phys. | 40 prio+3 |
| 14 | Désherbaffe (Trailblaze) | Plante | Phys. | 50 |
| 17 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 20 | Tranch'Aqua (Aqua Cutter) | Eau | Phys. | 70 |
| 24 | Balle Graine (Bullet Seed) | Plante | Phys. | 25×2–5 |
| 27 | Danse Pluie (Rain Dance) | Eau | Statut | – |
| 30 | **Sarbacane** (custom) | Eau | Phys. | 25×2–5 |
| 34 | Encornebois (Horn Leech) | Plante | Phys. | 75 |
| 38 | Direct Toxik (Poison Jab) | Poison | Phys. | 80 |
| 42 | Exuviation (Shell Smash) | Normal | Statut | – |
| 46 | Aqua-Brèche (Liquidation) | Eau | Phys. | 85 |
| 51 | Mégafouet (Power Whip) | Plante | Phys. | 120 |

## CT, CS et tuteurs
| Catégorie | Attaques |
|---|---|
| Socle | Toxik, Abri, Repos, Façade, Attraction, Danse Pluie, Blabla Dodo, Ronflement, Ténacité, Vantardise, Clonage, Balle Graine |
| STAB | Giga-Sangsue, Vibraqua, Surf, Cascade, Plongée |
| CS terrain | Coupe, Éclate-Roc |
| Couverture | Casse-Brique, Riposte (le kappa lutteur de sumo), Danse Lames (tuteur) |

Exclusions volontaires : Laser Glace, Blizzard, Vent Glace, Éboulement, Tomberoche (couvriraient la faiblesse Vol), Lance-Soleil et Zénith (pas de soleil pour un kappa), Séisme, Tunnel, attaques spéciales hors thème.
