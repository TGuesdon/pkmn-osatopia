# Famille Marcacin

> Sangliers des forêts et des plaines d'Amakna qui chargent brutalement
> l'adversaire au corps à corps. *(Lore de mémoire, à vérifier : sorts
> surtout Terre ; Gligli correspondrait au « sanglier agressif »
> d'après sa constante.)*
> Évolutions : Marcacin → Sanglier (niv. 18) → Gligli (niv. 36).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Constantes : `SPECIES_MARCACIN`, `SPECIES_SANGLIER`,
`SPECIES_SANGLIER_AGRESSIF`.

Autres valeurs : `PERCENT_FEMALE(50)`, `.eggCycles = 15`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`, `EGG_GROUP_FIELD`,
`BODY_COLOR_BROWN`.

## Intention

Archétype : **tank offensif**, avec une pointe de **démolisseur**. Gligli
encaisse puis fonce tête baissée avec des charges à contrecoup, que ses
talents rendent plus fortes (Téméraire) ou gratuites (Tête de Roc, caché).

Références :
- **Ursaking** (Sol/Normal, 550) : même profil de tank lent qui frappe fort.
- **Rhinoféros** (Sol/Roche) : Tête de Roc et Téméraire, l'esprit « charge ».
- **Mammochon** (Glace/Sol) : le « cochon » Sol, Isograisse.

L'Attaque a été volontairement baissée et la Vitesse relevée par rapport
au premier jet (Att 120 → 110, Vit 55 → 65 chez Gligli) : avec Tête de
Roc, chaque point d'Attaque pèse plus lourd, et un monstre trop lent est
frustrant en aventure.

Se distingue de Roi bouftou (Normal, mur à PV, Att 87) et d'Abrakne
(Insecte/Ténèbres, attaquant). Évite Damoclès par niveau et Gonflette,
déjà appris par Roi bouftou et d'autres monstres custom.

## Stades

| | Marcacin | Sanglier | Gligli |
|---|---|---|---|
| Types | Normal | Normal / Sol | Normal / Sol |
| PV | 55 | 85 | 110 |
| Attaque | 56 | 85 | 110 |
| Défense | 55 | 85 | 110 |
| Atq. Spé | 25 | 30 | 35 |
| Déf. Spé | 38 | 60 | 80 |
| Vitesse | 31 | 55 | 65 |
| **Total** | **260** | **400** | **510** |
| Évolution | niv. 18 | niv. 36 | – |
| Talents | Téméraire / Isograisse / Tête de Roc (caché) | idem | idem |
| Capture / Exp. | 190 / 58 | 120 / 140 | 45 / 245 |
| EV | Att +1 | Att +1, Déf +1 | Att +2, Déf +1 |

Stats sacrifiées : l'AtqSpé (aucun sort, que des charges) et la Vitesse
(il charge fort mais tard).

En Normal/Sol, il craint l'Eau, la Plante, la Glace et le Combat ; il est
immunisé contre l'Électrik et le Spectre.

Comparaisons (outil `similaires`) :
- Marcacin : Parecool (280), Rongourmand (275).
- Sanglier : Ouvrifier (405), Tiboudet (385) ; côté Osatopia, Araknotron
  (398), profil proche mais types et kit différents.
- Gligli : Frison (490), Mastouffe (500) ; côté Osatopia, Abrakne (495) et
  Roi bouftou (530).

## Talents

| Emplacement | Talent | Effet |
|---|---|---|
| 1 | Téméraire (Reckless) | +20 % aux attaques à contrecoup, qu'il subit toujours |
| 2 | Isograisse (Thick Fat) | Dégâts Feu et Glace divisés par deux ; couvre sa faiblesse Glace |
| Caché | Tête de Roc (Rock Head) | Plus de contrecoup ; rare, pour ne pas déséquilibrer l'aventure |

Écarté : Benêt (Oblivious), alternative possible à Isograisse.

## Kit final (Gligli, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Normal (charge) | Peignée (Head Charge) | Normal | Phys. | 120 | Coup de tête, contrecoup 25 % ; inédit chez les custom |
| STAB Sol | Cavalerie Lourde (High Horsepower) | Sol | Phys. | 95 | Fiable, sans effet secondaire ; inédit chez les custom |
| Couverture | Tête de Fer (Iron Head) | Acier | Phys. | 80 | Apeure 30 % ; touche Glace, Roche, Fée |
| Boost | Grondement (Howl) | Normal | Statut | – | +1 Att, le grognement avant la charge |

Alternatives dans le learnset ou en CT : Coud'Krâne, Bélier, Damoclès,
Assaut Frontal (Sanglier seulement), Séisme, Trépignement, Éboulement,
Hurlement, Ténacité.

## Capacités custom

Aucune.

## Learnsets

### Marcacin

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Grondement (Howl) | Normal | Statut | – |
| 11 | Piétisol (Bulldoze) | Sol | Phys. | 60 |
| 16 | Coup d'Boule (Headbutt) | Normal | Phys. | 70 |
| 21 | Hurlement (Roar) | Normal | Statut | – |
| 25 | Bélier (Take Down) | Normal | Phys. | 90 |
| 29 | Tête de Fer (Iron Head) | Acier | Phys. | 80 |
| 33 | Tunnel (Dig) | Sol | Phys. | 80 |
| 37 | Ténacité (Endure) | Normal | Statut | – |

### Sanglier

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Trépignement (Stomping Tantrum) | Sol | Phys. | 75 |
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Grondement (Howl) | Normal | Statut | – |
| 11 | Piétisol (Bulldoze) | Sol | Phys. | 60 |
| 16 | Coup d'Boule (Headbutt) | Normal | Phys. | 70 |
| 21 | Hurlement (Roar) | Normal | Statut | – |
| 25 | Bélier (Take Down) | Normal | Phys. | 90 |
| 29 | Tête de Fer (Iron Head) | Acier | Phys. | 80 |
| 33 | Tunnel (Dig) | Sol | Phys. | 80 |
| 37 | Ténacité (Endure) | Normal | Statut | – |
| 41 | Assaut Frontal (Headlong Rush) | Sol | Phys. | 120 |
| 46 | Cavalerie Lourde (High Horsepower) | Sol | Phys. | 95 |

Assaut Frontal est **exclusif à Sanglier** (`P_PRE_EVO_MOVES` à `FALSE`) :
une récompense pour qui retarde l'évolution, au prix d'une baisse de
Défense et de Défense Spéciale.

### Gligli

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Cavalerie Lourde (High Horsepower) | Sol | Phys. | 95 |
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 5 | Grondement (Howl) | Normal | Statut | – |
| 11 | Piétisol (Bulldoze) | Sol | Phys. | 60 |
| 16 | Coup d'Boule (Headbutt) | Normal | Phys. | 70 |
| 21 | Hurlement (Roar) | Normal | Statut | – |
| 25 | Bélier (Take Down) | Normal | Phys. | 90 |
| 29 | Tête de Fer (Iron Head) | Acier | Phys. | 80 |
| 33 | Tunnel (Dig) | Sol | Phys. | 80 |
| 37 | Ténacité (Endure) | Normal | Statut | – |
| 42 | Peignée (Head Charge) | Normal | Phys. | 120 |
| 48 | Coud'Krâne (Skull Bash) | Normal | Phys. | 130 |

Piétisol (60) au niveau 11, utile contre Roxanne. Bélier (90) au niveau
25, compensé par son contrecoup ; rien d'autre à 90+ avant le niveau 36.
Peignée juste avant Lévy & Tatia. Recoupements avec Roi bouftou limités à
Coup d'Boule et Bélier (demandés), à des niveaux différents.

Écartés : Fracass'Tête (150 sans contrecoup avec Tête de Roc), Damoclès
par niveau (déjà chez Roi bouftou, gardé en tuteur), Flair (inutilisable),
Coud'Boue par niveau (spécial).

## CT, CS et tuteurs

| | Marcacin | Sanglier | Gligli |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet (CT) | ✅ | ✅ | ✅ |
| Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✅ | ✅ | ✅ |
| Larcin (CT) : il fouille et chaparde | ✅ | ✅ | ✅ |
| Force, Éclate-Roc (CS) | ✅ | ✅ | ✅ |
| Hurlement, Tunnel (CT) : avant leur niveau | ✅ | ✅ | ✅ |
| Plaquage, Damoclès (tuteurs) : d'autres charges | ✅ | ✅ | ✅ |
| Coud'Boue (tuteur) : il se roule dans la boue | ✅ | ✅ | ✅ |
| Roulade (tuteur) : il dévale les pentes | ✅ | ✅ | ✅ |
| Tomberoche (CT) : couverture contre Vol | ✅ | ✅ | ✅ |
| Éboulement (tuteur) : couverture contre Vol | – | ✅ | ✅ |
| Tempête de Sable (CT) : le Sol l'immunise | – | ✅ | ✅ |
| Séisme (CT) | – | ✅ | ✅ |

Exclus volontairement :
- Danse Lames : Peignée et Coud'Krâne à +2, trop fort ; Grondement reste
  son seul boost ;
- Gonflette : déjà chez plusieurs custom, garde son identité ;
- Queue de Fer : pas de coups de queue ;
- Casse-Brique, Ultimapoing, Poing Feu, Poing Glace, Poing Éclair,
  Dynamo-Poing, Ultimawashi, Riposte : ni poings ni coups de pied ;
- Ultralaser, Surf et toutes les attaques spéciales : AtqSpé à 25–35 ;
- inutilisables : Retour, Frustration, Puissance Cachée, Force Cachée,
  Saisie, Flash.
