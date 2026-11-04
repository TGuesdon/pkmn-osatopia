# Famille Skyboufton

> Bouftous célestes dont la laine génère de l'électricité.
> *(Lore donné par l'utilisateur ; existence et sorts Dofus à vérifier.)*
> Évolutions : Skyboufton → Skybouftou (niv. 18) → Dieubouftou (niv. 38).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies : `PERCENT_FEMALE(50)`, `.eggCycles = 15`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` (comme Pharamp),
`EGG_GROUP_FIELD` (comme le Bouftou), `BODY_COLOR_WHITE` (la laine).

## Intention

Archétype : **tank offensif spécial**, avec **soutien** en secondaire.
Dieubouftou encaisse, se renforce avec Plénitude ou Cotogarde, se soigne avec
Lait à Boire et frappe avec deux STAB spéciaux (Tonnerre, Mégaphone). C'est la
version spéciale et céleste du Bouftou, qui reste 100 % physique.

Référence : **Pharamp** (mouton électrique lent, AtqSpé haute, Cotogarde,
Mur Lumière). Différences : plus de PV, moins d'Att et de Vit, un STAB Normal
spécial, pas de coups de poing.

Normal/Électrik aux trois stades. Avec Lévitation, la seule faiblesse est
**Combat** (immunités Spectre et Sol ; résistances Vol, Acier, Électrik) :
total et Vitesse volontairement un peu sous Pharamp pour compenser.

Les trois talents donnent trois profils :
- **Lévitation** : immunité Sol, mais ne profite pas d'un champ électrifié.
- **Boule de Poils** : contact divisé par 2, mais devient faible au Feu.
- **Créa-Élec** (caché) : pose un champ électrifié, reste au sol (faible Sol)
  et en profite pleinement (+30 % Électrik, Monte-Tension doublée).

## Stades

| | Skyboufton | Skybouftou | Dieubouftou |
|---|---|---|---|
| Types | Normal/Électrik | Normal/Électrik | Normal/Électrik |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 60 / 35 / 45 / 60 / 45 / 35 | 80 / 50 / 60 / 80 / 60 / 45 | 100 / 60 / 85 / 110 / 90 / 50 |
| Total | 280 | 375 | 495 |
| Talents | Lévitation / Boule de Poils / caché Créa-Élec | idem | idem |
| Capture / Exp. | 190 / 58 | 100 / 128 | 45 / 240 |
| EV | AtqSpé 1 | AtqSpé 2 | AtqSpé 2, PV 1 |

Comparaison : Wattouat 280, Lainergie 365, Pharamp 510, Ampibidou 495 ;
custom proches Obsidiantre (510) et Ronronchon (480), de types et rôles
différents.

## Kit final

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB Électrik | Tonnerre (90) | Coup d'Jus, Fatal-Foudre, Monte-Tension |
| STAB Normal | Mégaphone (90) | Triplattaque, Ultralaser (CT) |
| Boost / soin | Plénitude | Cotogarde, Lait à Boire, Chargeur |
| Couverture | Psyko (90, contre Combat) | Mur Lumière, Cage Éclair |

## Capacités custom

Aucune.

## Learnsets

Attaques de base communes aux trois stades, aux mêmes niveaux.
`P_PRE_EVO_MOVES` étant à `FALSE`, Tonnerre et Psyko par niveau sont réservés
à Dieubouftou.

### Skyboufton

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phy | 40 |
| 1 | Rugissement (Growl) | Normal | Statut | – |
| 4 | Éclair (Thunder Shock) | Électrik | Spé | 40 |
| 8 | Cage Éclair (Thunder Wave) | Électrik | Statut | – |
| 11 | Écho (Echoed Voice) | Normal | Spé | 40 |
| 14 | Spore Coton (Cotton Spore) | Plante | Statut | – |
| 17 | Rayon Chargé (Charge Beam) | Électrik | Spé | 50 |
| 21 | Boule Élek (Electro Ball) | Électrik | Spé | var. |
| 25 | Monte-Tension (Rising Voltage) | Électrik | Spé | 70 |
| 29 | Triplattaque (Tri Attack) | Normal | Spé | 80 |
| 33 | Coup d'Jus (Discharge) | Électrik | Spé | 80 |

### Skybouftou

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Chargeur (Charge) | Électrik | Statut | – |
| 1–17 | attaques de base de Skyboufton | | | |
| 21 | Boule Élek (Electro Ball) | Électrik | Spé | var. |
| 25 | Monte-Tension (Rising Voltage) | Électrik | Spé | 70 |
| 28 | Triplattaque (Tri Attack) | Normal | Spé | 80 |
| 31 | Lait à Boire (Milk Drink) | Normal | Statut | – |
| 34 | Coup d'Jus (Discharge) | Électrik | Spé | 80 |
| 37 | Mur Lumière (Light Screen) | Psy | Statut | – |
| 42 | Mégaphone (Hyper Voice) | Normal | Spé | 90 |
| 47 | Plénitude (Calm Mind) | Psy | Statut | – |
| 52 | Cotogarde (Cotton Guard) | Plante | Statut | – |
| 57 | Fatal-Foudre (Thunder) | Électrik | Spé | 110 |

### Dieubouftou

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Tonnerre (Thunderbolt) | Électrik | Spé | 90 |
| 1 | Chargeur (Charge) | Électrik | Statut | – |
| 1–37 | comme Skybouftou | | | |
| 41 | Mégaphone (Hyper Voice) | Normal | Spé | 90 |
| 44 | Psyko (Psychic) | Psy | Spé | 90 |
| 47 | Plénitude (Calm Mind) | Psy | Statut | – |
| 51 | Cotogarde (Cotton Guard) | Plante | Statut | – |
| 56 | Fatal-Foudre (Thunder) | Électrik | Spé | 110 |

## CT, CS et tuteurs

| Attaque | Source | Skyboufton | Skybouftou | Dieubouftou |
|---|---|---|---|---|
| Toxik, Abri, Repos, Reflet, Façade, Attraction | CT | ✔ | ✔ | ✔ |
| Mur Lumière, Protection, Rune Protect, Danse Pluie | CT | ✔ | ✔ | ✔ |
| Onde de Choc, Fatal-Foudre, Queue de Fer, Hurlement | CT | ✔ | ✔ | ✔ |
| Blabla Dodo, Ronflement, Ténacité, Vantardise | Tuteur | ✔ | ✔ | ✔ |
| Cage Éclair, Météores, Plaquage, Boul'Armure, Roulade | Tuteur | ✔ | ✔ | ✔ |
| Force, Éclate-Roc | CS | ✔ | ✔ | ✔ |
| Plénitude | CT | – | ✔ | ✔ |
| Damoclès, Boost | Tuteur | – | ✔ | ✔ |
| Tonnerre, Psyko, Ultralaser, Échange | CT | – | – | ✔ |
| Vol | CS | – | – | ✔ |

Exclusions volontaires : tous les poings et Ultimawashi (c'est un mouton),
Séisme, Tunnel et Tempête de Sable (créature céleste), Laser Glace et
Lance-Flammes (couverture recentrée sur Électrik/Normal/Psy), Tonnerre et Psyko
avant le stade final (temporisation du learnset).
