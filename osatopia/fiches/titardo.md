# Famille Titardo

> Titardo, Crapodo et Grenn sont des monstres de quête aux sorts Eau. Titardo croasse (Coâcoâ : dégâts Eau sur la durée, retrait de portée) et attire sa cible (Crapette) ; Grenn, crapaud en armure armé d'une lance, frappe au corps à corps (Gangrenn), protège ses alliés d'un bouclier (Batrattaque) et invoque un Grennouy. — Évolutions : Titardo → niv. 16 → Crapodo → niv. 36 → Grenn.

**État** : validée et intégrée.

Starter Eau d'Osatopia (refonte de la famille).

## Intention
Archétype : tank offensif, avec un boost tardif (attaquant à boost) · Références : Laggron (starter Eau physique et solide), Clamiral (armure et lame), Tartard (Eau/Combat équilibré) · Pourquoi : Grenn prend son armure et sa lance en devenant Eau/Combat ; c'est l'Eau/Combat robuste d'Osatopia, à côté de Tortue Bleue (rapide et fragile) et Moumoule (spécial).

## Stades
| | Titardo | Crapodo | Grenn |
|---|---|---|---|
| Types | Eau | Eau | Eau/Combat |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 52 / 65 / 50 / 45 / 50 / 48 | 72 / 86 / 68 / 55 / 62 / 65 | 95 / 115 / 90 / 70 / 85 / 75 |
| Total | 310 | 408 | 530 |
| Talents | Torrent / Cœur Noble (caché) | idem | idem |
| Capture / Exp. | 45 / 64 | 45 / 142 | 45 / 265 |
| EV | 1 Att | 2 Att | 2 Att, 1 Déf |

Autres champs inchangés : 50 % femelles, 20 cycles d'œuf, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`, groupe Eau 1, couleur verte.

Stat sacrifiée : l'AtqSpé (70), c'est un physique. Le reste est équilibré (75–95), Vitesse moyenne (75).

Correctif : Crapodo n'avait pas de `.evolutions` ; il évolue maintenant en Grenn au niveau 36.

## Kit final
| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB Eau | Aqua-Brèche (Liquidation) | Eau | Phys | 85 |
| STAB Combat (la lance) | Lame Sainte (Sacred Sword) | Combat | Phys | 90 |
| Boost | Danse Victoire (Victory Dance) | Combat | Statut | – |
| Couverture Fée | Estocorne (Smart Strike) | Acier | Phys | 70 |

## Capacités custom
Aucune. Piste écartée pour l'instant : Batrattaque (Eau physique 70, +1 Déf au lanceur à 100 %, modèle Nitrocharge).

## Learnsets
### Base commune (Titardo, Crapodo, Grenn)
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys | 40 |
| 1 | Rugissement (Growl) | Normal | Statut | – |
| 4 | Aqua-Jet (Aqua Jet) | Eau | Phys | 40 |
| 7 | Léchouille (Lick) | Spectre | Phys | 30 |
| 10 | Ultrason (Supersonic) | Normal | Statut | – |
| 13 | Balayette (Low Sweep) | Combat | Phys | 65 |
| 17 | Eau Revoir (Flip Turn) | Eau | Phys | 60 |
| 21 | Anneau Hydro (Aqua Ring) | Eau | Statut | – |
| 25 | Aqua-Brèche (Liquidation) | Eau | Phys | 85 |
| 29 | Exécu-Son (Throat Chop) | Ténèbres | Phys | 80 |
| 33 | Danse Pluie (Rain Dance) | Eau | Statut | – |

### Crapodo (en plus)
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Forte-Paume (Force Palm) | Combat | Phys | 60 |
| 38 | Gonflette (Bulk Up) | Combat | Statut | – |
| 44 | Aquatacle (Wave Crash) | Eau | Phys | 120 |

### Grenn (en plus)
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Lame Sainte (Sacred Sword) | Combat | Phys | 90 |
| 40 | Estocorne (Smart Strike) | Acier | Phys | 70 |
| 46 | Danse Victoire (Victory Dance) | Combat | Statut | – |
| 52 | Aquatacle (Wave Crash) | Eau | Phys | 120 |

## CT, CS et tuteurs
| Attaque | Titardo | Crapodo | Grenn |
|---|---|---|---|
| Surf, Cascade, Plongée, Force, Éclate-Roc (CS) | ✓ | ✓ | ✓ |
| Casse-Brique, Tomberoche, Danse Pluie | ✓ | ✓ | ✓ |
| Toxik, Abri, Repos, Façade, Reflet, Larcin, Provoc, Attraction | ✓ | ✓ | ✓ |
| Ténacité, Blabla Dodo, Vantardise, Plaquage, Frappe Atlas, Coud'Boue (tuteurs) | ✓ | ✓ | ✓ |
| Gonflette, Riposte, Damoclès | | ✓ | ✓ |
| Séisme, Coupe, Faux-Chage, Aéropique | | | ✓ |

Exclusions volontaires :
- Danse Lames : Danse Victoire reste le boost, et Tortue Bleue a déjà Danse Lames.
- Attaques spéciales (Laser Glace, Blizzard, Vibraqua, Vent Glace, Ultralaser) : c'est un physique ; Surf est gardée car c'est une CS.
- Coups de poing (Poing Glace, Poing Feu, Poing Éclair, Ultimapoing, Mitra-Poing, Dynamo-Poing), Ultimawashi et Éboulement : pas cohérents avec son physique.
- Queue de Fer, Ailes d'Acier, Hurlement : pas de queue ni d'ailes, Hurlement hors rôle.
- Coupe avant Grenn : seul Grenn a une lame.
