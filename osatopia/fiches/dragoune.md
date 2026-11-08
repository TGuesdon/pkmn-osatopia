# Famille Dragoune

> Dragoune et Dragonnet sont des invocations Osamodas aux sorts Feu (Dracoflammes, Dracorage : échange de place et vol de vie, Embrasement, Souffle du Dragon : vol de vie en cône et repousse). Crocabulia, boss Dragoeuf protecteur (niv. 120, Antre de Crocabulia), est ici le gardien du Dofus Vulbis (dégâts et mobilité). — Évolutions : Dragoune → niv. 30 → Dragonnet → niv. 50 → Crocabulia.

**État** : validée et intégrée.

À vérifier (lore) : dans Dofus, Crocabulia est surtout associé au Dofus Pourpre ; le lien avec le Vulbis est un choix Osatopia.

## Intention
Archétype : sweeper mixte, pseudo-légendaire (300 / 420 / 600) · Références : Drattak (profil mixte, Intimidation), Dracolosse, Dracaufeu (dragon de feu typique) · Pourquoi : un dragon de feu classique dont le talent Vulbis récompense chaque premier K.O. en dégâts et en vitesse.

## Stades
| | Dragoune | Dragonnet | Crocabulia |
|---|---|---|---|
| Types | Feu/Dragon | Feu/Dragon | Feu/Dragon |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 50 / 62 / 45 / 58 / 40 / 45 | 70 / 88 / 62 / 82 / 55 / 63 | 92 / 125 / 85 / 120 / 80 / 98 |
| Total | 300 | 420 | 600 |
| Talents | Brasier / Intimidation / Vulbis (caché) | idem | idem |
| Capture / Exp. | 45 / 60 | 45 / 147 | 45 / 300 |
| EV | 1 Att | 1 Att, 1 AtqSpé | 1 Att, 1 AtqSpé, 1 Vit |

Autres champs : 50 % femelles, 40 cycles d'œuf, `STANDARD_FRIENDSHIP`, `GROWTH_SLOW`, groupe Dragon, couleur rouge (valeurs pseudo-légendaire).

Stats sacrifiées : les défenses (85 / 80), c'est un sweeper et non un mur.

## Kit final
| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB Feu (vol de vie, clin d'œil à Dracorage) | Lame en Peine (Bitter Blade) | Feu | Phys | 90 |
| STAB Dragon | Draco-Météore (Draco Meteor) | Dragon | Spé | 130 |
| Boost dégâts + mobilité | Danse Draco (Dragon Dance) | Dragon | Statut | – |
| Couverture (Pied Tinement) | Séisme (Earthquake) | Sol | Phys | 100 |

## Talent custom : Vulbis
- `ABILITY_VULBIS`, description « Un K.O. booste Att/Spé/Vit. » (142 px).
- Copie de Synergie en version Gen 9 : au premier K.O. infligé, +1 en Attaque, Attaque Spéciale et Vitesse, une fois par combat. Branché dans le même `case` que `ABILITY_BATTLE_BOND` (`src/battle_script_commands.c`). Test : `test/battle/ability/vulbis.c`.

## Learnsets
### Dragoune
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Flammèche (Ember) | Feu | Spé | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 5 | Ouragan (Twister) | Dragon | Spé | 40 |
| 9 | Nitrocharge (Flame Charge) | Feu | Phys | 50 |
| 13 | Draco-Souffle (Dragon Breath) | Dragon | Spé | 60 |
| 17 | Crocs Feu (Fire Fang) | Feu | Phys | 65 |
| 21 | Abattage (Breaking Swipe) | Dragon | Phys | 60 |
| 25 | Draco-Griffe (Dragon Claw) | Dragon | Phys | 80 |

### Dragonnet
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Draco-Queue (Dragon Tail) | Dragon | Phys | 60 |
| 1–25 | comme Dragoune | | | |
| 33 | Draco-Choc (Dragon Pulse) | Dragon | Spé | 85 |
| 37 | Lame en Peine (Bitter Blade) | Feu | Phys | 90 |
| 41 | Danse Draco (Dragon Dance) | Dragon | Statut | – |
| 45 | Lance-Flammes (Flamethrower) | Feu | Spé | 90 |
| 49 | Draco-Charge (Dragon Rush) | Dragon | Phys | 100 |

### Crocabulia
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Séisme (Earthquake) | Sol | Phys | 100 |
| 1 | Draco-Queue (Dragon Tail) | Dragon | Phys | 60 |
| 1–49 | comme Dragonnet | | | |
| 54 | Draco-Météore (Draco Meteor) | Dragon | Spé | 130 |
| 58 | Boutefeu (Flare Blitz) | Feu | Phys | 120 |

## CT, CS et tuteurs
| Attaques | Dragoune | Dragonnet | Crocabulia |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet, Larcin, Hurlement, Zénith, Provoc | ✓ | ✓ | ✓ |
| Draco-Griffe (CT02), Lance-Flammes, Déflagration, Queue de Fer, Ailes d'Acier, Aéropique | ✓ | ✓ | ✓ |
| Tunnel, Tomberoche, Casse-Brique, Coupe, Force, Éclate-Roc | ✓ | ✓ | ✓ |
| Tuteurs : Poing Feu, Éboulement, Coud'Boue, Taillade, Plaquage, Damoclès, Ténacité, Blabla Dodo, Ronflement, Vantardise | ✓ | ✓ | ✓ |
| Surchauffe, Vol (CS) | – | ✓ | ✓ |
| Séisme (CT26), Ultralaser | – | – | ✓ |

Exclusions volontaires : Séisme avant Crocabulia (récompense d'évolution) ; Danse Lames et Gonflette (Danse Draco reste son seul boost) ; les spéciales hors type (Laser Glace, Tonnerre, Surf…).
