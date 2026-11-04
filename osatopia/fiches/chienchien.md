# Familles Chienchien (Leolhyène et Muloubard)

> Deux familles « miroir » de chiens errants. Le Chienchien Enragé, hargneux,
> devient le Leolhyène, une hyène charognarde ; le Chienchien Noir devient le
> Muloubard, un loup loubard qui se tient debout. *(Lore de mémoire, à
> vérifier : éléments des sorts et zones.)*
> Évolutions : Chienchien Enragé → Leolhyène (niv. 25) ; Chienchien Noir →
> Muloubard (niv. 25).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_FIELD` ; couleur `BODY_COLOR_BROWN` (famille Enragé) et
`BODY_COLOR_BLACK` (famille Noir).

## Intention

Deux attaquants physiques de **même total** (280 → 455) et de **types
simples**, pour qu'aucune famille n'ait un meilleur typage que l'autre.

- **Leolhyène** — Archétype : **nettoyeur rapide**. Références : Grahyèna
  (kit Ténèbres et morsures), Lougaroc Midi (profil Att/Vit). Plus rapide,
  plus fragile, priorité (Coup Bas) et Danse Lames.
- **Muloubard** — Archétype : **tank offensif**. Références : Pandarbare (la
  brute Combat), Baggaïd (le voyou robuste). Plus de PV et de Défense,
  soin par Vampi-Poing et Gonflette.

Mécanique miroir : **Prognathe** pour les deux. La hyène mord ; le loup mord
aussi, mais il se bat debout, aux poings.

## Stades

| | Chienchien Enragé | Leolhyène | Chienchien Noir | Muloubard |
|---|---|---|---|---|
| Constante | `SPECIES_CHIENCHIEN_ENRAGE` | `SPECIES_LEOLHYENE` | `SPECIES_CHIENCHIEN_NOIR` | `SPECIES_MULOUBARD` |
| Types | Ténèbres | Ténèbres | Combat | Combat |
| PV | 45 | 75 | 55 | 100 |
| Attaque | 65 | 105 | 65 | 110 |
| Défense | 40 | 60 | 50 | 80 |
| Atq. Spé | 30 | 48 | 30 | 40 |
| Déf. Spé | 40 | 62 | 40 | 62 |
| Vitesse | 60 | 105 | 40 | 63 |
| **Total** | **280** | **455** | **280** | **455** |
| Évolution | niv. 25 | – | niv. 25 | – |
| Talents | Prognathe / Impudence / *Colérique* | idem | Prognathe / Cran / *Chien de Garde* | idem |
| Capture / Exp. | 190 / 60 | 75 / 170 | 190 / 60 | 75 / 170 |
| EV | Att +1 | Att +1, Vit +1 | Att +1 | Att +1, PV +1 |

Stats sacrifiées : l'AtqSpé pour tous (attaquants physiques), les défenses
pour Leolhyène, la Vitesse pour Muloubard. Les totaux finaux restent au
milieu de la fourchette « 2 stades, commun » (évolution à 25), sans stat
au-dessus de 110.

Comparaisons (outil `similaires`) :
- Leolhyène : Gob Trotteur (445, plus rapide et plus fragile), Sarkapwane
  (465, Plante/Eau), Tortue Bleue (480).
- Muloubard : Milirat (440, plus rapide et moins robuste), Abrakne (495),
  Quartermac (490).

## Talents

| Emplacement | Chienchien Enragé / Leolhyène | Chienchien Noir / Muloubard |
|---|---|---|
| 1 | Prognathe (Strong Jaw) | Prognathe (Strong Jaw) |
| 2 | Impudence (Moxie) | Cran (Guts) |
| Caché | Colérique (Anger Point) | Chien de Garde (Guard Dog) |

- Prognathe : morsures ×1,5 (Morsure, Mâchouille, Croque Fort, Crocs Feu,
  Crocs Givre, Crochet Venin).
- Impudence : Att +1 à chaque K.O., le charognard qui s'emballe.
- Colérique : Att au maximum après un coup critique, d'où « Enragé ».
- Cran : Att ×1,5 sous altération de statut, le loubard qui encaisse.
- Chien de Garde : Intimidation augmente son Attaque, et il ne peut pas être
  forcé à changer.

## Kit final (niv. 40–50)

### Leolhyène

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB morsure | Mâchouille (Crunch) | Ténèbres | Phys. | 80 (120) | Peut baisser la Déf |
| Priorité | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 prio+1 | |
| Couverture | Crochet Venin (Poison Fang) | Poison | Phys. | 50 (75) | Couvre la Fée, sa faiblesse |
| Boost | Danse Lames (Swords Dance) | Normal | Statut | – | |

Alternatives : Croque Fort, Tricherie, Sabotage, Provoc, Crocs Feu / Givre,
Aiguisage.

### Muloubard

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB + soin | Vampi-Poing (Drain Punch) | Combat | Phys. | 75 | Le tank se soigne |
| Morsure | Mâchouille (Crunch) | Ténèbres | Phys. | 80 (120) | Couvre Psy et Spectre |
| Boost | Gonflette (Bulk Up) | Combat | Statut | – | Att et Déf +1 |
| Priorité | Mach Punch | Combat | Phys. | 40 prio+1 | |

Alternatives : Marto-Poing, Close Combat, Crocs Feu / Givre, Poings des
tuteurs, Hurlement.

(Puissance entre parenthèses : avec Prognathe.) Psycho-Croc écarté pour les
deux : peu cohérent avec des chiens.

## Capacités custom

Aucune.

## Learnsets

Les deux stades d'une famille partagent les attaques jusqu'au niveau 24 ; à
partir de l'évolution, les attaques sont exclusives au stade final
(`P_PRE_EVO_MOVES` à `FALSE`). Miroir : la hyène a Crocs Feu tôt et Crocs
Givre tard, le loup l'inverse ; boost au niveau 18 pour chacun.

### Chienchien Enragé → Leolhyène

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 4 | Bluff (Fake Out) | Normal | Phys. | 40 prio+3 |
| 8 | Grimace (Scary Face) | Normal | Statut | – |
| 11 | Morsure (Bite) | Ténèbres | Phys. | 60 (90) |
| 15 | Crochet Venin (Poison Fang) | Poison | Phys. | 50 (75) |
| 18 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 21 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 prio+1 |
| 24 | Crocs Feu (Fire Fang) | Feu | Phys. | 65 (97) |
| Évo | Croque Fort (Jaw Lock) | Ténèbres | Phys. | 80 (120) |
| 29 | Provoc (Taunt) | Ténèbres | Statut | – |
| 33 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 (120) |
| 37 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 41 | Crocs Givre (Ice Fang) | Glace | Phys. | 65 (97) |
| 45 | Sabotage (Knock Off) | Ténèbres | Phys. | 65 |
| 50 | Tricherie (Foul Play) | Ténèbres | Phys. | 95 |

Le Chienchien Enragé s'arrête au niveau 24 ; les attaques à partir de Évo
sont celles de Leolhyène.

### Chienchien Noir → Muloubard

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 4 | Éclate-Roc (Rock Smash) | Combat | Phys. | 40 |
| 8 | Rugissement (Growl) | Normal | Statut | – |
| 11 | Morsure (Bite) | Ténèbres | Phys. | 60 (90) |
| 15 | Vendetta (Revenge) | Combat | Phys. | 60 prio−4 |
| 18 | Gonflette (Bulk Up) | Combat | Statut | – |
| 21 | Casse-Brique (Brick Break) | Combat | Phys. | 75 |
| 24 | Crocs Givre (Ice Fang) | Glace | Phys. | 65 (97) |
| Évo | Vampi-Poing (Drain Punch) | Combat | Phys. | 75 |
| 29 | Mach Punch | Combat | Phys. | 40 prio+1 |
| 33 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 (120) |
| 37 | Marto-Poing (Hammer Arm) | Combat | Phys. | 100 |
| 41 | Crocs Feu (Fire Fang) | Feu | Phys. | 65 (97) |
| 45 | Hurlement (Roar) | Normal | Statut | – |
| 50 | Close Combat | Combat | Phys. | 120 |

Le Chienchien Noir s'arrête au niveau 24.

Morsure à 90 effectifs au niveau 11 : fort avant Roxanne (niv. 15), mais
Grahyèna a la même attaque au même moment. Points communs avec Gobet / Gob
Trotteur : Groz'Yeux, Coup Bas, Provoc, Danse Lames (rôle commun) ; Vive-Attaque
remplacée par Bluff pour s'en écarter.

## CT, CS et tuteurs

| Attaque | Enragé | Leolhyène | Noir | Muloubard |
|---|---|---|---|---|
| Toxik, Abri, Repos, Façade, Reflet, Attraction (CT) | ✅ | ✅ | ✅ | ✅ |
| Hurlement, Provoc, Tourmente, Larcin (CT) | ✅ | ✅ | ✅ | ✅ |
| Tunnel, Queue de Fer, Tomberoche (CT) | ✅ | ✅ | ✅ | ✅ |
| Force, Éclate-Roc (CS) | ✅ | ✅ | ✅ | ✅ |
| Plaquage, Damoclès, Éboulement, Coud'Boue (tuteurs) | ✅ | ✅ | ✅ | ✅ |
| Ténacité, Ronflement, Blabla Dodo, Vantardise (tuteurs) | ✅ | ✅ | ✅ | ✅ |
| Ultralaser (CT) | – | ✅ | – | ✅ |
| Coupe (CS), Aéropique (CT) | ✅ | ✅ | – | – |
| Danse Lames (tuteur) | ✅ | ✅ | – | – |
| Casse-Brique, Gonflette, Mitra-Poing (CT) | – | – | ✅ | ✅ |
| Poing Feu, Poing Glace, Poing Éclair, Ultimapoing, Ultimawashi, Dynamo-Poing, Riposte, Frappe Atlas (tuteurs) | – | – | ✅ | ✅ |
| Séisme (CT) | – | – | – | ✅ |

Exclus volontairement :
- Casse-Brique et Gonflette pour la famille Enragé, Danse Lames pour la
  famille Noir : chacune garde son boost et sa façon de frapper ;
- poings et Séisme pour la hyène, quadrupède ;
- toutes les attaques spéciales (Ball'Ombre…) ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée,
  Force Cachée.
