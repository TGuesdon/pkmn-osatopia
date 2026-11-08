# Famille Nodkoko

> Palmikos de l'île de Moon (Dofus niv. 42–50, Plage de la Tortue, Île des
> naufragés). Tous leurs sorts sont Neutre : *Kokojus* réduit la portée,
> *Enfeuillage* retire des PA, *Koulraoul* (Grokoko) frappe en zone et réduit
> les dommages adverses, *Kokospiration* attire et vole de la vie. Dans
> Osatopia, la noix de coco devient cocotier puis gros cocotier.
> — Évolutions : Nodkoko → Tikoko (niveau 18) → Grokoko (niveau 36).

**État** : validée et intégrée.

## Intention
Archétype : tank offensif ·
Références : Noadkoko (le palmier Pokémon, Récolte, lent et puissant),
Tropius (bananier très robuste en PV et DéfSpé) ·
Pourquoi : un Plante pur physique, lent et endurant, qui frappe fort avec
Martobois et efface le contrecoup avec sa capacité signature Lait de Coco.
Plus offensif qu'Abrakleur (mur physique Plante), plus lent et plus robuste
que Vigie pirate.

## Stades
| | Nodkoko | Tikoko | Grokoko |
|---|---|---|---|
| Constante | `SPECIES_NODKOKO` | `SPECIES_TIKOKO` | `SPECIES_GROKOKO` |
| Types | Plante | Plante | Plante |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 55 / 55 / 65 / 30 / 40 / 20 | 80 / 80 / 75 / 40 / 70 / 45 | 120 / 110 / 90 / 50 / 95 / 40 |
| Total | 265 | 390 | 505 |
| Talents | Coque Armure / Récolte / caché Téméraire | idem | idem |
| Capture / Exp. | 190 / 60 | 110 / 140 | 45 / 245 |
| EV | Déf +1 | Att +2 | PV +2, Att +1 |

Stats sacrifiées : AtqSpé (tout passe par le physique) et Vitesse (un
cocotier ne bouge pas). Talents : Coque Armure pour la coque de la noix,
Récolte pour les noix qui repoussent (baie recyclée), Téméraire pour
renforcer Martobois et Damoclès, dont le contrecoup est compensé par le lait.

Autres champs (valeurs Bitouf) : 50 % femelle, 15 cycles d'œuf,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`. Groupe d'œuf Plante, couleur
marron (à vérifier sur les sprites).

## Kit final
| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB fort | Martobois (Wood Hammer) | Plante | Physique | 120, contrecoup 1/3 |
| Soin | Lait de Coco (custom) | Plante | Statut | – |
| Couverture | Séisme (Earthquake) | Sol | Physique | 100 |
| Boost | Gonflette (Bulk Up) | Combat | Statut | – |

Alternatives : Vampigraine à la place de Gonflette, Canon Graine (80, sans
contrecoup), Tacle Lourd, Plaquage, Éboulement (tuteur).

## Capacités custom

**Lait de Coco** (`MOVE_LAIT_DE_COCO`) — Plante, statut, 5 PP, cible le
lanceur. Soigne 50 % des PV max du lanceur et guérit son altération de
statut (brûlure, poison, paralysie, sommeil, gel). Échoue seulement si le
lanceur a tous ses PV et aucun statut. Capacité de soin (bloquée par
Anti-Soin), affectée par Saisie, animation de Lait à Boire.
Nouvel effet `EFFECT_LAIT_DE_COCO` : script de combat dérivé de Lait à Boire
(`EFFECT_SOFTBOILED`) et de Selve Salvatrice (`EFFECT_JUNGLE_HEALING`),
pris en compte par l'IA. Difficulté : moyenne. Apprise à l'évolution en
Tikoko.

## Learnsets

### Nodkoko
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Physique | 40 |
| 1 | Boul'Armure (Defense Curl) | Normal | Statut | – |
| 4 | Feuillage (Leafage) | Plante | Physique | 40 |
| 7 | Roulade (Rollout) | Roche | Physique | 30 |
| 11 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 14 | Balle Graine (Bullet Seed) | Plante | Physique | 25 ×2–5 |
| 17 | Écrasement (Stomp) | Normal | Physique | 65 |
| 22 | Canon Graine (Seed Bomb) | Plante | Physique | 80 |
| 30 | Plaquage (Body Slam) | Normal | Physique | 85 |
| 38 | Racines (Ingrain) | Plante | Statut | – |

Boul'Armure + Roulade : la noix de coco qui roule.

### Tikoko
Attaques de Nodkoko aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Lait de Coco (custom) | Plante | Statut | – |
| 26 | Gonflette (Bulk Up) | Combat | Statut | – |
| 41 | Martobois (Wood Hammer) | Plante | Physique | 120 |

### Grokoko
Attaques de Nodkoko aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Tacle Lourd (Heavy Slam) | Acier | Physique | selon le poids |
| 1 | Lait de Coco (custom) | Plante | Statut | – |
| 26 | Gonflette (Bulk Up) | Combat | Statut | – |
| 40 | Séisme (Earthquake) | Sol | Physique | 100 |
| 44 | Martobois (Wood Hammer) | Plante | Physique | 120 |

Temporisation : rester Tikoko donne Martobois au niveau 41 au lieu de 44,
au prix de Séisme et des stats de Grokoko.

## CT, CS et tuteurs
| Attaque | Nodkoko | Tikoko | Grokoko |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Reflet, Attraction, Zénith, Rune Protect | ✓ | ✓ | ✓ |
| Lance-Soleil, Giga-Sangsue, Balle Graine, Tomberoche (CT) | ✓ | ✓ | ✓ |
| Coupe, Éclate-Roc (CS) | ✓ | ✓ | ✓ |
| Boul'Armure, Roulade, Plaquage, Damoclès, Coud'Boue (tuteurs) | ✓ | ✓ | ✓ |
| Clonage, Blabla Dodo, Ronflement, Ténacité, Vantardise, Boost (tuteurs) | ✓ | ✓ | ✓ |
| Gonflette (CT), Force (CS) | – | ✓ | ✓ |
| Séisme (CT), Éboulement (tuteur) | – | – | ✓ |

Coud'Boue rappelle *Kokojus* (baisse de portée → baisse de Précision).

Exclusions volontaires : Danse Lames (Gonflette reste le seul boost),
Explosion, attaques de poing, Surf et Plongée, Ultralaser, Séisme et
Éboulement avant Grokoko (Séisme arrive au niveau 40).
