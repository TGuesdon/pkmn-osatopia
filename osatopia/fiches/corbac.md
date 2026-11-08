# Famille Corbac

> Corbeaux de la *race des Corbacs* (Pénates du Corbac, Bibliothèque du
> Maître Corbac, niv. 100–110), aux sorts Air et Terre. Le Corbac déstabilise
> (*Cri Déstabilisateur*), lance des œufs et dilacère ; le Capsaaloocke vole
> l'Agilité, repousse (*Saut du Bison*) et pousse ses alliés (*Éclaireurs*) ;
> le Maître Corbac, armé d'une faux, frappe d'une *Sanction Ténébreuse*,
> augmente les critiques (*Lien Volatile*) et renvoie les dégâts (*Carapace
> d'Ailes*). Lore DofusDB.
> Évolutions : Corbac → Capsaaloocke (niv. 16) → Corbomaitre (niv. 36).
> Corbomaitre est le nom Osatopia du Maître Corbac.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Le nom affiché du stade 2 est corrigé en « Capsaaloocke » (orthographe Dofus) ;
la constante reste `SPECIES_CAAPSALOOCKE` (définie dans `include/`).

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_FLYING`, couleur `BODY_COLOR_BLACK`.

## Intention

Archétype : **démolisseur**, avec **attaquant à boost** en secondaire
(Aiguisage). Oiseau sombre purement physique, avec de gros PV pour encaisser
avant de frapper, une Vitesse correcte sans être un nettoyeur, et un thème
« critique » (Chanceux, Tranche-Nuit) qui reprend *Lien Volatile*.

Références : **Yveltal** (esthétique, PV hauts, Aura Ténébreuse),
**Corboss** (corbeau patron, Impudence), **Étouraptor** (oiseau physique à
3 stades).

Premier Vol/Ténèbres d'Osatopia. Se distingue de Kwak Vent (Vol, très rapide)
et de Gob Trotteur (Ténèbres, nettoyeur rapide) par sa robustesse.

## Stades

| | Corbac | Capsaaloocke | Corbomaitre |
|---|---|---|---|
| Types | Vol / Ténèbres | Vol / Ténèbres | Vol / Ténèbres |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 42 / 60 / 35 / 30 / 35 / 58 | 68 / 88 / 55 / 40 / 50 / 84 | 95 / 120 / 75 / 50 / 72 / 93 |
| Total | 260 | 385 | 505 |
| Évolution | niv. 16 | niv. 36 | – |
| Talents | Chanceux / Impudence / Aura Ténébreuse (caché) | idem | idem |
| Capture / Exp. | 190 / 58 | 90 / 142 | 45 / 240 |
| EV | Att +1 | Att +2 | Att +3 |

Stat sacrifiée : l'Attaque Spéciale (monstre 100 % physique).

## Kit final

| Rôle | Attaque | Type | Puiss. | Note |
|---|---|---|---|---|
| STAB Vol fort | Rapace (Brave Bird) | Vol | 120 | Contrecoup 1/3, exclusif au stade final (niv. 47) |
| STAB Ténèbres | Tranche-Nuit (Night Slash) | Ténèbres | 70 | Critique élevé, synergie Chanceux |
| Boost | Aiguisage (Hone Claws) | Ténèbres | – | Att + Précision |
| Couverture | Ailes d'Acier (Steel Wing) | Acier | 70 | Contre Fée, Glace, Roche |

Alternatives : Cent Rancunes, Bec Vrille, Danse Lames (tuteur), Éboulement
(tuteur), Atterrissage. Faux-Chage (à l'évolution) sert d'outil de capture,
en écho à la faux du Maître Corbac.

Aura Ténébreuse : +33 % de puissance aux attaques Ténèbres de tous les
Pokémon sur le terrain (×0,75 face à Aura Inversion).

## Capacités custom

Aucune. Piste écartée : *Sanction Ténébreuse* (Ténèbres physique à critique
élevé, effet de Tranche-Nuit).

## Learnsets

### Corbac

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Picpic (Peck) | Vol | Phys. | 35 |
| 1 | Grimace (Scary Face) | Normal | Statut | – |
| 4 | Représailles (Payback) | Ténèbres | Phys. | 50 |
| 8 | Danse Plumes (Feather Dance) | Vol | Statut | – |
| 11 | Double Volée (Dual Wingbeat) | Vol | Phys. | 40×2 |
| 13 | Larcin (Thief) | Ténèbres | Phys. | 60 |

### Capsaaloocke

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Vent Arrière (Tailwind) | Vol | Statut | – |
| 1–13 | (attaques de Corbac aux mêmes niveaux) | | | |
| 18 | Cru-Ailes (Wing Attack) | Vol | Phys. | 60 |
| 21 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 24 | Tranche-Nuit (Night Slash) | Ténèbres | Phys. | 70 |
| 27 | Buée Noire (Haze) | Glace | Statut | – |
| 30 | Bec Vrille (Drill Peck) | Vol | Phys. | 80 |
| 33 | Bombe Œuf (Egg Bomb) | Normal | Phys. | 100 |
| 38 | Cent Rancunes (Lash Out) | Ténèbres | Phys. | 75 |
| 44 | Atterrissage (Roost) | Vol | Statut | – |

### Corbomaitre

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Faux-Chage (False Swipe) | Normal | Phys. | 40 |
| Évo | Ailes d'Acier (Steel Wing) | Acier | Phys. | 70 |
| 1 | Vent Arrière (Tailwind) | Vol | Statut | – |
| 1–33 | (attaques de Corbac et Capsaaloocke aux mêmes niveaux) | | | |
| 39 | Cent Rancunes (Lash Out) | Ténèbres | Phys. | 75 |
| 43 | Atterrissage (Roost) | Vol | Statut | – |
| 47 | Rapace (Brave Bird) | Vol | Phys. | 120 |

Liens Dofus : Buée Noire ← *Cri Déstabilisateur*, Bombe Œuf ← *Lancer
d'œuf*, Vent Arrière ← *Éclaireurs*, Faux-Chage ← la faux du Maître.

## CT, CS et tuteurs

| Attaque | Corbac | Capsaaloocke | Corbomaitre |
|---|:-:|:-:|:-:|
| Toxik, Abri, Repos, Reflet, Façade, Attraction, Ténacité, Ronflement, Blabla Dodo, Vantardise | ✓ | ✓ | ✓ |
| Aéropique, Vol (CS), Larcin, Provoc, Tourmente | ✓ | ✓ | ✓ |
| Ailes d'Acier, Tomberoche | ✓ | ✓ | ✓ |
| Hurlement (← *Saut du Bison*) | | ✓ | ✓ |
| Éboulement, Danse Lames, Damoclès (tuteurs) | | ✓ | ✓ |
| Coupe (CS), Taillade (tuteur) — la faux | | | ✓ |
| Ultralaser | | | ✓ |

Exclusions volontaires : coups de poing et Casse-Brique (oiseau), Séisme et
Tunnel, Queue de Fer, attaques spéciales (Ball'Ombre…), Gonflette (déjà
très répandue, le kit a Aiguisage).
