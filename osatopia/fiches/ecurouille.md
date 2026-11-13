# Famille Écurouille

> Rongeur des forêts, mi-écureuil mi-hérisson. Dans Dofus, le Prespic devient
> invisible, renvoie une partie des dégâts qu'il subit et entrave ses
> adversaires. *(Lore de mémoire, à vérifier : élément des sorts et zones.)*
> Évolution : Écurouille → Prespic (niv. 22).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_FAST` (comme Grignoui et Pachirisu) ; groupe d'œuf
`EGG_GROUP_FIELD` ; couleur `BODY_COLOR_BROWN`.

## Intention

Archétype : **perturbateur** + **mur qui punit le contact** · Références :
Noacier (Épine de Fer), Blindépique (Pico-Défense, hérisson), Grimalin (kit de
perturbateur) · Pourquoi : traduire les trois sorts du Prespic sans code de
combat nouveau.

| Mécanique Dofus | Traduction |
|---|---|
| Renvoi de dommages | Talent **Épine de Fer**, **Pico-Défense** à l'évolution, Riposte |
| Entrave | **Entrave**, Regard Noir, Provoc, Encore, Plaquage (paralysie), Cage Éclair (tuteur) |
| Invisibilité | **Reflet**, **Coup Bas** (frappe prioritaire « sans être vu »), Tunnel (CT), talent caché **Infiltration** |

Bonus écureuil/hérisson : Boul'Armure + Roulade, Dard-Nuée (piquants),
Bajoues.

## Stades

| | Écurouille | Prespic |
|---|---|---|
| Constante | `SPECIES_ECUROUILLE` | `SPECIES_PRESPIC` |
| Types | Normal | Normal |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 50 / 50 / 60 / 30 / 40 / 55 | 70 / 75 / 95 / 45 / 65 / 110 |
| Total | 285 | 460 |
| Évolution | niv. 22 | – |
| Talents | Épine de Fer / Bajoues / *Infiltration* | idem |
| Capture / Exp. | 190 / 60 | 75 / 168 |
| EV | Vit +1 | Déf +1, Vit +1 |

Stats sacrifiées : l'AtqSpé (il frappe et punit au contact) et l'Attaque,
moyenne : son rôle est de renvoyer et de bloquer, pas de frapper fort. La
Vitesse haute lui permet de placer Entrave ou Pico-Défense en premier.

Comparaisons (`similaires`) : Tauros et Écrémeuh (490, plus offensifs),
Volkorne (480, profil proche mais Insecte/Vol et mur physique).

## Kit final

| Emplacement | Choix | Alternatives |
|---|---|---|
| Renvoi | **Pico-Défense** (Plante, statut, prio +4) | Riposte, Abri |
| Entrave | **Entrave** (Normal, statut) | Regard Noir, Provoc, Encore |
| STAB | **Plaquage** (Normal, phys., 85, paralysie) | Coup d'Boule, Damoclès |
| Invisibilité / couverture | **Coup Bas** (Ténèbres, phys., 70, prio +1) | Reflet, Tunnel |

## Capacités custom

Aucune.

## Learnsets

### Écurouille
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Boul'Armure (Defense Curl) | Normal | Statut | – |
| 7 | Roulade (Rollout) | Roche | Phys. | 30 |
| 10 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 13 | Reflet (Double Team) | Normal | Statut | – |
| 16 | Dard-Nuée (Pin Missile) | Insecte | Phys. | 25 ×2–5 |
| 19 | Entrave (Disable) | Normal | Statut | – |
| 22 | Coup d'Boule (Headbutt) | Normal | Phys. | 70 |
| 26 | Coup Bas (Sucker Punch) | Ténèbres | Phys. | 70 |
| 30 | Regard Noir (Mean Look) | Normal | Statut | – |
| 34 | Plaquage (Body Slam) | Normal | Phys. | 85 |
| 38 | Provoc (Taunt) | Ténèbres | Statut | – |

### Prespic
Toutes les attaques d'Écurouille aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Pico-Défense (Spiky Shield) | Plante | Statut | – |
| 42 | Riposte (Counter) | Combat | Phys. | – |
| 46 | Encore (Encore) | Normal | Statut | – |
| 50 | Damoclès (Double-Edge) | Normal | Phys. | 120 |

## CT, CS et tuteurs

| Attaque | Écurouille | Prespic |
|---|---|---|
| CT : Toxik, Abri, Repos, Attraction, Façade, Reflet, Larcin, Provoc, Tourmente, Tunnel, Queue de Fer, Aéropique | ✓ | ✓ |
| CT : Ultralaser | | ✓ |
| CS : Coupe, Force, Éclate-Roc | ✓ | ✓ |
| Tuteurs : Plaquage, Riposte, Boul'Armure, Roulade, Cage Éclair, Éboulement, Taillade, Coud'Boue, Ténacité, Vantardise, Blabla Dodo, Ronflement | ✓ | ✓ |
| Tuteur : Damoclès | | ✓ |

Exclusions volontaires : Danse Lames (perturbateur, pas attaquant à boost),
Séisme (couverture trop large), Explosion, Toile Gluante et Fulmifer (ne
collent pas au physique), attaques spéciales (Ball'Ombre, Laser Glace…),
coups de poing, attaques inutilisables (Retour, Frustration, Puissance Cachée,
Force Cachée, Flash, Saisie).
