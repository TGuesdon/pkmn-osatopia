# Famille Gamino

> Inspirés du minotaure grec, Gamino et Minotot hantent le Labyrinthe du Minotoror. Minotot, magicien rusé, en est le gardien : il transforme ses ennemis en Tofus pour les gêner et veille sur le Dofus Pourpre, qui augmente ses dégâts (à vérifier : éléments des sorts, zone exacte, lien Gamino → Minotot). — Évolutions : Gamino (`SPECIES_GAMINO`) → Minotot (`SPECIES_MINOTOT`) au niveau 45.

**État** : validée et intégrée

## Intention
Archétype : perturbateur (secondaire : tank offensif spécial) · Références : Hypnomade (perturbateur Psy, Entrave et Hypnose), Gallame (bipède Psy/Combat), M. Glaquette et Porygon2 (profil équilibré ~520) · Pourquoi : un mage gardien de fin de partie qui entrave l'adversaire (Entrave, Provoc, Anti-Soin, Regard Noir, Octoprise, Tofuïsation) puis frappe plus fort grâce à son talent caché **Pourpre**. Son combo signature : Tofuïsation change la cible en Vol pur, puis Tonnerre la frappe en super efficace.

## Stades
| | Gamino | Minotot |
|---|---|---|
| Types | Psy | Psy / Combat |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 65 / 55 / 60 / 80 / 60 / 50 | 90 / 85 / 85 / 110 / 90 / 65 |
| Total | 370 | 525 |
| Talents | Synchro (Synchronize), Attention (Inner Focus), **Pourpre** (custom, caché) | idem |
| Capture / Exp. | 60 / 140 | 45 / 250 |
| EV | AtqSpé +1 | AtqSpé +2, DéfSpé +1 |
| Groupes d'œuf | Humanoïde | Humanoïde |

Stat sacrifiée : la Vitesse (65). C'est un gardien qui encaisse, entrave, puis frappe ; il ne nettoie pas en premier. Rien sous 85 chez Minotot, pour rester équilibré, avec une Att correcte pour les coups de corne. Total légèrement au-dessus de la fourchette « 2 stades tardif » : c'est une récompense de fin de partie. Se distingue de Crachefoux (Feu, plus rapide, moins solide) et de Grenn (Combat physique), ainsi que des autres Psy : Voracle (rapide et fragile), Ronronchon et Bloqueuse (murs spéciaux).

Autres champs : 50 % femelle, cycles d'œuf 15, bonheur standard (valeurs Bitouf) ; croissance **lente** (choix de l'utilisateur) ; groupe d'œuf Humanoïde ; couleur marron.

## Kit final
| Rôle | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Signature, entrave | **Tofuïsation** (custom) | Psy | Statut | – |
| STAB Psy | Psyko (Psychic) ou Dissonance Psy (Psychic Noise) | Psy | Spé. | 90 / 75 |
| STAB Combat | Aurasphère (Aura Sphere) | Combat | Spé. | 80 |
| Couverture du combo Tofu | Tonnerre (Thunderbolt) | Électrik | Spé. | 90 |

Variantes de perturbateur : Entrave, Provoc, Anti-Soin, Tourmente, Cage Éclair, Regard Noir, Octoprise, Plénitude (boost).

## Talent custom : Pourpre
- Effet : les attaques du Pokémon infligent 30 % de dégâts en plus (×1,3) à une cible **entravée**.
- Une cible est entravée si elle a : un statut majeur ; au moins une stat baissée ; Entrave, Encore, Provoc, Embargo, Anti-Soin (y compris Dissonance Psy) ou Tourmente ; ou un type différent de celui de son espèce (Tofuïsation, Détrempage, Halloween…).
- Description : « Frappe fort les cibles entravées. »
- Code : `ABILITY_POURPRE`. Modificateur `GetPourpreModifier` / `IsBattlerHindered` dans le calcul final des dégâts (`battle_util.c`), donc aussi pris en compte par l'IA dans ses estimations de dégâts. L'IA favorise aussi les capacités de type `EFFECT_SOAK` quand elle a Pourpre (`battle_ai_main.c`).

## Capacités custom
### Tofuïsation
| Type | Cat. | Puiss. | Préc. | PP | Effet |
|---|---|---|---|---|---|
| Psy | Statut | – | 100 | 10 | La cible devient de type Vol pur (« changée en Tofu »). |

- Attaque existante la plus proche : Poudre Magique (Magic Powder) / Détrempage (Soak), `EFFECT_SOAK`, avec `.argument = { .type = TYPE_FLYING }`.
- Échoue si la cible est déjà Vol pur ou téracristallisée. Renvoyée par Reflet Magik. Pas une poudre (les Plante y sont sensibles).
- Animation : celle de Poudre Magique.
- Difficulté : facile. Code : `MOVE_TOFUISATION` (`moves.h`, `moves_info.h`).

## Learnsets
### Gamino
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Choc Mental (Confusion) | Psy | Spé. | 50 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Entrave (Disable) | Normal | Statut | – |
| 9 | Éclair (Thunder Shock) | Électrik | Spé. | 40 |
| 13 | Koud'Korne (Horn Attack) | Normal | Phys. | 65 |
| 17 | Rafale Psy (Psybeam) | Psy | Spé. | 65 |
| 21 | Provoc (Taunt) | Ténèbres | Statut | – |
| 25 | Regard Noir (Mean Look) | Normal | Statut | – |
| 29 | Dissonance Psy (Psychic Noise) | Psy | Spé. | 75 |
| 33 | Anti-Soin (Heal Block) | Psy | Statut | – |
| 37 | Plénitude (Calm Mind) | Psy | Statut | – |
| 41 | Psyko (Psychic) | Psy | Spé. | 90 |

### Minotot
Reprend toutes les attaques de Gamino aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Aurasphère (Aura Sphere) | Combat | Spé. | 80 |
| 50 | **Tofuïsation** (custom) | Psy | Statut | – |
| 54 | Tonnerre (Thunderbolt) | Électrik | Spé. | 90 |
| 58 | Octoprise (Octolock) | Combat | Statut | – |

Tofuïsation est réservée à Minotot : il faut évoluer pour obtenir la signature. Écarts volontaires avec Voracle (pas d'Extrasenseur, Machination ni Prescience) et Ronronchon (pas de Distorsion).

## CT, CS et tuteurs
| Attaque | Gamino | Minotot |
|---|---|---|
| Toxik, Abri, Repos, Reflet, Attraction, Ténacité, Ronflement, Blabla Dodo, Vantardise, Boost, Façade | ✓ | ✓ |
| Psyko, Plénitude, Mur Lumière, Protection, Échange | ✓ | ✓ |
| Provoc, Tourmente, Cage Éclair | ✓ | ✓ |
| Tonnerre | ✓ | ✓ |
| Dévorêve, Métronome, Ball'Ombre | ✓ | ✓ |
| Force, Éclate-Roc | ✓ | ✓ |
| Casse-Brique, Frappe Atlas, Séisme, Ultralaser | – | ✓ |

Exclusions volontaires : Fatal-Foudre, Onde de Choc et Poing Éclair (seul Tonnerre comme attaque Électrik) ; Laser Glace et Blizzard (ils frapperaient aussi un Tofuïsé en super efficace, le combo reste propre à Tonnerre) ; coups de poing (Mitra-Poing, Dynamo-Poing, Poing Feu, Poing Glace) : c'est un mage, pas un boxeur ; Lance-Flammes, Bomb-Beurk (couvertures hors thème).
