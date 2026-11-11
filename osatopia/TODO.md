# TODO Osatopia

- [ ] **Milirat** : retirer Poursuite (niv. 9) et Feinte (niv. 18) de son learnset, inutilisables dans le jeu (« Cette capacité ne peut pas être utilisée »). Les remplacer par des attaques Ténèbres utilisables de puissance équivalente.
- [ ] **Milirat** : il donne 2 EV en Attaque Spéciale alors que c'est un attaquant physique (Att 99, AtqSpé 45). Passer probablement à `.evYield_Attack = 2`.

## Animations des attaques custom

Les attaques custom réutilisent l'animation d'une attaque existante, sauf celles marquées d'un script dédié (`.battleAnimScript` dans `src/data/moves_info.h`, section `// Osatopia`). Les scripts sont dans `data/battle_anim_scripts.s`. Les scripts dédiés sont regroupés sous « Osatopia : animations des attaques custom », et le test `test/battle/move_animations/all_anims.c` (avec `T_SHOULD_RUN_MOVE_ANIM` et `ANIM_TEST_START_MOVE MOVES_COUNT_GEN9`) vérifie qu'ils ne laissent pas de sprites orphelins. Exemple d'animation maison : `gBattleAnimStatus_Bleed`, une griffure suivie d'un clignotement rouge, faite à partir de Griffe et du Poison.

Priorité : 🔴 l'animation actuelle trompe sur l'effet · 🟠 correcte mais générique · 🟢 elle convient.

- [x] 🔴 **Bave Fatale** (Poison, K.O. en un coup) — `gBattleAnimMove_BaveFatale` : bulles de Toxik sous la cible, jet de Détricanon raccourci, cible teintée de violet.
- [x] 🔴 **Gloutage** (Eau, K.O. en un coup) — `gBattleAnimMove_Gloutage` : mâchoire d'eau de Croc Fatal, puis crocs de Mâchouille teintés en bleu sur fond sombre, cible teintée de bleu profond.
- [x] 🔴 **Lancer Blop** (Eau, physique) — `gBattleAnimMove_LancerBlop` : œuf de Bombe Œuf teinté en bleu lancé en cloche, éclaboussure de Pistolet à O à l'impact.
- [ ] 🟠 **Galop** (Normal, pivot) — actuelle : Charge. Proposition : course et sabots (Écrasement ou Damoclès), puis le lanceur sort comme avec Demi-Tour.
- [ ] 🟠 **Filon d'Or** (Sol, physique, rapporte de l'argent) — actuelle : Jackpot. Proposition : des pépites dorées jaillissent du sol (Jet-Pierres recoloré en or), puis les pièces de Jackpot.
- [ ] 🟠 **Tofuïsation** (Psy, change la cible en type Vol) — actuelle : Poudre Magique. Proposition : un nuage de plumes (Danse Plumes) autour de la cible, qui vire au jaune Tofu.
- [ ] 🟠 **Potager** (Normal, plante des cawottes qui soignent) — actuelle : Racines. Proposition : des cawottes (sprite de baie recoloré en orange) qui poussent autour du lanceur.
- [ ] 🟠 **Déchirure** (Ténèbres, fait saigner) — actuelle : Éclate Griffe. Proposition : garder Éclate Griffe et ajouter le clignotement rouge sang de `gBattleAnimStatus_Bleed`.
- [ ] 🟠 **Lacération** (Ténèbres, 10 % de saignement) — actuelle : Tranche-Nuit. Proposition : Tranche-Nuit avec des entailles recolorées en rouge.
- [ ] 🟢 **Filante** (Fée, pivot) — actuelle : Météores. Les étoiles conviennent.
- [ ] 🟢 **Sarbacane** (Eau, 2 à 5 coups) — actuelle : Pistolet à O. Ça convient ; une variante plus fine (Hydro-Queue réduite) serait un plus.
- [ ] 🟢 **Masse Ombre** (Spectre, physique) — actuelle : Os Ombre. Ça convient.
- [ ] 🟢 **Radicule** (Plante, annule les stats modifiées) — actuelle : Mégafouet. Ça convient ; un nuage blanc (Bain de Smog) pour la remise à zéro serait un plus.
- [ ] 🟢 **Lait de Coco** (Plante, soin) — actuelle : Lait à Boire. Ça convient ; recolorer en blanc et vert serait un plus.
