# Famille Ouassingue

> Spectres de boue des marécages de l'île d'Otomaï. Dans Dofus, ils encaissent
> les dégâts à la place d'un allié (lore et éléments des sorts à vérifier).
> — Évolutions : Ouassingue → Tourbasse (niv. 30) → Roissingue (niv. 45).

**État** : validée et intégrée.

## Intention
Archétype : mur mixte (+ soutien en combat duo) · Références : Trépassable
(même double type, mais tank spécial), Hippodocus (mur robuste) · Pourquoi :
un spectre de boue lent qui encaisse des deux côtés, se soigne et use
l'adversaire. Le « j'encaisse pour mon allié » passe par Garde-Ami et Garde
Large plutôt que par une capacité custom. Pour se distinguer de Trépassable :
pas de Sangsue, pas d'Amass'Sable, AtqSpé modeste, dégâts fixes.

## Stades
| | Ouassingue | Tourbasse | Roissingue |
|---|---|---|---|
| Types | Spectre/Sol | Spectre/Sol | Spectre/Sol |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 70 / 45 / 65 / 45 / 55 / 20 | 95 / 60 / 85 / 60 / 80 / 30 | 125 / 70 / 105 / 70 / 105 / 35 |
| Total | 300 | 410 | 510 |
| Talents | Garde-Ami / Absorbe-Eau / caché Moiteur | idem | idem |
| Capture / Exp. | 120 / 64 | 60 / 145 | 45 / 240 |
| EV | 1 PV | 1 PV, 1 Déf | 1 PV, 1 Déf, 1 DéfSpé |

Autres champs : asexué, groupe d'œuf Amorphe, 20 cycles, bonheur standard,
croissance moyenne-lente, couleur marron.

Stats sacrifiées : Vitesse (un amas de boue rampe), Att et AtqSpé modestes
pour rester un mur et non un attaquant.

## Kit final
- **STAB Spectre** : Ombre Nocturne (dégâts = niveau, fiables pour un mur).
- **STAB Sol** : Boue-Bombe (Spé 65, peut baisser la Précision).
- **Soin** : Soin (Recover).
- **Utilitaire** : Onde Folie.

Alternatives : Ball'Ombre, Telluriforce, Châtiment, Malédiction, Garde Large
(duo), Toxik.

Talents : **Garde-Ami** (réduit les dégâts subis par les alliés, combat duo),
**Absorbe-Eau** (le marais boit l'eau : annule la faiblesse Eau), caché
**Moiteur** (empêche Explosion/Destruction).

## Capacités custom
Aucune.

## Learnsets
Socle commun (Ouassingue, repris aux mêmes niveaux par les stades suivants) :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Coud'Boue (Mud-Slap) | Sol | Spé | 20 |
| 1 | Léchouille (Lick) | Spectre | Phy | 30 |
| 5 | Armure (Harden) | Normal | Statut | – |
| 9 | Tourbi-Sable (Sand Tomb) | Sol | Phy | 35 |
| 13 | Ombre Nocturne (Night Shade) | Spectre | Spé | niv. |
| 17 | Tir de Boue (Mud Shot) | Sol | Spé | 55 |
| 21 | Onde Folie (Confuse Ray) | Spectre | Statut | – |
| 25 | Châtiment (Hex) | Spectre | Spé | 65 |
| 29 | Boue-Bombe (Mud Bomb) | Sol | Spé | 65 |
| 33 | Malédiction (Curse) | Spectre | Statut | – |
| 37 | Ocroupi (Muddy Water) | Eau | Spé | 90 |
| 41 | Ball'Ombre (Shadow Ball) | Spectre | Spé | 80 |

Exclusivités :

| Stade | Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|---|
| Ouassingue | 45 | Repos (Rest) | Psy | Statut | – |
| Tourbasse | Évo | Soin (Recover) | Normal | Statut | – |
| Roissingue | Évo | Telluriforce (Earth Power) | Sol | Spé | 90 |
| Roissingue | 1 | Soin (Recover) | Normal | Statut | – |
| Roissingue | 51 | Garde Large (Wide Guard) | Roche | Statut | – |
| Roissingue | 57 | Cœur de Rancœur (Bitter Malice) | Spectre | Spé | 75 |

Soin n'arrive qu'à l'évolution en Tourbasse : un Ouassingue non évolué reçoit
Repos à 45 à la place. Roissingue a Soin au niveau 1 pour ne pas le perdre
(`P_PRE_EVO_MOVES` est à `FALSE`).

## CT, CS et tuteurs
| Attaque | Ouassingue | Tourbasse | Roissingue |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction | ✓ | ✓ | ✓ |
| Mur Lumière, Protection, Rune Protect | ✓ | ✓ | ✓ |
| Provoc, Tourmente | ✓ | ✓ | ✓ |
| Danse Pluie, Tempête de Sable | ✓ | ✓ | ✓ |
| Séisme, Tunnel, Ball'Ombre, Vibraqua, Bombe Beurk | ✓ | ✓ | ✓ |
| Surf, Plongée (CS) | ✓ | ✓ | ✓ |
| Tuteurs : Coud'Boue, Ténacité, Blabla Dodo, Ronflement, Vantardise, Boul'Armure, Roulade, Plaquage, Riposte | ✓ | ✓ | ✓ |
| Hurlement | | ✓ | ✓ |
| Ultralaser | | | ✓ |

Exclusions volontaires : Plénitude (Plénitude + Soin en ferait un setup
sweeper spécial), Explosion (contredit Moiteur), Frappe Atlas (doublon
d'Ombre Nocturne), Lait à Boire (doublon de Soin), Giga-Sangsue (identité de
Trépassable), coups de poing, Force, Éclate-Roc, Tomberoche (pas de bras),
attaques Glace, Électrik et Feu.
