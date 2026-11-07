# Famille Crasper

> Fantômes de pirates. Dans Dofus, Crasper (Mont des Tombeaux) et Fantômayte
> (Berceau d'Alma) sont des avis de recherche ; la Vigie pirate fait partie de
> l'équipage du Grolandais et frappe à la masse (sort *Roce* : Terre, −PM). La
> chaîne d'évolution est propre à Osatopia. — Évolutions : Crasper → Fantômayte
> (niveau 20) → Vigie pirate (niveau 38).

**État** : validée et intégrée.

## Intention
Archétype : tank offensif ·
Références : Skelénox / Noctunoir (spectre qui devient brute, Lévitation),
Sinistrail (fantôme marin à l'arme lourde), Branette (Spectre physique) ·
Pourquoi : un Spectre physique plus robuste en PV et DéfSpé que Cameliache,
avec un côté pirate porté par Pickpocket, Larcin, Sabotage et Ancrage.

## Stades
| | Crasper | Fantômayte | Vigie pirate |
|---|---|---|---|
| Constante | `SPECIES_CRASPER` | `SPECIES_FANTOMAYTE` | `SPECIES_VIGIE_PIRATE` |
| Types | Spectre | Spectre | Spectre |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 45 / 55 / 50 / 35 / 60 / 45 | 70 / 80 / 60 / 45 / 80 / 60 | 100 / 120 / 80 / 50 / 90 / 55 |
| Total | 290 | 395 | 495 |
| Talents | Lévitation / Pickpocket / caché Corps Maudit | idem | idem |
| Capture / Exp. | 190 / 60 | 100 / 142 | 45 / 240 |
| EV | DéfSpé +1 | Att +2 | Att +2, PV +1 |

Autres champs (valeurs Bitouf) : 50 % femelle, 15 cycles d'œuf,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`. Groupe d'œuf Amorphe, couleur
grise (à vérifier sur les sprites).

## Kit final
| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB fort | Masse Ombre (custom) | Spectre | Physique | 85, 30 % Vit −1 |
| Boost | Gonflette (Bulk Up) | Combat | Statut | – |
| Couverture | Sabotage (Knock Off) | Ténèbres | Physique | 65 |
| Utilitaire | Feu Follet (Will-O-Wisp) | Feu | Statut | – |

Alternatives : Esprit Frappeur (110), Hantise (90), Séisme (CT), Anti-Soin.

## Capacités custom

**Masse Ombre** (`MOVE_MASSE_OMBRE`) — Spectre, physique, 85, précision 100,
10 PP, contact. 30 % de chances de baisser la Vitesse de la cible (rappel du
−PM de *Roce*). `EFFECT_HIT` + `MOVE_EFFECT_SPD_MINUS_1`, animation d'Os
Ombre. Difficulté : facile. Apprise à l'évolution en Vigie pirate.

## Learnsets

### Crasper
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Étonnement (Astonish) | Spectre | Physique | 30 |
| 1 | Dépit (Spite) | Spectre | Statut | – |
| 5 | Entrave (Disable) | Normal | Statut | – |
| 9 | Ombre Portée (Shadow Sneak) | Spectre | Physique | 40, prio +1 |
| 12 | Larcin (Thief) | Ténèbres | Physique | 60 |
| 15 | Feu Follet (Will-O-Wisp) | Feu | Statut | – |
| 19 | Regard Noir (Mean Look) | Normal | Statut | – |
| 23 | Griffe Ombre (Shadow Claw) | Spectre | Physique | 70 |
| 28 | Balance (Pain Split) | Normal | Statut | – |
| 33 | Sabotage (Knock Off) | Ténèbres | Physique | 65 |
| 38 | Lien du Destin (Destiny Bond) | Spectre | Statut | – |
| 43 | Hantise (Phantom Force) | Spectre | Physique | 90 |

### Fantômayte
Attaques de Crasper aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Onde Folie (Confuse Ray) | Spectre | Statut | – |
| 36 | Gonflette (Bulk Up) | Combat | Statut | – |

### Vigie pirate
Attaques de Crasper aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Masse Ombre (custom) | Spectre | Physique | 85 |
| 1 | Ancrage (Anchor Shot) | Acier | Physique | 80 |
| 41 | Gonflette (Bulk Up) | Combat | Statut | – |
| 47 | Anti-Soin (Heal Block) | Psy | Statut | – |
| 53 | Esprit Frappeur (Poltergeist) | Spectre | Physique | 110 |

Gonflette arrive au niveau 36 chez Fantômayte et au 41 chez la Vigie :
évoluer tôt retarde le boost. Ancrage ne s'obtient que via le Maître des
capacités.

## CT, CS et tuteurs
| Attaque | Crasper | Fantômayte | Vigie |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Reflet, Attraction, Larcin, Provoc, Tourmente, Ball'Ombre, Danse Pluie | ✓ | ✓ | ✓ |
| Tomberoche, Casse-Brique, Éclate-Roc | ✓ | ✓ | ✓ |
| Clonage, Blabla Dodo, Ronflement, Ténacité, Vantardise, Boost (tuteurs) | ✓ | ✓ | ✓ |
| Séisme, Gonflette (CT) | – | – | ✓ |
| Éboulement (tuteur), Force (CS) | – | – | ✓ |

Exclusions volontaires : Danse Lames (Gonflette reste le seul boost),
Gonflette en CT avant la Vigie (temporisation du learnset), attaques de poing
(Poing Glace, Poing Éclair, Poing Feu…), Plongée et Cascade, attaques
spéciales hors Ball'Ombre, Coupe, Vol, Aéropique, Queue de Fer, Ailes d'Acier.
