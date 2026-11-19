# Trio des gardiens : Croqueleur, Ougah et Grolloum

> Trois boss de donjon Dofus qui remplacent les Regis. **Croqueleur**
> (DofusDB #5664, race Croquants, niv. 130) est un golem de chocolat qui garde
> la Croquanterie : il attire ses proies (Attraction gourmande) puis les
> repousse d'un coup des quatre éléments (Total Impwâkt). **Ougah** (#1159,
> race Fungus, niv. 180) est l'idole géante des Fungus : il gagne en puissance
> quand on le frappe (Bizarrerie), devient critique (Spore Hanchambre), se
> soigne au hasard et invoque des champignons. **Grolloum** (#2942, Gobelins de
> Sakaï, niv. 190) est un gobelin géant à l'aura glacée qui vole la vie à
> l'Eau (Banquise), échange de place (Frimas) et relève le dernier allié mort
> (Cycle). Sans évolution.

**État** : validée et intégrée. Croqueleur remplace Regirock (`DesertRuins`),
Ougah remplace Registeel (`AncientTomb`) et Grolloum remplace Regice
(`IslandCave`), au niveau 40. Les énigmes en braille, les drapeaux, la musique
et les transitions Regi ne changent pas. Les trois reprennent les cris des
Regis. Hors combat, chacun a son sprite 32×32 tiré du rendu Dofus (face,
direction 3) et sa palette (`OBJ_EVENT_PAL_TAG_CROQUELEUR` / `OUGAH` /
`GROLLOUM`), à la place du sprite `regi.png` commun. Les poupées et la Battle
Frontier gardent les Regis.

## Intention
Archétype : légendaires de donjon, profils libres d'après Dofus · Références :
Regirock / Registeel / Regice pour la place dans le jeu, Blizzeval et
Épine-de-Fer (Croqueleur), Fongus-Furie et Dinglu (Ougah), Ire-Foudre et
Kaimorse (Grolloum) pour les stats · Pourquoi :
- Croqueleur n'a que 2 PM dans Dofus et frappe au corps à corps : cogneur
  lent et solide.
- Ougah (12 000 PV, bonnes résistances) devient plus fort quand on le frappe :
  mur qui contre-attaque grâce à Courroupace.
- Grolloum (15 000 PV, sorts Eau et Feu, vol de vie) : attaquant spécial
  très endurant. Glace/Ténèbres le rend quadruple faible au Combat, donc à
  Croqueleur.

`GROWTH_SLOW` (comme les Regis).

## Stades
| | Croqueleur | Ougah | Grolloum |
|---|---|---|---|
| Types | Roche/Combat | Plante/Roche | Glace/Ténèbres |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 105 / 140 / 140 / 55 / 95 / 45 | 120 / 115 / 120 / 70 / 110 / 45 | 125 / 80 / 85 / 120 / 100 / 70 |
| Total | 580 | 580 | 580 |
| Talents | Poing de Fer (Iron Fist) / Fermeté (Sturdy) · caché : Piège Sable (Arena Trap) | Courroupace (Anger Shell) / Pose Spore (Effect Spore) · caché : Colérique (Anger Point) | Isograisse (Thick Fat) / Pression (Pressure) · caché : Corps Gel (Ice Body) |
| Capture / Exp. | 3 / 290 | 3 / 290 | 3 / 290 |
| EV | 2 Att, 1 Déf | 1 PV, 1 Att, 1 Déf | 1 PV, 2 AtqSpé |
| Taille / poids | 2,6 m / 500 kg | 2,0 m / 350 kg | 2,2 m / 260 kg |
| Couleur | Marron | Bleu | Noir |
| Catégorie (en jeu) | Choco Golem | Fungus God | Frost Goblin |

Asexués, sans œuf, 80 cycles, bonheur 0, légendaires.

## Kit final (niv. 40, celui de la rencontre)
- **Croqueleur** : Lame de Roc (Stone Edge), Marto-Poing (Hammer Arm), Poing
  Glace (Ice Punch), Gonflette (Bulk Up).
- **Ougah** : Encornebois (Horn Leech), Éboulement (Rock Slide), Spore,
  Synthèse (Synthesis).
- **Grolloum** : Laser Glace (Ice Beam), Vibrobscur (Dark Pulse), Banquise
  (Pack Ice), Machination (Nasty Plot).

Bizarrerie (Ougah) est représentée par le talent Courroupace, sans capacité
custom.

## Capacités custom
**Banquise** — en jeu **Pack Ice** (`MOVE_BANQUISE`) : Glace, spéciale,
puissance 75, précision 100, 10 PP. Rend au lanceur la moitié des dégâts
infligés (`EFFECT_ABSORB`, comme Giga-Sangsue). Animation de Lyophilisation.
Description : « Freezing waves sap the foe. / Half the damage heals user. »

## Learnsets
| Niv. | Croqueleur | Ougah | Grolloum |
|---|---|---|---|
| 1 | Anti-Air (Smack Down) · Roche · Phys. · 50 | Vampigraine (Leech Seed) · Plante · Statut | Vent Glace (Icy Wind) · Glace · Spé. · 55 |
| 1 | Poing Feu (Fire Punch) · Feu · Phys. · 75 | Tomberoche (Rock Tomb) · Roche · Phys. · 60 | Aboiement (Snarl) · Ténèbres · Spé. · 55 |
| 1 | Poing Éclair (Thunder Punch) · Électrik · Phys. · 75 | Para-Spore (Stun Spore) · Plante · Statut | Provoc (Taunt) · Ténèbres · Statut |
| 1 | Barrage (Block) · Normal · Statut | Racines (Ingrain) · Plante · Statut | Balance (Pain Split) · Normal · Statut |
| 9 | Poing Glace (Ice Punch) · Glace · Phys. · 75 | Spore · Plante · Statut | Banquise (Pack Ice) · Glace · Spé. · 75 |
| 18 | Gonflette (Bulk Up) · Combat · Statut | Synthèse (Synthesis) · Plante · Statut | Machination (Nasty Plot) · Ténèbres · Statut |
| 27 | Marto-Poing (Hammer Arm) · Combat · Phys. · 100 | Éboulement (Rock Slide) · Roche · Phys. · 75 | Vibrobscur (Dark Pulse) · Ténèbres · Spé. · 80 |
| 36 | Lame de Roc (Stone Edge) · Roche · Phys. · 100 | Encornebois (Horn Leech) · Plante · Phys. · 75 | Laser Glace (Ice Beam) · Glace · Spé. · 90 |
| 45 | Projection (Circle Throw) · Combat · Phys. · 60 | Pico-Défense (Spiky Shield) · Plante · Statut | Chute de Neige (Snowscape) · Glace · Statut |
| 54 | Big Splash (Body Press) · Combat · Phys. · 80 | Vole-Force (Strength Sap) · Plante · Statut | Second Souffle (Revival Blessing) · Normal · Statut |
| 63 | Piège de Roc (Stealth Rock) · Roche · Statut | Malédiction (Curse) · Spectre · Statut | Explonuit (Night Daze) · Ténèbres · Spé. · 85 |
| 72 | Mitra-Poing (Focus Punch) · Combat · Phys. · 150 | Mégafouet (Power Whip) · Plante · Phys. · 120 | Lyophilisation (Freeze-Dry) · Glace · Spé. · 70 |
| 81 | Close Combat · Combat · Phys. · 120 | Lame de Roc (Stone Edge) · Roche · Phys. · 100 | Blizzard · Glace · Spé. · 110 |
| 90 | Fracass'Tête (Head Smash) · Roche · Phys. · 150 | Martobois (Wood Hammer) · Plante · Phys. · 120 | Buée Noire (Haze) · Glace · Statut |

## CT, CS et tuteurs
| | Croqueleur | Ougah | Grolloum |
|---|---|---|---|
| Socle commun | Toxik, Abri, Repos, Façade, Ultralaser, Reflet, Vantardise, Ténacité, Blabla Dodo, Ronflement, Provoc, Tourmente | idem | idem |
| STAB | Tomberoche, Éboulement, Tempête de Sable, Éclate-Roc, Force, Mitra-Poing, Gonflette, Casse-Brique, Dynamo-Poing, Riposte, Frappe Atlas | Giga-Sangsue, Balle Graine, Lance-Soleil, Zénith, Tomberoche, Éboulement, Tempête de Sable, Éclate-Roc, Force | Laser Glace, Blizzard, Grêle, Vent Glace, Poing Glace, Larcin |
| Couverture | Séisme, Tunnel, Poing Feu, Poing Glace, Poing Éclair, Méga-Poing, Plaquage | Séisme, Roulade, Boul'Armure, Danse Lames, Plaquage, Mur Lumière, Protection, Rune Protect | Lance-Flammes, Déflagration (sorts Feu de Dofus), Ball'Ombre, Bombe Beurk, Plénitude, Mur Lumière, Méga-Poing, Plaquage |

Exclusions volontaires : aucune attaque spéciale pour Croqueleur, aucun coup
de poing pour Ougah (pas de bras), ni Électrik ni Psy pour Grolloum, pas
d'Attraction (asexués).
