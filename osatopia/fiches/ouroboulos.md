# Famille Ouroboulos

> Scorpion cuirassé qui renvoie une partie des dégâts qu'on lui inflige.
> *(Lore donné par l'utilisateur ; éléments des sorts et zone à vérifier.)*
> Évolutions : Ouroboulos → Mantiscore (niv. 32).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies : `PERCENT_FEMALE(50)`, `.eggCycles = 20`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` et `EGG_GROUP_BUG`, comme la famille
Scorpique ; couleur `BODY_COLOR_BROWN` (conservée du placeholder).

## Intention

Archétype : **mur physique**, avec **punisseur de contact** en secondaire.
Mantiscore encaisse, fait payer chaque contact (Peau Dure, Blockhaus,
Pico-Défense), renvoie les coups (Riposte, Vendetta, Fulmifer), se renforce
avec Gonflette et frappe avec Big Splash, qui calcule ses dégâts sur la
Défense. Pas de soin : il tient par la Défense et punit, il ne se régénère pas.

Références : **Prédastérie** (mur Poison, Blockhaus), **Noacier** (punit le
contact avec Épine de Fer tout en frappant), **Coatox** (même double type, mais
offensif : contre-modèle pour les stats).

Combat/Poison aux deux stades, pour ne pas doubler Scorpique/Scordion
(Sol/Poison). Faiblesses : Psy ×4, Sol, Vol. Résistances : Insecte ×4, Combat,
Poison, Roche, Ténèbres, Plante.

## Stades

| | Ouroboulos | Mantiscore |
|---|---|---|
| Types | Combat/Poison | Combat/Poison |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 65 / 55 / 75 / 30 / 50 / 40 | 100 / 85 / 115 / 45 / 80 / 65 |
| Total | 315 | 490 |
| Talents | Peau Dure / Dépôt Toxique / caché Cruauté | idem |
| Capture / Exp. | 120 / 64 | 45 / 175 |
| EV | Déf 1 | Déf 2 |

Comparaison : Gigansel 100/100/130/45/90/35, Crabaraque 70/105/125/65/75/45,
Wo Wabbit (custom) 110/75/110/45/90/70, Scordion 75/100/110/40/75/85.
AtqSpé et Vitesse sacrifiées : il encaisse d'abord, et la lenteur sert Vendetta
et Riposte.

Talents :
- **Peau Dure** (Rough Skin) : l'attaquant perd 1/8 de ses PV à chaque contact.
- **Dépôt Toxique** (Toxic Debris) : un coup physique reçu pose des Pics Toxik
  chez l'adversaire.
- **Cruauté** (Merciless, caché) : coups critiques garantis sur une cible
  empoisonnée (Blockhaus, Griffes Funestes, Toxik).

## Kit final

| Emplacement | Attaque | Alternatives dans le learnset |
|---|---|---|
| Boost | Gonflette (Bulk Up) | — |
| STAB Combat | Big Splash (Body Press, 80, sur la Déf) | Marto-Poing, Casse-Brique, Vendetta |
| STAB Poison | Griffes Funestes (Dire Claw, 80) | Crochet Venin, Toxik |
| Renvoi | Blockhaus (Baneful Bunker) | Pico-Défense, Riposte, Fulmifer |

## Capacités custom

Aucune.

## Learnsets

### Ouroboulos

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Armure (Harden) | Normal | Statut | — |
| 1 | Éclate-Roc (Rock Smash) | Combat | Physique | 40 |
| 4 | Gaz Toxik (Poison Gas) | Poison | Statut | — |
| 8 | Toupie Éclat (Mortal Spin) | Poison | Physique | 30 |
| 12 | Vendetta (Revenge) | Combat | Physique | 60, prio −4 |
| 16 | Crochet Venin (Poison Fang) | Poison | Physique | 50 |
| 20 | Blockhaus (Baneful Bunker) | Poison | Statut | prio +4 |
| 24 | Casse-Brique (Brick Break) | Combat | Physique | 75 |
| 28 | Griffes Funestes (Dire Claw) | Poison | Physique | 80 |
| 32 | Riposte (Counter) | Combat | Physique | renvoi |
| 36 | Gonflette (Bulk Up) | Combat | Statut | — |
| 40 | Toxik (Toxic) | Poison | Statut | — |
| 44 | Pico-Défense (Spiky Shield) | Plante | Statut | prio +4 |
| 48 | Big Splash (Body Press) | Combat | Physique | 80 |

### Mantiscore

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Big Splash (Body Press) | Combat | Physique | 80 |
| 1 | Armure (Harden) | Normal | Statut | — |
| 1 | Éclate-Roc (Rock Smash) | Combat | Physique | 40 |
| 4 | Gaz Toxik (Poison Gas) | Poison | Statut | — |
| 8 | Toupie Éclat (Mortal Spin) | Poison | Physique | 30 |
| 12 | Vendetta (Revenge) | Combat | Physique | 60, prio −4 |
| 16 | Crochet Venin (Poison Fang) | Poison | Physique | 50 |
| 20 | Blockhaus (Baneful Bunker) | Poison | Statut | prio +4 |
| 24 | Casse-Brique (Brick Break) | Combat | Physique | 75 |
| 28 | Griffes Funestes (Dire Claw) | Poison | Physique | 80 |
| 32 | Riposte (Counter) | Combat | Physique | renvoi |
| 35 | Gonflette (Bulk Up) | Combat | Statut | — |
| 39 | Toxik (Toxic) | Poison | Statut | — |
| 43 | Pico-Défense (Spiky Shield) | Plante | Statut | prio +4 |
| 47 | Fulmifer (Metal Burst) | Acier | Physique | renvoi |
| 52 | Marto-Poing (Hammer Arm) | Combat | Physique | 100 |

Temporisation : Big Splash arrive à l'évolution (niv. 32), contre 48 si
l'évolution est bloquée.

## CT, CS et tuteurs

| Attaque | Ouroboulos | Mantiscore |
|---|---|---|
| Toxik, Gonflette, Abri, Casse-Brique, Façade, Ténacité, Blabla Dodo, Ronflement, Vantardise, Provoc, Attraction, Reflet, Hurlement | ✓ | ✓ |
| Éclate-Roc, Force, Tunnel, Tomberoche, Éboulement, Frappe Atlas, Riposte, Mitra-Poing, Dynamo-Poing | ✓ | ✓ |
| Queue de Fer (couverture Fée), Larcin (couverture Psy) | ✓ | ✓ |
| Séisme | — | ✓ |

Exclusions volontaires : Repos (pas de soin), Danse-Lames (en ferait un
attaquant), Poing-Glace / Poing de Feu / Poing-Éclair (pas de sens pour lui),
Ultralaser, Méga-Poing et Ultimapoing, toutes les CT spéciales.
