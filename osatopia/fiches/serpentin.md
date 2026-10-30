# Famille Serpentin

> Petit serpent venimeux ; le Serpiplume est un grand serpent aux anneaux de
> pierre, coiffé d'une crête de plumes rouges. *(Lore de mémoire, à vérifier :
> éléments des sorts et zone des deux monstres.)*
> Évolutions : Serpentin → Serpiplume (niv. 40).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupes d'œuf
`EGG_GROUP_FIELD` + `EGG_GROUP_DRAGON` (comme Abo et Arbok), couleurs
`BODY_COLOR_GREEN` (Serpentin) et `BODY_COLOR_GRAY` (Serpiplume) d'après les
sprites.

## Intention

Archétype : **attaquant physique qui se renforce** (wallbreaker). Serpiplume
encaisse un coup grâce à sa Défense, se booste avec Poliroche, puis frappe très
fort. En fin d'aventure, Fracass'Tête sans contrecoup (talent caché Tête de
Roc) devient sa mécanique signature.

Références : **Arbok** (attaquant physique moyen et assez rapide,
Intimidation, Mue, Regard Médusant, crocs) et **Dunaconda** (corps de pierre,
Défense élevée, Mue, Enroulement).

Poison au premier stade, Poison/Roche au stade final, une combinaison inédite
chez les monstres custom. Faiblesses : Sol ×4, Eau, Acier, Psy. Résistances :
Poison ×4, Normal, Feu, Vol, Insecte, Fée.

Évolution tardive (niv. 40, après Alizée et avant Lévy & Tatia) : Serpentin
reste un petit serpent sans attaque Roche ; la pierre n'arrive qu'avec
l'évolution.

## Stades

| | Serpentin | Serpiplume |
|---|---|---|
| Types | Poison | Poison/Roche |
| PV | 55 | 80 |
| Attaque | 75 | 120 |
| Défense | 60 | 100 |
| Atq. Spé | 35 | 45 |
| Déf. Spé | 50 | 65 |
| Vitesse | 65 | 90 |
| **Total** | **340** | **500** |
| Évolution | niv. 40 | – |
| Capture / Exp. | 120 / 70 | 45 / 215 |
| EV | Att +1 | Att +2 |

Stats sacrifiées : l'AtqSpé (attaquant purement physique) et la DéfSpé, son
point faible face aux attaques Eau et Psy spéciales.

Comparaisons (outil `similaires`) :
- Serpentin : Grondogue (340), Crabagarre (338) ; côté Osatopia, Raphaela
  (310) et Bwak Terre (310), plus faibles.
- Serpiplume : Vrombotor (500), Hachécateur (500), Dogrino (505) ; côté
  Osatopia, Kwak Terre (500) et Abrakne (495), plus lents et plus endurants.

## Talents

| Emplacement | Serpentin | Serpiplume |
|---|---|---|
| 1 | Intimidation (Intimidate) | Intimidation (Intimidate) |
| 2 | Mue (Shed Skin) | Mue (Shed Skin) |
| Caché | Tête de Roc (Rock Head) | Tête de Roc (Rock Head) |

- Intimidation : héritage d'Arbok.
- Mue : talent commun à Arbok et Dunaconda.
- Tête de Roc : annule le contrecoup de Fracass'Tête et de Damoclès.
- Écartés : Impudence, Expul'Sable, Toxitouche.

## Kit final (Serpiplume, niv. 40–55)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Roche | Fracass'Tête (Head Smash) | Roche | Phys. | 150 | Sans contrecoup avec Tête de Roc |
| STAB Poison | Direct Toxik (Poison Jab) | Poison | Phys. | 80 | Peut empoisonner |
| Boost | Poliroche (Rock Polish) | Roche | Statut | – | Vitesse +2 |
| Couverture | Séisme (Earthquake, CT) | Sol | Phys. | 100 | Contre l'Acier, qui résiste à ses deux STAB |

Alternatives : Lame de Roc, Éboulement, Mâchouille, Regard Médusant, Toupie
Éclat, Queue de Fer, Enroulement (s'il a été appris par Serpentin).

Écartées : Crash Toxique (attaque signature sans description), Griffes
Funestes (pas de griffes), Détricanon (déjà chez Shin Larve).

## Capacités custom

Aucune.

## Learnsets

### Serpentin

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Ligotage (Wrap) | Normal | Phys. | 15 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 4 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 9 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 12 | Regard Médusant (Glare) | Normal | Statut | – |
| 15 | Queue-Poison (Poison Tail) | Poison | Phys. | 50 |
| 21 | Crochet Venin (Poison Fang) | Poison | Phys. | 50 |
| 24 | Grincement (Screech) | Normal | Statut | – |
| 28 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 32 | Direct Toxik (Poison Jab) | Poison | Phys. | 80 |
| 42 | Enroulement (Coil) | Poison | Statut | – |

Enroulement est exclusif à Serpentin (`P_PRE_EVO_MOVES` à `FALSE`) et arrive
après le niveau d'évolution : une récompense pour qui retarde l'évolution.

### Serpiplume

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Éboulement (Rock Slide) | Roche | Phys. | 75 |
| 1 | Ligotage (Wrap) | Normal | Phys. | 15 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 4 | Dard-Venin (Poison Sting) | Poison | Phys. | 15 |
| 9 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 12 | Regard Médusant (Glare) | Normal | Statut | – |
| 15 | Queue-Poison (Poison Tail) | Poison | Phys. | 50 |
| 21 | Crochet Venin (Poison Fang) | Poison | Phys. | 50 |
| 24 | Grincement (Screech) | Normal | Statut | – |
| 28 | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 32 | Direct Toxik (Poison Jab) | Poison | Phys. | 80 |
| 43 | Poliroche (Rock Polish) | Roche | Statut | – |
| 46 | Lame de Roc (Stone Edge) | Roche | Phys. | 100 |
| 50 | Toupie Éclat (Mortal Spin) | Poison | Phys. | 30 |
| 55 | Fracass'Tête (Head Smash) | Roche | Phys. | 150 |

Rien à 90+ avant le niveau 46. Points communs avec les autres monstres
custom : Groz'Yeux et Morsure ; Mâchouille et Crochet Venin existent ailleurs
mais pas dans cet enchaînement. Jet-Pierres retiré : Serpentin est un tout
petit serpent, la pierre n'arrive qu'à l'évolution.

## CT, CS et tuteurs

| | Serpentin | Serpiplume |
|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet (CT) | ✅ | ✅ |
| Zénith, Danse Pluie (CT) | ✅ | ✅ |
| Provoc, Tourmente, Larcin (CT) | ✅ | ✅ |
| Tomberoche, Tempête de Sable, Tunnel (CT) | ✅ | ✅ |
| Séisme (CT) : couvre l'Acier | ✅ | ✅ |
| Queue de Fer (CT) : couvre Fée et Glace | ✅ | ✅ |
| Force, Éclate-Roc (CS) | ✅ | ✅ |
| Plaquage, Damoclès, Roulade, Boul'Armure, Coud'Boue (tuteurs) | ✅ | ✅ |
| Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✅ | ✅ |
| Ultralaser (CT) | – | ✅ |
| Éboulement (tuteur) | – | ✅ |

Exclus volontairement :
- Bombe Beurk : spéciale ;
- Danse Lames : Poliroche et Enroulement suffisent comme boosts ;
- les poings (Mitra-Poing, tuteurs), Coupe, Aile d'Acier, Aéropique : pas de
  membres ni d'ailes ;
- Surf, Plongée, Cascade : pas un serpent d'eau ;
- Éboulement pour Serpentin : la pierre n'arrive qu'à l'évolution ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée,
  Force Cachée.
