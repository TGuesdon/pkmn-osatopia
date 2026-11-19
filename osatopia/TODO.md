# TODO Osatopia

- [x] **Milirat** : retirer Poursuite (niv. 9) et Feinte (niv. 18) de son learnset, inutilisables dans le jeu (« Cette capacité ne peut pas être utilisée »). Les remplacer par des attaques Ténèbres utilisables de puissance équivalente.
- [x] **Milirat** : il donne 2 EV en Attaque Spéciale alors que c'est un attaquant physique (Att 99, AtqSpé 45). Passer probablement à `.evYield_Attack = 2`.

## Animations des attaques custom

Les attaques custom réutilisent l'animation d'une attaque existante, sauf celles marquées d'un script dédié (`.battleAnimScript` dans `src/data/moves_info.h`, section `// Osatopia`). Les scripts sont dans `data/battle_anim_scripts.s`. Les scripts dédiés sont regroupés sous « Osatopia : animations des attaques custom », et le test `test/battle/move_animations/all_anims.c` (avec `T_SHOULD_RUN_MOVE_ANIM` et `ANIM_TEST_START_MOVE MOVES_COUNT_GEN9`) vérifie qu'ils ne laissent pas de sprites orphelins. Exemple d'animation maison : `gBattleAnimStatus_Bleed`, une griffure suivie d'un clignotement rouge, faite à partir de Griffe et du Poison.

Priorité : 🔴 l'animation actuelle trompe sur l'effet · 🟠 correcte mais générique · 🟢 elle convient.

- [x] 🔴 **Bave Fatale** (Poison, K.O. en un coup) — `gBattleAnimMove_BaveFatale` : bulles de Toxik sous la cible, jet de Détricanon raccourci, cible teintée de violet.
- [x] 🔴 **Gloutage** (Eau, K.O. en un coup) — `gBattleAnimMove_Gloutage` : mâchoire d'eau de Croc Fatal, puis crocs de Mâchouille teintés en bleu sur fond sombre, cible teintée de bleu profond.
- [x] 🔴 **Lancer Blop** (Eau, physique) — `gBattleAnimMove_LancerBlop` : œuf de Bombe Œuf teinté en bleu lancé en cloche, éclaboussure de Pistolet à O à l'impact.
- [x] 🟠 **Galop** (Normal, pivot) — `gBattleAnimMove_Galop` : le lanceur fonce en boule de poussière comme avec Demi-Tour, piétine deux fois (sabots d'Écrasement) et revient.
- [x] 🟠 **Filon d'Or** (Sol, physique, rapporte de l'argent) — `gBattleAnimMove_FilonDor` : le sol tremble, des pépites (Jet-Pierres teinté en or) tombent sur la cible, puis les pièces de Jackpot.
- [x] 🟠 **Tofuïsation** (Psy, change la cible en type Vol) — `gBattleAnimMove_Tofuisation` : plumes de Danse Plumes teintées en jaune Tofu, puis la cible vire au jaune et se déforme.
- [x] 🟠 **Potager** (Normal, plante des cawottes qui soignent) — `gBattleAnimMove_Potager` : les racines de Racines, teintées en orange cawotte, poussent autour du lanceur.
- [x] 🟠 **Déchirure** (Ténèbres, fait saigner) — `gBattleAnimMove_Dechirure` : Éclate Griffe aux griffes rouges, puis le clignotement rouge sang du Saignement.
- [x] 🟠 **Lacération** (Ténèbres, 10 % de saignement) — `gBattleAnimMove_Laceration` : Tranche-Nuit aux entailles rouge sang.
- [ ] 🟢 **Filante** (Fée, pivot) — actuelle : Météores. Les étoiles conviennent.
- [ ] 🟢 **Sarbacane** (Eau, 2 à 5 coups) — actuelle : Pistolet à O. Ça convient ; une variante plus fine (Hydro-Queue réduite) serait un plus.
- [ ] 🟢 **Masse Ombre** (Spectre, physique) — actuelle : Os Ombre. Ça convient.
- [ ] 🟢 **Radicule** (Plante, annule les stats modifiées) — actuelle : Mégafouet. Ça convient ; un nuage blanc (Bain de Smog) pour la remise à zéro serait un plus.
- [ ] 🟢 **Lait de Coco** (Plante, soin) — actuelle : Lait à Boire. Ça convient ; recolorer en blanc et vert serait un plus.

## Rencontres sauvages hors `wild_encounters.json`

- [x] **Barpau (Route 119)** : `sWildFeebas` (6 cases de pêche, niv. 20–25) donne désormais **Tilamproie**.
- [x] **Dons, échanges et combats scriptés remplacés** :
  - Dons : Terhal → **Sinistrofu** (Steven), Morphéo → **Dolbinos** + Aimant (Institut Météo), œuf d'Okéoké → **Timansot** (Vermilava), fossiles Racine / Griffe → **Soldalia** / **Phorreveur** (Devon), starters de Johto → **Tifoux / Titardo / Tronknyde** (labo, Pokédex complété).
  - Échanges (`src/data/trade.h`) : Chacha ← Tigrimas (Mérouville), Pupuce ← Mouchame (Cimetronelle), Germinion ← Dragoune (Pacifiville), Scarafeuille Noir ← Écurouille (Zone de Combat).
  - Combats : Kecleon → **Maltrio** niv. 30, Voltorbe / Électrode → **Gobus**, Simularbre → **Abraknyde** niv. 40.
  - Code : Zigzaton prêté à Timmy et Zigzaton du premier combat → **Boufton**.
- [x] **Sprites hors combat** (32×32, rendus Dofus réduits, palette propre) : Maltrio (`OBJ_EVENT_GFX_MALTRIO`, Routes 119/120 et Cimetronelle), Abraknyde à la place de l'arbre Simularbre (`OBJ_EVENT_GFX_SUDOWOODO`), Boufton à la place du Zigzaton qui poursuit Seko (`OBJ_EVENT_GFX_ZIGZAGOON_1`).
- [x] **Reflet du pont de la Route 120** (`OBJ_EVENT_GFX_KECLEON_BRIDGE_SHADOW`) : silhouette 16×16 de Maltrio.
- [x] **Pokémon de compagnie** (sprites hors combat, cris et répliques) : Zigzaton → Boufton, Skitty → Chacha, Goélise (dont PEEKO) → Tofu, Azurill / Azumarill → Biblop / Blop, Pikachu → Dokachu (PEKACHU devient DOKACHOU), Medhyèna des sbires → Chienchien Enragé, Kecleon → Écurouille (Lilycove, Route 117) et Chienchien Noir (Sootopolis, `OBJ_EVENT_GFX_CHIENCHIEN_NOIR`), Vigoroth déménageurs → Koalak Immature, Tarsal / Kirlia et Dusclops (Palais et Pike de la Zone de Combat) → Tigrimas et Fantomayte.
- [ ] **Encore vanilla côté décor** : Mew (Île Lointaine), décoration de base secrète « toy TV shaped like a SKITTY », dresseurs qui parlent de « BIRD POKéMON ». Les constantes d'enum (`INGAME_TRADE_SEEDOT`…) et les labels de script gardent aussi les noms vanilla.
- [x] **Regirock / Regice / Registeel** : remplacés par Croqueleur, Grolloum et Ougah (`osatopia/fiches/regis.md`).
- [ ] **Encore vanilla, à concevoir** :
  - Latios / Latias errants (`src/roamer.c`) et à l'Île du Sud.
  - Îles événementielles (Mew, Deoxys, Lugia, Ho-Oh), œuf Pichu (Cadeau Mystère), rencontres du Pike et de la Pyramide (Zone de Combat).
- [x] **Pierres d'évolution des Bwak** : deux exemplaires de chaque au sol : Pierre Glace (Grotte Tréfonds à marée basse, salle de glace et salle basse), Pierre Terre (Grotte Granite B1F et B2F), Pierre Vent (Chutes Météore 1F, deux recoins).
