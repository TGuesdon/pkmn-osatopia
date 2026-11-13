# Famille Kwoan

> Le Kwoan est une tête de mort qui hante le Cimetière, ses cryptes et la
> Maison Fantôme (niv. 32–40). Il frappe au contact (*Frappe Gerbante*),
> devient intaclable (*Déplacement Libre*) et réduit la portée de ses
> ennemis (*Confusion Optique*). Le Chafer est le squelette de base
> de la race Chafers, armé d'une épée (*Coup du Chafer*, Terre).
> Évolutions : Kwoan → Chafer (niv. 25).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Placeholders remplacés par des valeurs choisies pour un squelette : asexué
(`MON_GENDERLESS`), `.eggCycles = 15`, `STANDARD_FRIENDSHIP`,
`GROWTH_MEDIUM_FAST` (remplissage de route, comme Medhyèna et Osselait), `EGG_GROUP_AMORPHOUS`, `BODY_COLOR_WHITE`.

## Intention

Archétype : **remplissage de route**, avec une tendance **tank offensif lent**
au stade final · Références : Grahyèna (le Ténèbres basique, échelle de
puissance), Ossatueur (le squelette lent et robuste), Scalproie (la lame
Ténèbres) · Pourquoi : un mort-vivant tout ce qu'il y a de plus basique. D'abord
une tête qui mord et qui hante, puis un squelette complet avec une épée.

Le type **Ténèbres pur** vient de l'univers du Cimetière (le sort du Chafer
est Terre). Les autres Ténèbres purs (Gob Trotteur, Leolhyène) sont des
physiques rapides : le Chafer est lent et ne prend pas Coup Bas ni Danse Lames.

## Stades

| | Kwoan | Chafer |
|---|---|---|
| Constante | `SPECIES_KWOAN` | `SPECIES_CHAFER` |
| Types | Ténèbres | Ténèbres |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 45 / 60 / 60 / 35 / 40 / 35 | 75 / 105 / 85 / 40 / 60 / 55 |
| Total | 275 | 420 |
| Talents | Incisif / Armurbaston / Corps Maudit (caché) | Incisif / Armurbaston / Corps Maudit (caché) |
| Capture / Exp. | 190 / 60 | 75 / 170 |
| EV | 1 Déf | 1 Att, 1 Déf |

Stats sacrifiées : l'AtqSpé (corps à corps uniquement), la Vit (squelette
raide, à l'opposé des autres Ténèbres custom) et un peu la DéfSpé (les os
encaissent mieux les coups que la magie).

Comparaison : Grahyèna 420, Ossatueur 425, Berserkatt 440 ; Sherpoa (420)
a le même total mais il est Roche et bien plus rapide (75).

## Kit final (Chafer, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB épée | Tranche-Nuit (Night Slash) | Ténèbres | Phys. | 70 (105) | Tranchante, critique élevé ; à l'évolution |
| STAB lourd | Représailles (Payback) | Ténèbres | Phys. | 50 / 100 | Double s'il frappe en second, idéal pour un lent |
| Couverture | Lame Sainte (Sacred Sword) | Combat | Phys. | 90 (135) | Tranchante, ignore les boosts de Déf |
| Boost | Aiguisage (Hone Claws) | Ténèbres | Statut | – | +1 Att / +1 Précision ; il affûte sa lame |

Les puissances entre parenthèses incluent Incisif.

Alternatives dans le learnset et les CT : Mâchouille, Tricherie, Osmerang,
Mur de Fer, Casse-Brique, Taillade, Provoc.

Talents :
- **Incisif** (Sharpness) : ×1,5 sur les capacités tranchantes (Tranche-Nuit,
  Lame Sainte, Taillade, Coupe).
- **Armurbaston** (Battle Armor) : immunisé aux coups critiques, l'armure d'os.
- **Corps Maudit** (Cursed Body), caché : peut infliger Entrave à l'attaquant.

## Capacités custom

Aucune. Les sorts Dofus correspondent à des attaques existantes : *Frappe
Gerbante* → Coup d'Boule, *Confusion Optique* → Onde Folie, *Déplacement
Libre* → Regard Noir, *Coup du Chafer* → Tranche-Nuit.

## Learnsets

Temporisation : un Kwoan qui n'évolue pas apprend Mâchouille (27) et
Tricherie (37) bien plus tôt que le Chafer (36 et 48), qui reçoit à la place
son épée dès l'évolution.

### Kwoan

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 1 | Étonnement (Astonish) | Spectre | Phys. | 30 |
| 5 | Représailles (Payback) | Ténèbres | Phys. | 50 |
| 9 | Regard Noir (Mean Look) | Normal | Statut | – |
| 12 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 16 | Onde Folie (Confuse Ray) | Spectre | Statut | – |
| 20 | Coup d'Boule (Headbutt) | Normal | Phys. | 70 |
| 27 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 32 | Tourmente (Torment) | Ténèbres | Statut | – |
| 37 | Tricherie (Foul Play) | Ténèbres | Phys. | 95 |

### Chafer

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Tranche-Nuit (Night Slash) | Ténèbres | Phys. | 70 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 1 | Étonnement (Astonish) | Spectre | Phys. | 30 |
| 5 | Représailles (Payback) | Ténèbres | Phys. | 50 |
| 9 | Regard Noir (Mean Look) | Normal | Statut | – |
| 12 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 16 | Onde Folie (Confuse Ray) | Spectre | Statut | – |
| 20 | Coup d'Boule (Headbutt) | Normal | Phys. | 70 |
| 29 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 32 | Osmerang (Bonemerang) | Sol | Phys. | 50 × 2 |
| 36 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 40 | Lame Sainte (Sacred Sword) | Combat | Phys. | 90 |
| 44 | Mur de Fer (Iron Defense) | Acier | Statut | – |
| 48 | Tricherie (Foul Play) | Ténèbres | Phys. | 95 |

## CT, CS et tuteurs

| | Kwoan | Chafer |
|---|---|---|
| Toxik, Abri, Repos, Façade, Reflet (CT) | ✅ | ✅ |
| Provoc, Tourmente, Larcin (CT) | ✅ | ✅ |
| Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✅ | ✅ |
| Coud'Boue (tuteur) | ✅ | ✅ |
| Roulade (tuteur) : la tête qui roule | ✅ | – |
| Casse-Brique (CT) : couvre Ténèbres, Acier, Normal | – | ✅ |
| Aéropique (CT) : coup d'épée qui ne rate pas | – | ✅ |
| Tomberoche (CT) : couvre Vol | – | ✅ |
| Tunnel (CT) : il sort de sa tombe | – | ✅ |
| Coupe, Éclate-Roc, Force (CS) | – | ✅ |
| Taillade (tuteur) : tranchante, profite d'Incisif | – | ✅ |
| Ultralaser (CT) | – | ✅ |

Exclus volontairement :
- Zénith, Danse Pluie : aucun sens pour un squelette ;
- Danse Lames, Gonflette : garderaient Aiguisage et Mur de Fer sans intérêt,
  et tous les autres Ténèbres custom ont déjà Danse Lames ;
- Séisme : couverture trop forte pour un remplissage ; Osmerang et Tunnel
  suffisent ;
- Ball'Ombre et les autres attaques spéciales : AtqSpé 40 ;
- Mitra-Poing et les poings des tuteurs : il se bat à l'épée ; Queue de Fer :
  pas de queue ;
- Attraction : asexué ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée,
  Force Cachée.
