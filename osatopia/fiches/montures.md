# Montures : Volkorne, Dragodinde, Muldo

> Dans Dofus, la Dragodinde, le Muldo et le Volkorne sont les trois montures d'élevage : on les élève en enclos, on les croise, et elles donnent leurs caractéristiques à leur cavalier (à vérifier : éléments, zones et comportement de chacune). — Évolutions : aucune (stades uniques, `SPECIES_VOLKORNE`, `SPECIES_DRAGODINDE`, `SPECIES_MULDO`).

**État** : validée et intégrée

## Intention
Archétype : pivot (« monture ») qui sort du terrain pour porter un allié · Références : Écrémeuh / Scorvol (Volkorne), Capidextre / Dodrio (Dragodinde), Étouraptor / Kangourex (Muldo) · Pourquoi : une monture se définit par le cavalier qu'elle porte. Chacune possède une attaque pivot et le talent **Monture**, qui transmet sa meilleure stat au Pokémon qui entre à sa place. Les trois sont rapides ; leur meilleure stat (et donc le bonus transmis) les distingue.

## Stades
| | Volkorne | Dragodinde | Muldo |
|---|---|---|---|
| Types | Insecte / Vol | Normal | Eau |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 80 / 75 / 115 / 40 / 70 / 100 | 75 / 95 / 65 / 50 / 60 / 130 | 95 / 110 / 75 / 45 / 70 / 95 |
| Total | 480 | 475 | 490 |
| Talents | **Monture** (custom), Armurbaston (Battle Armor), Écran Poudre (Shield Dust, caché) | **Monture** (custom), Pied Véloce (Quick Feet), Querelleur (Scrappy, caché) | **Monture** (custom), Glissade (Swift Swim), Impudence (Moxie, caché) |
| Bonus Monture | +1 Défense | +1 Vitesse | +1 Attaque |
| Pivot | Demi-Tour (U-turn) | **Galop** (custom) | Eau Revoir (Flip Turn) |
| Capture / Exp. | 45 / 170 | 45 / 170 | 45 / 175 |
| EV | Déf +2, Vit +1 | Vit +3 | Att +2, Vit +1 |
| Groupes d'œuf | Terrestre / Insecte | Terrestre / Dragon | Terrestre / Eau 1 |

Stats sacrifiées : l'AtqSpé pour les trois (montures physiques) ; DéfSpé moyenne pour que le bonus Défense de Volkorne reste ciblé. Volkorne est doublement faible à Roche. Dragodinde est le monstre custom le plus rapide. Muldo se distingue de Tortue Bleue (Eau/Combat, 75/115/80/45/65/100) par plus de PV, moins de Vitesse et le type Eau pur.

Autres champs : 50 % femelle, cycles d'œuf 15, bonheur standard (valeurs Bitouf) ; croissance **lente** (élever une monture prend du temps) ; groupe Terrestre commun pour qu'elles se reproduisent entre elles comme dans l'élevage Dofus ; couleurs : Volkorne rouge, Dragodinde marron, Muldo bleu (à ajuster selon les sprites).

## Kit final
| Rôle | Volkorne | Dragodinde | Muldo |
|---|---|---|---|
| Pivot | Demi-Tour (Insecte 70) | Galop (Normal 70) | Eau Revoir (Eau 60) |
| STAB | Bec Vrille (Vol 80) | Façade (Normal 70, 140 sous statut, synergie Pied Véloce) | Aqua-Brèche (Eau 85) |
| 3ᵉ | Atterrissage (soin) | Cavalerie Lourde (Sol 95) | Mâchouille (Ténèbres 80) |
| 4ᵉ | Big Splash (Body Press, frappe avec la Défense) | Danse Lames | Danse Draco |

## Talent custom : Monture
- **En combat** : quand le Pokémon quitte le terrain sans être K.O. (changement, attaque pivot, changement forcé), le Pokémon qui entre à sa place gagne +1 dans la meilleure stat de base de la monture (hors PV ; à égalité, ordre Att, Déf, Vit, AtqSpé, DéfSpé). Pas de bonus après un K.O., comme Vœu Soin.
- **Hors combat** : en tête d'équipe, divise par deux le taux de rencontres sauvages (comme Puanteur).
- Code : `Cmd_switchoutabilities` mémorise la stat dans `battlerState[battler].storedMonture` (`include/battle.h`), consommé dans `DoSwitchInEffectsForBattler` juste après Vœu Soin et Danse Lune (`BattleScript_MontureActivates`). Hors combat : `WildEncounterCheck` (`wild_encounter.c`).

## Capacités custom
| Nom | Type | Cat. | Puiss. | Préc. | PP | Effet | Modèle |
|---|---|---|---|---|---|---|---|
| Galop | Normal | Physique | 70 | 100 | 20 | Frappe (contact) puis le lanceur retourne dans l'équipe | Demi-Tour, `EFFECT_HIT_ESCAPE` (facile) |

Animation : celle de Charge. Avec Querelleur, Galop touche aussi les Spectre.

## Learnsets

### Volkorne
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Picpic (Peck) | Vol | Phys. | 35 |
| 1 | Armure (Harden) | Normal | Statut | – |
| 4 | Sécrétion (String Shot) | Insecte | Statut | – |
| 7 | Taillade (Fury Cutter) | Insecte | Phys. | 40 |
| 10 | Cru-Ailes (Wing Attack) | Vol | Phys. | 60 |
| 13 | Bond (Pounce) | Insecte | Phys. | 50 |
| 16 | Piqûre (Bug Bite) | Insecte | Phys. | 60 |
| 20 | **Demi-Tour** (U-turn) | Insecte | Phys. | 70 |
| 24 | **Atterrissage** (Roost) | Vol | Statut | – |
| 28 | Furie-Bond (Lunge) | Insecte | Phys. | 80 |
| 32 | **Bec Vrille** (Drill Peck) | Vol | Phys. | 80 |
| 36 | Mur de Fer (Iron Defense) | Acier | Statut | – |
| 40 | **Big Splash** (Body Press) | Combat | Phys. | 80 |
| 44 | Vent Arrière (Tailwind) | Vol | Statut | – |
| 50 | Mégacorne (Megahorn) | Insecte | Phys. | 120 |

### Dragodinde
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Vive-Attaque (Quick Attack) | Normal | Phys. | 40 prio+1 |
| 7 | Double Pied (Double Kick) | Combat | Phys. | 30×2 |
| 11 | Écrasement (Stomp) | Normal | Phys. | 65 |
| 15 | Piétisol (Bulldoze) | Sol | Phys. | 60 |
| 19 | **Galop** (custom) | Normal | Phys. | 70 |
| 23 | **Façade** (Facade) | Normal | Phys. | 70 |
| 27 | Plaquage (Body Slam) | Normal | Phys. | 85 |
| 31 | **Danse Lames** (Swords Dance) | Normal | Statut | – |
| 35 | **Cavalerie Lourde** (High Horsepower) | Sol | Phys. | 95 |
| 39 | Relais (Baton Pass) | Normal | Statut | – |
| 43 | Taurogne (Raging Bull) | Normal | Phys. | 90 |
| 48 | Damoclès (Double-Edge) | Normal | Phys. | 120 |

### Muldo
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Aqua-Jet (Aqua Jet) | Eau | Phys. | 40 prio+1 |
| 9 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 13 | **Eau Revoir** (Flip Turn) | Eau | Phys. | 60 |
| 17 | Tranch'Aqua (Aqua Cutter) | Eau | Phys. | 70 |
| 21 | Hurlement (Roar) | Normal | Statut | – |
| 25 | **Mâchouille** (Crunch) | Ténèbres | Phys. | 80 |
| 28 | Danse Pluie (Rain Dance) | Eau | Statut | – |
| 32 | **Aqua-Brèche** (Liquidation) | Eau | Phys. | 85 |
| 36 | **Danse Draco** (Dragon Dance) | Dragon | Statut | – |
| 41 | Hydro-Queue (Aqua Tail) | Eau | Phys. | 90 |
| 47 | Aquatacle (Wave Crash) | Eau | Phys. | 120 |

## CT, CS et tuteurs
| Catégorie | Volkorne | Dragodinde | Muldo |
|---|---|---|---|
| Socle | Toxik, Abri, Repos, Façade, Attraction, Blabla Dodo, Ronflement, Ténacité, Vantardise | idem | idem |
| CS de monture | **Vol** | **Force** | **Surf**, Cascade, Plongée |
| Autres CS | Coupe, Éclate-Roc | Coupe, Éclate-Roc | Éclate-Roc |
| STAB | Aéropique, Taillade (tuteur) | Plaquage, Damoclès, Ultimawashi (tuteurs) | – |
| Défense / utilitaire | Protection, Rune Protect, Provoc, Riposte (tuteur) | Danse Lames (tuteur) | Danse Pluie, Hurlement, Provoc, Tourmente |
| Couverture | Ailes d'Acier, Larcin | Séisme, Queue de Fer, Tomberoche, Éboulement, Larcin | Queue de Fer, Force, Larcin |

Exclusions volontaires :
- Volkorne : Séisme et Tunnel (insecte volant), Danse Lames (il reste défenseur), attaques spéciales.
- Dragodinde : Casse-Brique, Riposte et coups de poing, Vol et Aéropique (elle ne vole pas), Tunnel, Ultralaser.
- Muldo : Laser Glace, Blizzard, Vent Glace, Vibraqua (spéciales ; Surf gardé pour le déplacement), Séisme (pas de profil Eau/Sol), Danse Lames (il a Danse Draco).
- Les trois : Reflet.
