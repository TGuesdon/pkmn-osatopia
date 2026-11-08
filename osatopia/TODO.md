# TODO Osatopia

- [ ] **Milirat** : retirer Poursuite (niv. 9) et Feinte (niv. 18) de son learnset, inutilisables dans le jeu (« Cette capacité ne peut pas être utilisée »). Les remplacer par des attaques Ténèbres utilisables de puissance équivalente.
- [ ] **Milirat** : il donne 2 EV en Attaque Spéciale alors que c'est un attaquant physique (Att 99, AtqSpé 45). Passer probablement à `.evYield_Attack = 2`.

## Animations des attaques custom

Aucune attaque custom n'a d'animation dédiée : toutes réutilisent celle d'une attaque existante (`.battleAnimScript` dans `src/data/moves_info.h`, section `// Osatopia`). Les scripts sont dans `data/battle_anim_scripts.s`. Exemple d'animation maison : `gBattleAnimStatus_Bleed`, une griffure suivie d'un clignotement rouge, faite à partir de Griffe et du Poison.

Priorité : 🔴 l'animation actuelle trompe sur l'effet · 🟠 correcte mais générique · 🟢 elle convient.

- [ ] 🔴 **Bave Fatale** (Poison, K.O. en un coup) — actuelle : Toxik. Proposition : un glyphe de bave au sol puis un jet de boue (Détricanon), cible teintée de violet.
- [ ] 🔴 **Gloutage** (Eau, K.O. en un coup) — actuelle : Mâchouille. Proposition : la cible est aspirée (Avale) puis disparaît, avec un éclat d'eau.
- [ ] 🔴 **Lancer Blop** (Eau, physique) — actuelle : Écume. Proposition : un projectile en cloche (Canon Graine ou Bombe Œuf) recoloré en bleu, éclaboussure à l'impact.
- [ ] 🟠 **Galop** (Normal, pivot) — actuelle : Charge. Proposition : course et sabots (Écrasement ou Damoclès), puis le lanceur sort comme avec Demi-Tour.
- [ ] 🟠 **Filon d'Or** (Sol, physique, rapporte de l'argent) — actuelle : Jackpot. Proposition : des pépites dorées jaillissent du sol (Jet-Pierres recoloré en or), puis les pièces de Jackpot.
- [ ] 🟠 **Tofuïsation** (Psy, change la cible en type Vol) — actuelle : Poudre Magique. Proposition : un nuage de plumes (Danse Plumes) autour de la cible, qui vire au jaune Tofu.
- [ ] 🟠 **Potager** (Normal, plante des cawottes qui soignent) — actuelle : Racines. Proposition : des cawottes (sprite de baie recoloré en orange) qui poussent autour du lanceur.
- [ ] 🟠 **Déchirure** (Ténèbres, fait saigner) — actuelle : Éclate Griffe. Proposition : garder Éclate Griffe et ajouter le clignotement rouge sang de `gBattleAnimStatus_Bleed`.
- [ ] 🟠 **Lacération** (Ténèbres, 10 % de saignement) — actuelle : Tranche-Nuit. Proposition : Tranche-Nuit avec des entailles recolorées en rouge.
- [ ] 🟢 **Filante** (Fée, pivot) — actuelle : Météores. Les étoiles conviennent.
- [ ] 🟢 **Sarbacane** (Eau, 2 à 5 coups) — actuelle : Pistolet à O. Ça convient ; une variante plus fine (Hydro-Queue réduite) serait un plus.
- [ ] 🟢 **Masse Ombre** (Spectre, physique) — actuelle : Os Ombre. Ça convient.
- [ ] 🟢 **Lait de Coco** (Plante, soin) — actuelle : Lait à Boire. Ça convient ; recolorer en blanc et vert serait un plus.
