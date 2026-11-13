# Famille Masticroc

> Vers des sables (race Dofus « Vers des sables », niv. 162–170) qui hantent
> la Gorge des Vents Hurlants, la Cité Oubliée et le Boyau du Père Ver. Ils
> s'enfouissent (*Ensablage*), surgissent sous leur proie (*Surgissement*),
> l'aspirent (*Aspiration Gourmande*) et l'avalent (*Avalement*).
> — Évolutions : Masticroc → Cycloporth (niv. 16) → Trémorse (niv. 32)

**État** : validée et intégrée

## Intention
Archétype : piégeur offensif (+ poseur de pièges) · Références : Kraknoix
(Piège Sable, Tourbi-Sable), Dunaconda (ver des sables Sol pur, Mue),
Hippodocus · Pourquoi : un monstre de remplissage pour les grottes et
canyons désertiques, Sol pur, qui bloque sa proie puis la croque. Il se
distingue de Phossile (Sol pur démolisseur, Danse Lames / Séisme / Lame de
Roc) par une Vitesse plus haute, moins de bulk et un kit de piège.

Ids DofusDB : Masticroc 4729, Cycloporth 4731, Trémorse 4728.

## Stades
| | Masticroc | Cycloporth | Trémorse |
|---|---|---|---|
| Types | Sol | Sol | Sol |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 45 / 60 / 45 / 30 / 35 / 45 | 75 / 82 / 75 / 40 / 55 / 58 | 85 / 115 / 85 / 45 / 65 / 95 |
| Total | 260 | 385 | 490 |
| Talents | Prognathe / Mue · caché Piège Sable | idem | idem |
| Capture / Exp. | 190 / 56 | 100 / 133 | 45 / 225 |
| EV | Att +1 | Att +1, Déf +1 | Att +2, Vit +1 |
| Taille / poids | 0,6 m / 12 kg | 1,5 m / 120 kg | 3,2 m / 280 kg |
| Catégorie Pokédex | Sand Worm | Gulp Worm | Dune Worm |

- Cycloporth est le stade trapu et lent (Dofus : *Volvation*, +21 % de
  résistances partout, 4 PM) ; Trémorse est le plus mobile (6 PM).
- AtqSpé sacrifiée : famille entièrement physique.
- Piège Sable en talent caché : les sauvages des grottes (talents 1 et 2
  seulement) n'empêchent pas le joueur de fuir.
- Croissance `GROWTH_MEDIUM_SLOW` (comme Racaillou et Phorreveur : famille
  classique à 3 stades). Groupe d'œuf Terrestre (comme Dunaconda),
  50 % femelles, 15 cycles, bonheur standard, couleur marron.

## Kit final
| Rôle | Attaque | Type · cat. · puiss. |
|---|---|---|
| STAB qui piège | Myria-Vagues (Thousand Waves) | Sol · phys · 90, empêche de fuir |
| Morsure / couverture | Mâchouille (Crunch) | Ténèbres · phys · 80 (Prognathe) |
| Piège d'entrée | Picots (Spikes) | Sol · statut |
| Boost | Gonflette (Bulk Up) | Combat · statut |

Alternatives : Tourbi-Sable, Tunnel, Cavalerie Lourde, Assaut Frontal ·
Crocs Feu, Coup Bas · Piège de Roc, Barrage · Amass'Sable.

## Capacités custom
Aucune.

## Learnsets

### Masticroc
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Ligotage (Wrap) | Normal | Phys | 15 |
| 1 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 5 | Tourbi-Sable (Sand Tomb) | Sol | Phys | 35 |
| 9 | Morsure (Bite) | Ténèbres | Phys | 60 |
| 12 | Grimace (Scary Face) | Normal | Statut | – |
| 15 | Piétisol (Bulldoze) | Sol | Phys | 60 |

### Cycloporth
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Barrage (Block) | Normal | Statut | – |
| 1–15 | (attaques de Masticroc aux mêmes niveaux) | | | |
| 19 | Crocs Feu (Fire Fang) | Feu | Phys | 65 |
| 23 | Tunnel (Dig) | Sol | Phys | 80 |
| 27 | Picots (Spikes) | Sol | Statut | – |
| 31 | Mâchouille (Crunch) | Ténèbres | Phys | 80 |
| 35 | Amass'Sable (Shore Up) | Sol | Statut | – |
| 39 | Gonflette (Bulk Up) | Combat | Statut | – |
| 44 | Cavalerie Lourde (High Horsepower) | Sol | Phys | 95 |

### Trémorse
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Myria-Vagues (Thousand Waves) | Sol | Phys | 90 |
| 1–31 | (attaques de Cycloporth aux mêmes niveaux, sauf Barrage) | | | |
| 36 | Gonflette (Bulk Up) | Combat | Statut | – |
| 41 | Cavalerie Lourde (High Horsepower) | Sol | Phys | 95 |
| 46 | Coup Bas (Sucker Punch) | Ténèbres | Phys | 70, prio +1 |
| 52 | Assaut Frontal (Headlong Rush) | Sol | Phys | 120 |

Barrage reste exclusif à Cycloporth (`P_PRE_EVO_MOVES` à `FALSE`) : en
évoluant, il est remplacé par Myria-Vagues, qui bloque *et* frappe.

## CT, CS et tuteurs
| Attaques | Masticroc | Cycloporth | Trémorse |
|---|---|---|---|
| CT : Toxik, Abri, Repos, Façade, Attraction, Reflet, Tempête de Sable, Larcin, Séisme, Tunnel, Tomberoche, Gonflette, Hurlement, Provoc, Tourmente | ✓ | ✓ | ✓ |
| CS : Éclate-Roc, Force | ✓ | ✓ | ✓ |
| Tuteurs : Plaquage, Ténacité, Blabla Dodo, Ronflement, Coud'Boue, Éboulement, Vantardise, Damoclès, Boul'Armure, Roulade | ✓ | ✓ | ✓ |
| Ultralaser | | | ✓ |

Exclusions volontaires : poings et Casse-Brique, Coupe, Queue de Fer (ni
bras, ni griffes, ni vraie queue) ; Danse Lames (le boost de Phossile) ;
attaques spéciales offensives.
