# Légendaires : Solar et Bethel

> Solar (DofusDB #5100, race Calcinés) et Bethel Akarna (#5110, race
> Submergés) sont les boss de la Tour de Solar et de la Tour de Bethel. Ce
> sont des morts-vivants capables de relever d'autres morts. Les sorts de
> Solar suivent la course du soleil (Aube Saine, Démon de Midi, Coucher de
> Soleil, Démons de Minuit) ; Bethel lance des malédictions (Pantang,
> Vindicte), se téléporte (Étoile de Mer) et pose des glyphes. Sans
> évolution. Ils remplacent Groudon et Kyogre.

**État** : validée et intégrée. Solar et Bethel remplacent Groudon et Kyogre
dans le scénario (dialogues, combats de Terra Cave et Marine Cave, cris de
Sootopolis) et hors combat (sprites 32×32 générés depuis le renderer Dofus,
palettes `OBJ_EVENT_PAL_TAG_SOLAR` / `BETHEL` ; les palettes `GROUDON` /
`KYOGRE` servent à leur version endormie, en gris). Ils reprennent les cris,
la musique, la transition et le décor de combat de Groudon et Kyogre.
Restent à Groudon et Kyogre : l'intro du jeu et la cinématique de Rayquaza à
Sootopolis (grands sprites dessinés).

## Intention
Archétype : légendaire de météo, attaquant · Références : Groudon, Kyogre ·
Pourquoi : ils reprennent les rôles de Groudon (physique, Sécheresse) et de
Kyogre (spécial, Crachin), pour que la scène de Sootopolis fonctionne telle
quelle. Dans Dofus, Solar a deux fois plus de PV que Bethel et de fortes
résistances ; Bethel n'en a aucune : Solar est donc un tank lent, Bethel un
lanceur rapide et plus fragile.

## Stades
| | Solar | Bethel |
|---|---|---|
| Types | Feu | Eau |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 115 / 150 / 130 / 85 / 105 / 85 | 95 / 80 / 90 / 155 / 125 / 125 |
| Total | 670 | 670 |
| Talents | Sécheresse (Drought) | Crachin (Drizzle) |
| Capture / Exp. | 3 / 335 | 3 / 335 |
| EV | 3 Att | 3 AtqSpé |
| Taille / poids | 2,5 m / 400 kg | 2,2 m / 180 kg |

Comparaison : Groudon 100/150/140/100/90/90, Kyogre 100/100/90/150/140/90,
Regigigas et Miraidon (profils les plus proches). Aucun monstre Osatopia
proche (les autres plafonnent vers 530).

Valeurs reprises de Groudon : asexués, pas d'œufs, 120 cycles, bonheur 0,
croissance lente.

## Kit final
**Solar** : Solar Flare (Feu, 120, les deux adversaires) · Lame en Peine
(Feu, 90, vol de vie) · Séisme (couverture Roche, Feu, Électrik) ·
Malédiction (+Att +Déf −Vit, idéal pour un tank lent). Options : Boutefeu,
Feu Sacré, Lame de Roc, Close Combat, Danse Lames, Necromancy.

**Bethel** : Onde Originelle (Eau, 110, les deux adversaires) · Pantang
(Eau, 80, −1 DéfSpé) · Fatal-Foudre (ne rate pas sous la pluie, rappelle ses
sorts Air) · Necromancy. Options : Hydrocanon, Giclédo, Laser Glace,
Ball'Ombre, Plénitude, Requiem.

## Capacités custom
| Conception | En jeu | Type | Cat. | Puiss. | Préc. | PP | Effet | Modèle |
|---|---|---|---|---|---|---|---|---|
| Nécromancie | Necromancy | Spectre | Statut | — | — | 1 | Ranime un Pokémon K.O. de l'équipe avec la moitié de ses PV | Second Souffle (`EFFECT_REVIVAL_BLESSING`) |
| Éruption Solaire | Solar Flare | Feu | Physique | 120 | 85 | 5 | Touche les deux adversaires | Lame Pangéenne (`EFFECT_HIT`, cible les deux) |
| Pantang | Pantang (Dofus) | Eau | Spéciale | 80 | 100 | 10 | −1 DéfSpé à coup sûr | Luminocrash (−2 au lieu de −1) |

Nécromancie échoue sans allié K.O. : un Solar ou un Bethel sauvage seul ne
peut pas s'en servir. Elle est exclue du test IA « can use all moves »
(comme Second Souffle) ; Pantang est dans la liste de Sans Limite.

## Learnsets
**Solar**
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Grimace (Scary Face) | Normal | Statut | — |
| 1 | Nitrocharge (Flame Charge) | Feu | Phys. | 50 |
| 1 | Malédiction (Curse) | Spectre | Statut | — |
| 1 | Feu Follet (Will-O-Wisp) | Feu | Statut | — |
| 1 | Éruption Solaire (Solar Flare) | Feu | Phys. | 120 |
| 9 | Lame en Peine (Bitter Blade) | Feu | Phys. | 90 |
| 18 | Danse Lames (Swords Dance) | Normal | Statut | — |
| 27 | Séisme (Earthquake) | Sol | Phys. | 100 |
| 36 | Lame de Roc (Stone Edge) | Roche | Phys. | 100 |
| 45 | Nécromancie (Necromancy) | Spectre | Statut | — |
| 54 | Lien du Destin (Destiny Bond) | Spectre | Statut | — |
| 72 | Feu Sacré (Sacred Fire) | Feu | Phys. | 100 |
| 81 | Close Combat | Combat | Phys. | 120 |
| 90 | Boutefeu (Flare Blitz) | Feu | Phys. | 120 |

**Bethel**
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Grimace (Scary Face) | Normal | Statut | — |
| 1 | Vibraqua (Water Pulse) | Eau | Spé. | 60 |
| 1 | Châtiment (Hex) | Spectre | Spé. | 65 |
| 1 | Onde Originelle (Origin Pulse) | Eau | Spé. | 110 |
| 9 | Pantang | Eau | Spé. | 80 |
| 18 | Plénitude (Calm Mind) | Psy | Statut | — |
| 27 | Ball'Ombre (Shadow Ball) | Spectre | Spé. | 80 |
| 36 | Fatal-Foudre (Thunder) | Électrik | Spé. | 110 |
| 45 | Nécromancie (Necromancy) | Spectre | Statut | — |
| 54 | Requiem (Perish Song) | Normal | Statut | — |
| 72 | Hydrocanon (Hydro Pump) | Eau | Spé. | 110 |
| 81 | Laser Glace (Ice Beam) | Glace | Spé. | 90 |
| 90 | Giclédo (Water Spout) | Eau | Spé. | 150 |

## CT, CS et tuteurs
| | Solar | Bethel |
|---|---|---|
| Socle commun | Toxik, Abri, Repos, Façade, Ultralaser, Reflet, Vantardise, Ténacité, Blabla Dodo, Ronflement, Hurlement, Provoc, Tourmente, Attraction, Larcin | idem |
| STAB | Lance-Flammes, Déflagration, Surchauffe, Zénith, Poing Feu | Vibraqua, Surf, Cascade, Plongée, Danse Pluie |
| Couverture | Séisme, Tunnel, Casse-Brique, Gonflette, Danse Lames, Éboulement, Tomberoche, Mitra-Poing, Taillade, Faux-Chage, Force, Coupe, Éclate-Roc, Plaquage, Damoclès | Laser Glace, Blizzard, Vent Glace, Tonnerre, Fatal-Foudre, Onde de Choc, Cage Éclair, Ball'Ombre, Psyko, Plénitude, Dévorêve, Mur Lumière, Protection, Rune Protect, Échange |

Exclusions volontaires : Lance-Soleil, Électrik et Plante pour Solar (Bethel
doit rester son contre), Surf et les CS aquatiques pour Solar, coups de
poing et attaques physiques de contact pour Bethel.
