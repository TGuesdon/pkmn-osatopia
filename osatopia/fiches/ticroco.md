# Famille Ticroco

> Dans Dofus, le Crocodaille est un crocodile des Marécages, d'élément Terre, et l'une des étapes de la quête du Dofus Ébène, un Dofus qui empoisonne (à vérifier : sorts exacts, zone, lien entre Crocoburio et le dragon Crocabulia). — Évolutions : Ticroco (`SPECIES_BEBE_CROCOBURIO`) → Crocodaille (`SPECIES_CROCODAILLE`) au niveau 25 → Crocoburio (`SPECIES_CROCOBURIO`) au niveau 45.

**État** : validée et intégrée

## Intention
Archétype : démolisseur (secondaire : attaquant à boost, via Danse Draco) · Références : Crocorible (profil de stats, crocodile terrestre), Libégon (Sol/Dragon, Draco-Griffe à l'évolution), Aligatueur (crocodile à crocs et Hydro-Queue) · Pourquoi : un prédateur du marais qui mord. **Prognathe** fait des crocs élémentaires des couvertures à 97 effectifs, **Lavabo** annule sa faiblesse à l'Eau, et le talent caché **Ébène** rappelle la quête du Dofus. Le Dragon ne se réveille qu'à l'évolution tardive du niveau 45.

## Stades
| | Ticroco | Crocodaille | Crocoburio |
|---|---|---|---|
| Types | Sol | Sol | Sol / Dragon |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 60 / 66 / 55 / 30 / 38 / 36 | 80 / 94 / 74 / 42 / 55 / 55 | 100 / 130 / 92 / 60 / 78 / 80 |
| Total | 285 | 400 | 540 |
| Talents | Prognathe (Strong Jaw), Lavabo (Storm Drain), **Ébène** (custom, caché) | idem | idem |
| Capture / Exp. | 120 / 60 | 75 / 145 | 45 / 250 |
| EV | Att +1 | Att +2 | Att +3 |
| Groupes d'œuf | Monstre / Eau 1 | Monstre / Eau 1 | Monstre / Eau 1 |

Crocoburio est passé de 515 à 540 (+5 PV, +5 Att, +4 Déf, +6 DéfSpé, +5 Vit) avec la famille Demoloch : il était un peu faible.

Stats sacrifiées : l'AtqSpé, parce qu'il est 100 % physique avec les crocs. Sa Vitesse est moyenne (c'est un prédateur à l'affût), compensée par Danse Draco. Il se distingue de Phossile (Sol, 100/105/100/50/75/70) en frappant plus fort et en encaissant moins, et du type Dragon de Dracochon par sa Vitesse et son kit de crocs.

Autres champs (valeurs Bitouf) : 50 % femelle, cycles d'œuf 15, bonheur standard, croissance moyenne-lente ; couleur verte.

## Kit final
| Rôle | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB Sol fort | Séisme (Earthquake) | Sol | Phys. | 100 |
| Croc (Prognathe) | Mâchouille (Crunch) | Ténèbres | Phys. | 80 (120) |
| STAB Dragon | Draco-Griffe (Dragon Claw) | Dragon | Phys. | 80 |
| Boost | Danse Draco (Dragon Dance) | Dragon | Statut | – |

Alternatives : Crocs Givre à la place de Mâchouille contre les Dragons et les Vols, Cavalerie Lourde, Colère, Gonflette. Avec Ébène, Crochet Venin et les attaques de contact usent la cible par l'empoisonnement grave.

## Talent custom : Ébène
- Les attaques **de contact** ont 30 % de chances d'infliger un **empoisonnement grave** (dégâts croissants, comme le Dofus Ébène).
- Plus proche : Toxitouche (Poison Touch), avec le statut de Chaîne Toxique (Toxic Chain).
- Description : « Le contact empoisonne gravement. »
- Code : `ABILITY_EBENE`, branché sur le `case ABILITY_POISON_TOUCH` de `ABILITYEFFECT_MOVE_END_ATTACKER` (`battle_util.c`), avec `MOVE_EFFECT_TOXIC` à la place de `MOVE_EFFECT_POISON`. Mêmes conditions que Toxitouche : contact, cible touchée et empoisonnable, pas d'Armure Contact (Protective Pads) ni de Ventouse (Long Reach).

## Capacités custom
Aucune.

## Learnsets
Les trois stades reprennent les attaques de base de Ticroco aux mêmes niveaux.

### Ticroco
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Griffe (Scratch) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Tourbi-Sable (Sand Tomb) | Sol | Phys. | 35 |
| 8 | Grimace (Scary Face) | Normal | Statut | – |
| 12 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 16 | Piétisol (Bulldoze) | Sol | Phys. | 60 |
| 19 | Crochet Venin (Poison Fang) | Poison | Phys. | 50 |
| 22 | Crocs Givre (Ice Fang) | Glace | Phys. | 65 |
| 24 | Trépignement (Stomping Tantrum) | Sol | Phys. | 75 |

### Crocodaille (base +)
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 28 | Crocs Feu (Fire Fang) | Feu | Phys. | 65 |
| 31 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 35 | Gonflette (Bulk Up) | Combat | Statut | – |
| 38 | Hydro-Queue (Aqua Tail) | Eau | Phys. | 90 |
| 42 | Cavalerie Lourde (High Horsepower) | Sol | Phys. | 95 |

### Crocoburio (base + Crocodaille +)
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Draco-Griffe (Dragon Claw) | Dragon | Phys. | 80 |
| 48 | Danse Draco (Dragon Dance) | Dragon | Statut | – |
| 52 | Séisme (Earthquake) | Sol | Phys. | 100 |
| 58 | Colère (Outrage) | Dragon | Phys. | 120 |

Aiguisage n'est appris qu'à l'évolution en Crocodaille (`P_PRE_EVO_MOVES` à `FALSE`).

## CT, CS et tuteurs
| Attaques | Ticroco | Crocodaille | Crocoburio |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet, Larcin, Hurlement, Tempête de Sable, Danse Pluie | ✓ | ✓ | ✓ |
| Séisme, Tunnel, Coud'Boue (tuteur) | ✓ | ✓ | ✓ |
| Tomberoche, Éboulement (tuteur), Casse-Brique, Queue de Fer, Gonflette | ✓ | ✓ | ✓ |
| Surf, Plongée, Cascade | ✓ | ✓ | ✓ |
| Coupe, Force, Éclate-Roc | ✓ | ✓ | ✓ |
| Plaquage, Damoclès, Ténacité, Clonage, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✓ | ✓ | ✓ |
| Draco-Griffe (CT02) | – | – | ✓ |
| Ultralaser | – | – | ✓ |

Exclusions volontaires : Psycho-Croc ; Danse Lames (Gonflette et Danse Draco restent ses seuls boosts) ; les attaques spéciales (Laser Glace, Lance-Flammes…) ; les coups de poing ; Draco-Griffe avant le type Dragon.
