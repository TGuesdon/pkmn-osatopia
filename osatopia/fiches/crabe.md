# Famille Crabe

> Le Crabe (DofusDB #63) est un crabe violoniste du Rivage sufokien (Monstres
> des plages, niv. 42-50), affublé d'une pince géante. Sorts : *Pince* (corps à
> corps, Terre), *Violon Sel* (−2 PM et −10 Fuite en zone) et *Chancre* (Feu,
> piège déclenché). Le Crustorail Kouraçao (DofusDB #1060) est un bernard-l'ermite
> de la Colonie du Magistral (Plage de Corail, Grotte Hesque, niv. 36-48) qui
> porte des tubes de corail sur le dos : *Pince de Corail* (Eau, augmente les
> dommages des alliés autour de lui) et *Protection de Corail* (résistance Eau
> en zone). — Évolutions : Crabe → Crustorail (niv. 30).
> Constantes : `SPECIES_CRABE` (1731), `SPECIES_CRUSTORAIL` (1732), créées
> pour cette famille (1730 est réservé à Gambaf).

**État : validée et intégrée** (`include/constants/species.h`,
`include/constants/pokedex.h`, `include/constants/moves.h`, `moves_info.h`,
`species_info.h`, `gen_9.h`, `teachable_learnsets.h`, `pokedex_orders.h`,
`pokemon.c`, `graphics/pokemon.h`, sprites Dofus).

## Intention

Archétype : **attaquant à boost** (principal), à boost progressif plutôt
qu'instantané, + **tank offensif** (secondaire). Références : **Krabboss**
(profil de stats, typage Eau pur, Pince-Masse, Guillotine, Hyper Cutter /
Coque Armure), **Scalproie** (attaquant physique lent à moyen
qui monte en puissance au fil du combat).

Pourquoi : la lignée tourne autour de la **pince**. Crustorail ne se boost pas
avec Danse Lames : chaque *Pince de Corail* (capacité custom, Eau, +1 Attaque)
le rend plus dangereux, comme le sort Dofus qui augmente les dommages autour
de lui. **Hyper Cutter** protège ce boost progressif (Intimidation, Charme…),
**Griffe Dure** récompense les pinces (attaques directes).
Pince-Masse fait le STAB, Séisme (ou Tunnelier en attendant la CT) couvre
sa faiblesse Électrik, Ancrage reprend le *Violon Sel* (la cible ne peut plus
fuir), Guillotine reste le coup de poker.

Ce qui le distingue des autres monstres marins :
- **Gambaf** (en conception, Eau/Combat) : démolisseur lent avec Poing de Fer.
  Crustorail n'a aucun coup de poing (Pince de Corail n'est pas un poing), il
  est Eau pur, plus rapide, et monte en puissance au lieu de frapper fort tout
  de suite.
- **Tortue Bleue** (Eau/Combat) a déjà le créneau « coups critiques » (Chanceux
  + Puissance + Tranch'Aqua) : Crustorail n'a ni Chanceux ni Puissance.
- **Corailleur** (Roche/Eau, même colonie) est une forteresse lente (Mur de
  Fer, Big Splash) ; Grokillage → Moumoule est spécial ; Dagon/Pichon/Raul Mops
  sont rapides et fragiles ; Tilamproie et Mol Usk sont spéciaux.
- Les autres **Eau purs** physiques : **Muldo** (95/110/75/45/70/95) est une
  monture rapide qui se boost d'un coup (Danse Draco, Glissade, Impudence,
  Aquatacle) ; **Pichon** est un nettoyeur rapide et fragile (Aqua-Jet,
  Coqui-Lame). Crustorail est plus lent (70), cuirassé (Déf 115), n'a ni
  Danse Draco ni Glissade, et couvre avec Sol et Acier.

## Stades

| | Crabe | Crustorail |
|---|---|---|
| Types | Eau | Eau |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 40 / 85 / 80 / 25 / 35 / 45 | 70 / 120 / 115 / 45 / 60 / 70 |
| Total | 310 | 480 |
| Talents | Hyper Cutter (Hyper Cutter) / Coque Armure (Shell Armor) / caché : Griffe Dure (Tough Claws) | idem |
| Capture / Exp. | 200 / 65 | 60 / 170 |
| EV | 1 Att | 2 Att + 1 Déf |
| Évolution | niv. 30 | – |

Eau pur : faiblesses Électrik et Plante. Résistances : Feu, Eau, Glace,
Acier. Séisme et Tunnelier répondent aux Électrik.

Comparaison : Krabby 30/105/90/25/25/50 (325), Krabboss 55/130/115/50/50/75
(475), Scalproie 65/125/100/60/70/70 (490), Corailleur 90/105/115/45/75/40
(470), Scordion 75/100/110/40/75/85 (485). Par rapport à Krabboss, Crustorail
prend 15 PV et 10 DéfSpé et perd 10 Att, 5 Vit et 5 AtqSpé : il doit survivre
le temps de cumuler ses boosts. L'AtqSpé est sacrifiée (aucun sort à distance
chez le Crabe), la DéfSpé reste faible (la carapace arrête les coups, pas la
magie). Le Crabe est un monstre de plage commun, plafonné à 310.

Valeurs par défaut (famille Bitouf, faute de choix) : 50 % femelle,
15 cycles d'œuf, bonheur standard, croissance moyenne-lente, groupe d'œuf
Aquatique 3 (`EGG_GROUP_WATER_3`, celui des crustacés), couleur rouge
(Crabe, orange en réalité) et violette (Crustorail, couleur des tubes de
corail).

Pokédex : Crabe 0,4 m / 7,0 kg, catégorie « Fiddler » ; Crustorail 1,1 m /
62,0 kg, catégorie « Coral Crab ». Descriptions en jeu :
- Crabe : « A fiddler crab of the Sufokian shore. It waves its huge pincer
  like a bow to scare off foes and court its mate. »
- Crustorail : « It hides under a crown of living coral. Each time its claws
  pinch a foe, the coral glows and its next blow hits even harder. »

## Kit final

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB Eau fort | Pince-Masse (Crabhammer), Eau, phys., 100, 90 %, critique élevé | Aqua-Brèche (Liquidation) 85 ; Cascade (Waterfall) 80, CS ; Coqui-Lame (Razor Shell) 75 ; Aquatacle (Wave Crash) 120, contrecoup |
| Boost | **Pince de Corail** (custom), Eau, phys., 40, +1 Att à chaque coup | Danse Lames (Swords Dance), tuteur ; Gonflette (Bulk Up), CT ; Griffe Acier (Metal Claw) 50, +1 Att à 10 % |
| Couverture Sol (contre Électrik) | Séisme (Earthquake), Sol, phys., 100, CT | Tunnelier (Drill Run) 80, critique élevé, niv. 37 (en attendant la CT) ; Assaut Frontal (Headlong Rush) 120, baisse ses défenses ; Piétisol (Bulldoze) 60, −1 Vit |
| Couverture / poker | Ancrage (Anchor Shot), Acier, phys., 80, la cible ne peut plus fuir | Guillotine (Guillotine), Normal, K.O. en un coup à 30 % ; Plaie Croix (X-Scissor) 80 ; Éboulement (Rock Slide) 75, tuteur |

Deux façons de le jouer :
- **Hyper Cutter** + Pince de Corail : il encaisse, cumule +1 Att par tour et
  personne ne peut lui retirer ses boosts d'Attaque.
- **Griffe Dure** (caché) : Pince-Masse, Tunnelier, Ancrage, Pince de Corail et
  Assaut Frontal sont des attaques directes (×1,3) ; pas Séisme.

Coque Armure (2ᵉ talent) est l'option défensive : pas de coup critique subi,
donc pas de boost perdu sur un critique.

Talents écartés : **Sans Limite** (Sheer Force, le 3ᵉ talent de Krabboss)
annule le +1 Att de Pince de Corail ; **Chanceux** (Super Luck) est déjà le
créneau de Tortue Bleue.

## Capacités custom

### Pince de Corail — en jeu « Coral Claw »

| Champ | Valeur |
|---|---|
| Constante | `MOVE_PINCE_DE_CORAIL` |
| Nom en jeu | Coral Claw (52 px) |
| Type / catégorie | Eau / Physique |
| Puissance / précision / PP | 40 / 100 % / 20 |
| Effet | +1 Attaque du lanceur à 100 % (`MOVE_EFFECT_ATK_PLUS_1`, `.self = TRUE`) |
| Contact | oui ; **pas** un coup de poing (`punchingMove` absent : Poing de Fer ne l'augmente pas) |
| Attaque la plus proche | Poing Boost (Power-Up Punch), `EFFECT_HIT` + `MOVE_EFFECT_ATK_PLUS_1` (même fiche, en type Eau) |
| Difficulté | **facile** : une entrée dans `moves_info.h` + une constante |
| Description | « A coral pincer strike that » (135 px) / « raises the user's Attack. » (131 px) |

Lien Dofus : *Pince de Corail* augmente les dommages des alliés autour du
Crustorail pendant 5 tours ; en combat simple, le bonus revient au lanceur.

Intégration : `MOVE_PINCE_DE_CORAIL = MOVES_COUNT_GEN9 + 15` (+14 réservé à `MOVE_BOND_METEORE` de Gambaf), animation de
Pince-Masse, ajoutée à `IsMoveSheerForceBoosted` dans
`test/battle/ability/sheer_force.c` et à `osatopia/noms_en_jeu.md`.

Variante écartée : **Violon Sel** (« Salt Fiddle »), Sol, statut, −2 Vitesse
et empêche la fuite (le sort du Crabe). Effet nouveau, difficulté moyenne ;
Grimace (Scary Face) et Ancrage couvrent déjà cette idée avec des attaques
existantes.

## Learnsets

**Crabe**

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| 1 | Force Poigne (Vise Grip) | Normal | Phys. | 55 | la pince, dès le départ |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – | −1 Déf |
| 4 | Armure (Harden) | Normal | Statut | – | carapace |
| 8 | Aqua-Jet (Aqua Jet) | Eau | Phys. | 40, prio +1 | STAB faible |
| 11 | Grimace (Scary Face) | Normal | Statut | – | *Violon Sel* : −2 Vit |
| 14 | Griffe Acier (Metal Claw) | Acier | Phys. | 50 | pince, +1 Att à 10 % |
| 17 | Piétisol (Bulldoze) | Sol | Phys. | 60 | Sol, −1 Vit |
| 21 | Coqui-Lame (Razor Shell) | Eau | Phys. | 75 | STAB moyen |
| 25 | Plaie Croix (X-Scissor) | Insecte | Phys. | 80 | les pinces en ciseaux |
| 29 | Gigotage (Flail) | Normal | Phys. | variable | clin d'œil à Krabby |

**Crustorail** (reprend les attaques du Crabe aux mêmes niveaux)

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| Évo | **Pince de Corail** (Coral Claw) | Eau | Phys. | 40 | boost progressif |
| 1 | Garde Large (Wide Guard) | Roche | Statut | – | *Protection de Corail* (protège l'équipe en double) |
| 33 | Ancrage (Anchor Shot) | Acier | Phys. | 80 | *Violon Sel* : bloque la fuite |
| 37 | Tunnelier (Drill Run) | Sol | Phys. | 80 | couverture contre Électrik |
| 42 | Pince-Masse (Crabhammer) | Eau | Phys. | 100 | STAB Eau fort |
| 47 | Guillotine (Guillotine) | Normal | Phys. | K.O. | coup de poker |
| 52 | Assaut Frontal (Headlong Rush) | Sol | Phys. | 120 | couverture finale |

17 attaques. Rien à 90+ avant le niveau 42. Contre Voltère (24, Électrik), le
Crabe est en difficulté (Piétisol aide) ; contre Adriane (29, Feu),
Coqui-Lame suffit.

Recoupements avec d'autres monstres custom : Scorpique/Scordion partagent Force
Poigne, Plaie Croix et Tunnelier, mais pas leur ordre ni le reste (Tourbi-Sable
et Aiguisage ont été écartés pour cette raison) ; Corailleur partage Aqua-Jet,
Grimace et Coqui-Lame. Pince-Masse, Ancrage (sauf Vigie Pirate au niv. 1),
Gigotage + Guillotine et Assaut Frontal + Pince de Corail sont propres à la
lignée.

## CT, CS et tuteurs

| Attaque | Crabe | Crustorail |
|---|---|---|
| CT Toxik, Abri, Repos, Façade, Attraction, Reflet, Protection, Danse Pluie, Tempête de Sable, Larcin, Faux-Chage | ✓ | ✓ |
| Tuteurs Ténacité, Blabla Dodo, Ronflement, Vantardise | ✓ | ✓ |
| CS Coupe, Surf, Force, Éclate-Roc, Cascade, Plongée | ✓ | ✓ |
| CT Tunnel, Tomberoche ; tuteurs Coud'Boue, Taillade, Vent Glace | ✓ | ✓ |
| CT Séisme, Casse-Brique, Provoc | – | ✓ |
| Tuteurs Éboulement, Plaquage, Damoclès | – | ✓ |

Exclusions volontaires :
- **Danse Lames** (tuteur) et **Gonflette** (CT) : Pince de Corail reste le
  seul boost (sinon le boost progressif perd son intérêt).
- Tous les **coups de poing** (Mitra-Poing, Poing Glace, Poing Éclair, Poing Feu,
  Ultimapoing, Dynamo-Poing) : des pinces, pas des poings, et c'est le
  créneau de Gambaf (Poing de Fer). Krabboss a Marto-Poing : écarté aussi.
- **Laser Glace, Blizzard, Ultralaser, Vibraqua** : spéciaux, AtqSpé 45
  (Surf reste pour l'exploration ; Vent Glace pour ralentir).
- **Séisme** réservé à Crustorail : le Crabe a Piétisol et Tunnel.
- Roulade, Boul'Armure, Explosion, Lance-Soleil : incohérents avec un crabe.

## Capture, expérience et EV

| | Capture | Exp. | EV |
|---|---|---|---|
| Crabe | 200 | 65 | 1 Att |
| Crustorail | 60 | 170 | 2 Att, 1 Déf |

Repères : Krabby 225 / 65, Krabboss 60 / 166 ; Grokillage 120 / 70 → Moumoule
45 / 195 ; Corailleur 45 / 170. Le Crabe est commun sur les plages et à la
pêche ; Crustorail se trouve en surf sur les routes maritimes plus tardives,
d'où une capture un peu meilleure qu'un stade final classique (45).

## Choix écartés

1. **Types** : Eau/Sol (première proposition) et Eau/Acier. L'utilisateur a
   choisi **Eau pur**, comme Krabboss et le Kouraçao.
2. **Stade final** : une évolution à embranchement vers les quatre
   Crustorails (Malibout, Passaoh, Morito) a été écartée ; seul le Kouraçao
   (#1060, l'élément Eau) est retenu.
3. **Boost** : Danse Lames comme Krabboss, ou Pince de Corail à 50 de
   puissance et 50 % de boost.
4. **Évolution** au niveau 28 comme Krabby (30 retenu).

## Sprites

Récupérés depuis Dofus (renderer Ankama, vraie vue de dos pour les deux) :
- Crabe : DofusDB #63, face direction 3, dos direction 5, taille « petit » ;
- Crustorail : Kouraçao #1060, face direction 1, dos direction 5, taille
  « grand ».

Icônes régénérées depuis la face (palette d'icône 3 pour les deux). Échelle du
Pokédex : 504 / 14 (Crabe), 313 / 5 (Crustorail).

## À faire

- Numérotation : `SPECIES_GAMBAF` (1730) est intégré sur une autre branche ;
  `MOVE_PINCE_DE_CORAIL` prend `MOVES_COUNT_GEN9 + 15`, +14 étant réservé à
  `MOVE_BOND_METEORE` (PR Gambaf #95).
- Rencontres : Crabe sur les plages (Route 109, sable) et à la pêche ;
  Crustorail en surf sur les routes maritimes (124-134).
