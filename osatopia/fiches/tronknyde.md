# Famille Tronknyde

> Les Abraknydiens sont des arbres vivants de la forêt des Abraknydes
> (Orée, niv. 33–50) : lents (3 PM pour l'Abraknyde), élément Terre, ils
> encaissent, se soignent (*Reconstitution Abraknydienne*), affaiblissent au
> corps à corps (*Écrasement Abraknydien*, −2 PA) et posent un glyphe au sol
> (*Glyphe Sylvestre*). L'Abrakleur Clair (Canopée du Kimbo, niv. 152–160)
> draine la vie (*Pédoncule perfide*), gagne en puissance quand on le frappe
> (*Radicelle*) et enlève les envoûtements (*Radicule*). Faibles au Feu et
> à l'Air. — Évolutions : Tronknyde → Abraknyde (niv. 16) → Abrakleur (niv. 36).

**État** : validée et intégrée. Remplace la version manuelle précédente.

## Intention
Archétype : tank offensif, « la Défense comme arme » (Mur de Fer + Big
Splash) · Références : Torterra (le starter arbre lent et physique),
Blindépique (starter mur à la Déf énorme), Noacier (le tank qui punit) ·
Pourquoi : starter Plante d'Osatopia. Il durcit son écorce et frappe avec,
draine pour tenir, et sa signature Radicule empêche l'adversaire de booster.
Plante pur assumé : il reste proche de Grokoko (tank physique Plante), mais
Grokoko gonfle son Att (Gonflette, Martobois) quand Abrakleur gonfle sa Déf.

## Stades
| | Tronknyde | Abraknyde | Abrakleur |
|---|---|---|---|
| Constante | `SPECIES_TRONKNYDE` | `SPECIES_ABRAKNYDE` | `SPECIES_ABRAKLEUR` |
| Types | Plante | Plante | Plante |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 55 / 58 / 62 / 35 / 45 / 42 | 80 / 82 / 92 / 45 / 65 / 40 | 100 / 110 / 118 / 60 / 85 / 57 |
| Total | 297 | 404 | 530 |
| Talents | Engrais / caché Toison Herbue | idem | idem |
| Capture / Exp. | 45 / 64 | 45 / 142 | 45 / 265 |
| EV | Déf +1 | Déf +2 | Déf +2, Att +1 |

Stats sacrifiées : AtqSpé (physique pur) et Vitesse (un arbre). La Vitesse
baisse au stade 2 (les 3 PM de l'Abraknyde). Face à Grokoko
(120/110/90/50/95/40) : plus de Déf, moins de PV et de DéfSpé, donc plus
exposé aux attaques spéciales (Feu, Glace), comme dans le lore.

Autres champs alignés sur les starters (Tifoux, Titardo) : 50 % femelle,
20 cycles d'œuf, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`, groupe d'œuf
Plante, couleur marron.

## Kit final
| Rôle | Attaque | Alternatives |
|---|---|---|
| STAB qui draine | Encornebois (Plante 75) | Mégafouet, Lame Feuille, Radicule |
| Arme principale | Big Splash (Body Press, Combat 80, utilise la Déf) | — |
| Boost | Mur de Fer (Déf +2) | Gonflette (CT) |
| Soin / affaiblissement | Vole-Force | Champ Herbu, Cavalerie Lourde, Séisme (CT) |

Synergies : Mur de Fer → Big Splash ; Champ Herbu → Toison Herbue (Déf ×1,5),
soin chaque tour, STAB boosté ; Radicule contre les monstres qui boostent.

## Capacités custom
**Radicule** (`MOVE_RADICULE`) — Plante · Physique · 70 · précision 100 ·
PP 15 · contact. « Fouette avec une racine qui annule les stats modifiées. »
Reprend `EFFECT_HIT` + `MOVE_EFFECT_CLEAR_SMOG` (Bain de Smog) : efface tous
les changements de stats de la cible. Effet garanti (sans `chance`), donc pas
boosté par Sans Limite, comme Bain de Smog. Animation : Mégafouet.
Difficulté : facile. Apprise à l'évolution en Abrakleur.

## Learnsets
### Tronknyde
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Écras'Face (Pound) | Normal | Phys | 40 |
| 1 | Armure (Harden) | Normal | Statut | – |
| 4 | Tapotige (Branch Poke) | Plante | Phys | 40 |
| 7 | Grimace (Scary Face) | Normal | Statut | – |
| 10 | Tranch'Herbe (Razor Leaf) | Plante | Phys | 55 |
| 13 | Champ Herbu (Grassy Terrain) | Plante | Statut | – |
| 16 | Piétisol (Bulldoze) | Sol | Phys | 60 |
| 20 | Encornebois (Horn Leech) | Plante | Phys | 75 |
| 24 | Mur de Fer (Iron Defense) | Acier | Statut | – |
| 28 | Big Splash (Body Press) | Combat | Phys | 80 |
| 32 | Vole-Force (Strength Sap) | Plante | Statut | – |
| 36 | Lame Feuille (Leaf Blade) | Plante | Phys | 90 |
| 42 | Mégafouet (Power Whip) | Plante | Phys | 120 |

### Abraknyde
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Piétisol (Bulldoze) | Sol | Phys | 60 |
| 1–32 | Socle de Tronknyde aux mêmes niveaux (sans Piétisol à 16) | | | |
| 36 | Lame Feuille (Leaf Blade) | Plante | Phys | 90 |
| 40 | Cavalerie Lourde (High Horsepower) | Sol | Phys | 95 |
| 45 | Mégafouet (Power Whip) | Plante | Phys | 120 |

### Abrakleur
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Radicule (custom) | Plante | Phys | 70 |
| 1–32 | Socle de Tronknyde aux mêmes niveaux (sans Piétisol à 16) | | | |
| 39 | Lame Feuille (Leaf Blade) | Plante | Phys | 90 |
| 43 | Cavalerie Lourde (High Horsepower) | Sol | Phys | 95 |
| 48 | Mégafouet (Power Whip) | Plante | Phys | 120 |

Temporisation : rester Abraknyde jusqu'au niveau 36 donne Lame Feuille ;
évoluer donne Radicule tout de suite et Lame Feuille à 39.

## CT, CS et tuteurs
| Attaque | Tronknyde | Abraknyde | Abrakleur |
|---|---|---|---|
| Socle : Toxik, Abri, Repos, Reflet, Attraction, Rune Protect, Protection, Ténacité, Vantardise, Blabla Dodo, Ronflement, Boul'Armure, Façade, Plaquage, Coud'Boue, Balle Graine, Giga-Sangsue, Lance-Soleil, Zénith, Riposte | ✓ | ✓ | ✓ |
| CS : Coupe, Force, Éclate-Roc | ✓ | ✓ | ✓ |
| Tomberoche, Éboulement, Tunnel | ✓ | ✓ | ✓ |
| Séisme, Gonflette | | ✓ | ✓ |
| Ultralaser | | | ✓ |

Exclusions volontaires : coups de poing et de pied (Mitra-Poing,
Dynamo-Poing, Poings élémentaires, Ultimapoing, Ultimawashi), Casse-Brique
(Big Splash couvre Combat), Danse Lames (contraire au plan Défense),
Damoclès (contrecoup), Roulade (réservée à Grokoko), Queue de Fer, Aéropique,
Larcin, Faux-Chage, Explosion.
