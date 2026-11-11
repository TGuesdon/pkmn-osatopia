# Famille Sousouris

> Les Milirats Strubiens hantent les Égouts d'Astrub (niv. 22–30). Ils
> frappent avec *Lancer de Lance* (Eau, à distance, vole 1 de portée) et
> *Air Empoisonné* (Air, zone en croix, repousse). Le Sousouris n'existe que
> comme monstre de quête (*Morsure*, Terre).
> Évolutions : Sousouris → Milirat (niv. 18).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Refonte d'une première version (Puanteur/Fuite, learnset commun aux deux
stades avec Poursuite et Feinte inutilisables, EV AtqSpé sur Milirat).
Croissance (moyenne-rapide), groupe d'œuf (Terrestre), couleur (gris),
sexe 50 % et cycles d'œuf (15) sont conservés.

## Intention

Archétype : **perturbateur lancier**. Sousouris est un **remplissage de
route** de début de jeu. Une fois évolué, Milirat a pris sa lance : il frappe
sans contact (Longue Portée), verrouille l'adversaire avec Provoc et
Exécu-Son, punit l'attaquant avec Coup Bas et transperce les Fée avec
Estocorne.

Références : **Rattatac d'Alola** (même typage, rongeur, Coup Bas, Croc de
Mort), **Fouinar** (rongeur de début de jeu, PV et Vitesse). L'attaque
**Estocorne** (« transperce la cible ») incarne la lance.

Il se démarque des autres attaquants Ténèbres custom (Léolhyène 455 et Gob
Trotteur 445, rapides et offensifs) : moins d'Attaque, nettement moins de
Vitesse, plus de robustesse, et un kit tourné vers la gêne.

## Stades

| | Sousouris | Milirat |
|---|---|---|
| Types | Normal | Normal/Ténèbres |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 45 / 52 / 40 / 30 / 38 / 50 | 78 / 92 / 70 / 40 / 65 / 80 |
| Total | 255 | 425 |
| Talents | Fuite / Regard Vif / *Agitation* | Longue Portée / Regard Vif / *Agitation* |
| Évolution | niv. 18 | – |
| Capture / Exp. | 255 / 56 | 90 / 147 |
| EV | Att +1 | Att +2 |

Stat sacrifiée : l'AtqSpé (lancier purement physique).

Comparaisons (`similaires`) : Ratentif (255) et Skitty (260) pour Sousouris,
Corbac (260) côté Osatopia ; Grahyèna (420) et Badabouin (420) pour Milirat,
Araknotron (398, Vit 60) côté Osatopia.

## Kit final

| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB principal | Exécu-Son (Throat Chop) | Ténèbres | Phys. | 80 |
| Priorité | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 |
| Couverture lance | Estocorne (Smart Strike) | Acier | Phys. | 70 |
| Utilitaire | Provoc (Taunt) | Ténèbres | Statut | – |

Alternatives : Sabotage, Croc de Mort, Danse Lames, Direct Toxik,
Hyperceuse, Ruse.

Talents : **Longue Portée** (aucune attaque ne fait contact : pas de Statik,
Peau Dure ni Pico-Défense) ; **Agitation** en talent caché, compensée par
Estocorne qui ne rate jamais.

## Capacités custom

Aucune. Piste écartée : un *Lancer de Lance* Ténèbres sans contact qui
baisse la précision.

## Learnsets

### Sousouris

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Vive-Attaque (Quick Attack) | Normal | Phys. | 40 |
| 7 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 10 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 13 | Grimace (Scary Face) | Normal | Statut | – |
| 16 | Assurance | Ténèbres | Phys. | 60 |
| 19 | Provoc (Taunt) | Ténèbres | Statut | – |
| 22 | Croc de Mort (Hyper Fang) | Normal | Phys. | 80 |
| 26 | Sabotage (Knock Off) | Ténèbres | Phys. | 65 |
| 30 | Croc Fatal (Super Fang) | Normal | Phys. | – |
| 34 | Damoclès (Double-Edge) | Normal | Phys. | 120 |

### Milirat

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Estocorne (Smart Strike) | Acier | Phys. | 70 |
| 1 | Ruse (Feint) | Normal | Phys. | 30 |
| 1–16 | base commune (Charge → Assurance) | | | |
| 20 | Provoc (Taunt) | Ténèbres | Statut | – |
| 23 | Croc de Mort (Hyper Fang) | Normal | Phys. | 80 |
| 26 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 |
| 30 | Sabotage (Knock Off) | Ténèbres | Phys. | 65 |
| 33 | Exécu-Son (Throat Chop) | Ténèbres | Phys. | 80 |
| 37 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 41 | Direct Toxik (Poison Jab) | Poison | Phys. | 80 |
| 45 | Hyperceuse (Hyper Drill) | Normal | Phys. | 100 |

Temporisation : un Sousouris qu'on ne fait pas évoluer garde Croc Fatal et
Damoclès ; Milirat reçoit la lance (Estocorne, Hyperceuse) et Coup Bas.

## CT, CS et tuteurs

| Attaque | Source | Sousouris | Milirat |
|---|---|---|---|
| Toxik, Provoc, Tourmente, Abri, Repos, Façade, Reflet, Attraction, Larcin, Danse Pluie | CT | ✓ | ✓ |
| Tunnel, Queue de Fer, Tomberoche | CT | ✓ | ✓ |
| Coupe, Éclate-Roc, Force | CS | ✓ | ✓ |
| Coud'Boue, Ténacité, Blabla Dodo, Ronflement, Vantardise, Plaquage | Tuteur | ✓ | ✓ |
| Damoclès | Tuteur | ✓ | ✗ |
| Aéropique, Faux-Chage | CT | – | ✓ |
| Taillade, Éboulement | Tuteur | – | ✓ |

Exclusions volontaires : Damoclès pour Milirat (récompense du Sousouris non
évolué), Danse Lames par tuteur (garde le timing du niv. 37), poings et
Casse-Brique (il tient une lance), Séisme, et toutes les attaques spéciales,
Ultralaser compris (AtqSpé 40).
