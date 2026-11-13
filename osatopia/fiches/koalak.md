# Famille Koalak

> Marsupiaux de la Montagne des Koalaks. Le Koalak Indigo est associé aux Blops
> Indigo (élément Eau) ; le jeune Tikoala porte des Biblops dans son sac et les
> lance une fois adulte (lore à vérifier). — Évolutions : Tikoala → Koalak
> (niveau 22+ avec un Biblop, Blop ou Gloutoblop dans l'équipe).

**État** : validée et intégrée.

## Intention
Archétype : attaquant physique équilibré + utilitaire (Toile Gluante) ·
Références : Kangourex (porteur de poche), Dodoala (koala) ·
Pourquoi : un Normal polyvalent dont l'originalité est la couverture Eau
Lancer Blop et l'évolution liée à la famille Blop.

## Stades
| | Tikoala | Koalak |
|---|---|---|
| Constante | `SPECIES_KOALAK_IMMATURE` | `SPECIES_KOALAK_INDIGO` |
| Types | Normal | Normal |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 55 / 55 / 45 / 35 / 45 / 55 | 90 / 100 / 70 / 55 / 75 / 85 |
| Total | 290 | 475 |
| Talents | Ramassage / Querelleur / caché Technicien | idem |
| Capture / Exp. | 190 / 58 | 75 / 168 |
| EV | Att +1 | Att +2 |

Autres champs (valeurs Bitouf) : 50 % femelle, 15 cycles d'œuf,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_FAST` (comme Kangourex), groupe d'œuf Terrestre.

Évolution : `EVO_LEVEL` 22 avec `IF_SPECIES_IN_PARTY`, une entrée par membre de
la famille Blop (Biblop, Blop, Gloutoblop), comme Mantyke avec Rémoraid.

## Kit final
| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB fort | Plaquage (Body Slam) | Normal | Physique | 85 |
| Couverture Eau | Lancer Blop (custom) | Eau | Physique | 65, Vit −1 |
| Utilitaire | Toile Gluante (Sticky Web) | Insecte | Statut | – |
| Couverture Spectre | Mâchouille (Crunch) | Ténèbres | Physique | 80 |

Alternatives : Damoclès, Bluff, Bâillement, Coup Bas, Danse Lames.
Technicien (caché) booste Bluff, Vive-Attaque et Morsure.

## Capacités custom
**Lancer Blop** (`MOVE_LANCER_BLOP`) — Eau, physique, 65, précision 100, 15 PP.
Baisse la Vitesse de la cible d'un niveau (100 %). `EFFECT_HIT` +
`MOVE_EFFECT_SPD_MINUS_1`, comme Bond (Pounce), balistique, animation Écume.
Difficulté : facile.

## Learnsets
### Tikoala
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Écras'Face (Pound) | Normal | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Boul'Armure (Defense Curl) | Normal | Statut | – |
| 7 | Vive-Attaque (Quick Attack) | Normal | Phys. | 40 |
| 10 | Bluff (Fake Out) | Normal | Phys. | 40 |
| 13 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 17 | Coup d'Boule (Headbutt) | Normal | Phys. | 70 |
| 21 | Bâillement (Yawn) | Normal | Statut | – |
| 25 | Toile Gluante (Sticky Web) | Insecte | Statut | – |
| 29 | Plaquage (Body Slam) | Normal | Phys. | 85 |
| 33 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 40 | Damoclès (Double-Edge) | Normal | Phys. | 120 |

### Koalak
Mêmes attaques aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Lancer Blop | Eau | Phys. | 65 |
| 36 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 |
| 44 | Danse Lames (Swords Dance) | Normal | Statut | – |

## CT, CS et tuteurs
| Attaque | Tikoala | Koalak |
|---|---|---|
| Toxik, Abri, Repos, Attraction, Façade, Reflet, Larcin, Provoc, Danse Pluie | ✓ | ✓ |
| Casse-Brique, Tunnel, Tomberoche, Queue de Fer, Gonflette | ✓ | ✓ |
| Ultralaser | | ✓ |
| CS : Coupe, Force, Éclate-Roc | ✓ | ✓ |
| Tuteurs : Plaquage, Damoclès, Ultimapoing, Ultimawashi, Frappe Atlas, Riposte, Boul'Armure, Roulade, Poing Glace, Ténacité, Blabla Dodo, Ronflement, Vantardise | ✓ | ✓ |

Exclusions volontaires : Séisme ; Surf, Cascade, Plongée, Vibraqua (Lancer Blop
reste la seule attaque Eau) ; Danse Lames en tuteur (contournerait le niveau 44
de Koalak) ; Explosion.
