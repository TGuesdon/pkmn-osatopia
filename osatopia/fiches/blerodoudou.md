# Famille Blerodoudou

> Les Bléros sont des blaireaux agressifs des Crocs de verre et des Cavernes du Kolosso, sur l'île de Frigost. Wolvero frappe d'autant plus fort qu'il est blessé (*Griffemort*) et vole la vie (*Glouton*). Blérom est un colosse qui draine ses ennemis (*Carnage*) et protège les siens (*Symbiote*). — Évolutions : Blerodoudou → Wolvero (niv. 20) → Blerom (niv. 38).

**État** : validée et intégrée.

⚠ Blerodoudou est introuvable sur DofusDB (nom maison ou bébé inventé, à vérifier).

## Intention
Archétype : brute physique / wallbreaker lent, encaisseur offensif en second. · Références : Mackogneur, Bétochef. · Pourquoi : des blaireaux très agressifs aux grandes griffes, très musclés au stade final. Combat pur, la glace de Frigost passe par Isograisse et des attaques physiques Glace de couverture.

## Stades
| | Blerodoudou | Wolvero | Blerom |
|---|---|---|---|
| Types | Combat | Combat | Combat |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 65 / 75 / 50 / 25 / 40 / 40 | 85 / 100 / 65 / 30 / 52 / 63 | 115 / 135 / 90 / 35 / 70 / 45 |
| Total | 295 | 395 | 490 |
| Talents | Griffe Dure / Isograisse / *Hémorragie* | idem | idem |
| Capture / Exp. | 190 / 60 | 90 / 140 | 45 / 250 |
| EV | Att 1 | Att 2 | Att 2, PV 1 |

Autres valeurs : 50 % femelles, éclosion 15, bonheur standard, croissance moyenne-lente, groupe œuf Terrestre, couleur marron.

## Kit final
| Rôle | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB fort | Coup Croix (Cross Chop) | Combat | Phys. | 100 |
| STAB situationnel (*Griffemort*) | Contre (Reversal) | Combat | Phys. | var. |
| Couverture Vol/Dragon/Sol | Avalanche | Glace | Phys. | 60 (×2) |
| Boost | Aiguisage (Hone Claws) | Ténèbres | Statut | — |

Talents :
- **Griffe Dure** : renforce son kit, presque entièrement au contact.
- **Isograisse** : l'île de glace.
- **Hémorragie** (caché, talent Osatopia) : 20 % de faire saigner à chaque attaque physique. Il remplace Colérique.

## Capacités custom
Déchirure (statut, fait saigner) et Lacération (75, 10 % de saignement), avec le talent Hémorragie : voir [`osatopia/mecaniques/saignement.md`](../mecaniques/saignement.md). Elles remplacent Grimace et Éclate Griffe.

## Learnsets

### Blerodoudou
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Griffe (Scratch) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | — |
| 5 | Cogne (Arm Thrust) | Combat | Phys. | 15 |
| 9 | Combo-Griffe (Fury Swipes) | Normal | Phys. | 18 |
| 12 | Poing Karaté (Karate Chop) | Combat | Phys. | 50 |
| 15 | Aiguisage (Hone Claws) | Ténèbres | Statut | — |
| 18 | Éclats Glace (Ice Shard) | Glace | Phys. | 40 |
| 24 | Lacération | Ténèbres | Phys. | 75 |
| 27 | Déchirure | Ténèbres | Statut | — |

### Wolvero
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Contre (Reversal) | Combat | Phys. | var. |
| 1–27 | (comme Blerodoudou) | | | |
| 30 | Sacrifice (Submission) | Combat | Phys. | 80 |
| 33 | Griffe Ombre (Shadow Claw) | Spectre | Phys. | 70 |
| 36 | Avalanche | Glace | Phys. | 60 |
| 42 | Coup Croix (Cross Chop) | Combat | Phys. | 100 |
| 46 | Chute Glace (Icicle Crash) | Glace | Phys. | 85 |
| 50 | Ultime Bastion (No Retreat) | Combat | Statut | — |
| 55 | Surpuissance (Superpower) | Combat | Phys. | 120 |

### Blerom
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Coup Croix (Cross Chop) | Combat | Phys. | 100 |
| 1–36 | (comme Wolvero, sans Contre) | | | |
| 42 | Chute Glace (Icicle Crash) | Glace | Phys. | 85 |
| 46 | Ultime Bastion (No Retreat) | Combat | Statut | — |
| 50 | Surpuissance (Superpower) | Combat | Phys. | 120 |

Contre est exclusif à Wolvero (`P_PRE_EVO_MOVES` à `FALSE`) : à garder avant d'évoluer.

## CT, CS et tuteurs
| Attaque | Blerodoudou | Wolvero | Blerom |
|---|---|---|---|
| Toxik, Abri, Repos, Attraction, Façade, Reflet, Ténacité, Blabla Dodo, Ronflement, Vantardise, Larcin, Provoc, Tourmente, Hurlement | ✓ | ✓ | ✓ |
| Gonflette, Casse-Brique, Éclate-Roc, Force, Riposte, Frappe Atlas | ✓ | ✓ | ✓ |
| Draco-Griffe, Aéropique, Coupe, Taillade, Faux-Chage, Danse Lames | ✓ | ✓ | ✓ |
| Tunnel, Tomberoche, Éboulement, Plaquage | ✓ | ✓ | ✓ |
| Séisme, Damoclès | | ✓ | ✓ |

Exclusions volontaires :
- tous les poings (Mitra-Poing, Dynamo-Poing, Poings Feu/Glace/Éclair, Ultimapoing), puisqu'il frappe avec ses griffes ;
- les attaques spéciales (Laser Glace, Vent Glace…) ;
- Queue de Fer et Ultralaser.
