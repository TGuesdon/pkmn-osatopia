# Légendaire : Ilyzaelle

> Ilyzaelle (DofusDB #4967, race Brûlâmes) est la gardienne du royaume des
> morts. Dans Dofus, son combat se joue en deux phases : un spectre vert
> corrompu, puis sa vraie forme dorée (sort « Vers les ténèbres »). Ses sorts
> sont Feu : Hantâme (téléportation, dégâts de zone, Érosion) et Lance de
> l'effroi (dégâts, état Pacifiste). Sans évolution. Elle remplace Rayquaza
> et commande les morts-vivants Solar et Bethel.

**État** : validée et intégrée. Ilyzaelle remplace Rayquaza dans le scénario
(dialogues, combat du Pilier Céleste, cris de Sootopolis) et hors combat
(sprite 64×64 de la phase verte, palette `OBJ_EVENT_PAL_TAG_ILYZAELLE`). Elle
reprend la musique, la transition et le décor de combat de Rayquaza, et son
cri. Restent à Rayquaza : l'intro du jeu et la cinématique de Sootopolis
(grands sprites dessinés).

## Intention
Archétype : légendaire attaquant mixte, boss en deux phases · Références :
Rayquaza (rôle et stats), Zygarde (Power Construct) · Pourquoi : elle domine
Solar et Bethel comme Rayquaza dominait Groudon et Kyogre. Spectre/Acier :
gardienne des morts en armure, avec une lance.

## Stades
| | Ilyzaelle (phase 1, verte) | Ilyzaelle (phase 2, dorée) |
|---|---|---|
| Constante | `SPECIES_ILYZAELLE` | `SPECIES_ILYZAELLE_DOREE` (combat uniquement) |
| Types | Spectre/Acier | Spectre/Acier |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 100 / 145 / 95 / 145 / 95 / 100 | 160 / 155 / 105 / 155 / 105 / 100 |
| Total | 680 | 780 |
| Talent | Reawakening | Reawakening |
| Capture / Exp. | 3 / 340 | 3 / 340 |
| EV | 2 Att, 1 AtqSpé | idem |
| Taille / poids | 2,1 m / 150 kg, « Soul Keeper » | idem |

Comparaison : Rayquaza 105/150/90/150/90/95 (680), Dialga
100/120/120/150/100/90 (680), Méga-Rayquaza (780).

Valeurs reprises de Solar et Bethel : asexuée, pas d'œufs, 120 cycles,
bonheur 0, croissance lente.

## Talent custom
| Conception | En jeu | Effet | Modèle |
|---|---|---|---|
| Réveil | Reawakening (« Awakens when weakened. ») | En fin de tour, sous 50 % PV, prend sa forme dorée ; les PV max augmentent et elle gagne la différence. Revient en forme verte après le combat ou au K.O. | Power Construct (Zygarde) |

Messages : « X's soul is stirring! » puis « X revealed its true form! »,
avec l'animation générique de changement de forme. Comme Power Construct, le
talent ne peut être ni copié, ni échangé, ni supprimé.

Synergie voulue : Malédiction (version Spectre) coûte la moitié des PV max,
ce qui déclenche la transformation à la fin du tour.

## Kit final
Lance de l'effroi (STAB Spectre physique) · Choc Météore (STAB Acier) ·
Hantâme (Feu, élément Dofus) · Malédiction. Options : Esprit Frappeur,
Revenant, Métalaser, Necromancy, Machination, Danse Lames.

## Capacités custom
| Conception | En jeu | Type | Cat. | Puiss. | Préc. | PP | Effet | Modèle |
|---|---|---|---|---|---|---|---|---|
| Lance de l'effroi | Dread Lance | Spectre | Physique | 90 | 100 | 10 | 30 % d'apeurer (contact) | Tête de Fer |
| Hantâme | Soul Haunt | Feu | Spéciale | 80 | 100 | 10 | Touche les deux adversaires ; ils ne peuvent plus se soigner pendant 2 tours | Dissonance Psy |

Les deux sont dans la liste de Sans Limite (`test/battle/ability/sheer_force.c`).

## Learnset
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Grimace (Scary Face) | Normal | Statut | — |
| 1 | Ombre Portée (Shadow Sneak) | Spectre | Phys. | 40 |
| 1 | Griffe Acier (Metal Claw) | Acier | Phys. | 50 |
| 1 | Feu Follet (Will-O-Wisp) | Feu | Statut | — |
| 1 | Lance de l'effroi (Dread Lance) | Spectre | Phys. | 90 |
| 9 | Hantâme (Soul Haunt) | Feu | Spé. | 80 |
| 18 | Malédiction (Curse) | Spectre | Statut | — |
| 27 | Choc Météore (Sunsteel Strike) | Acier | Phys. | 100 |
| 36 | Ball'Ombre (Shadow Ball) | Spectre | Spé. | 80 |
| 45 | Nécromancie (Necromancy) | Spectre | Statut | — |
| 54 | Machination (Nasty Plot) | Ténèbres | Statut | — |
| 63 | Hommage Posthume (Last Respects) | Spectre | Phys. | 50 |
| 72 | Revenant (Shadow Force) | Spectre | Phys. | 120 |
| 81 | Métalaser (Steel Beam) | Acier | Spé. | 140 |
| 90 | Déflagration (Fire Blast) | Feu | Spé. | 110 |

Les deux formes partagent ce learnset.

## CT, CS et tuteurs
| Groupe | Attaques |
|---|---|
| Socle commun | Toxik, Abri, Repos, Façade, Ultralaser, Reflet, Vantardise, Ténacité, Blabla Dodo, Ronflement, Hurlement, Provoc, Tourmente, Attraction, Larcin |
| STAB et Feu | Ball'Ombre, Queue de Fer, Ailes d'Acier, Lance-Flammes, Déflagration, Surchauffe, Zénith |
| Couverture | Danse Lames, Gonflette, Plénitude, Casse-Brique, Coupe, Taillade, Faux-Chage, Aéropique, Dévorêve, Mur Lumière, Protection, Rune Protect |

Exclusions volontaires : Eau, Électrik, Glace et Sol (Bethel et ses
faiblesses restent des contres).

## Sprites
- Phase 1 : rendu Dofus (look `{4139}`), face direction 3, dos direction 7,
  taille énorme. Le haut de la lance est coupé dans les sources pour que le
  corps remplisse le cadre.
- Phase 2 : face tirée d'un rendu Dofus de la forme dorée fourni par
  l'utilisateur (retourné) ; dos = dos vert recoloré en or (dégradé).
- Hors combat : 64×64 depuis la direction 1, cinq images identiques à un
  pixel près (endormie, éveillée, cri, normale, envol) dans
  `rayquaza_cutscene.png`, et `rayquaza_still.png`.
