# Famille Soldalia

> Soldats de pierre animés, liés aux plantes et aux fleurs (lore Dofus
> **à vérifier** : élément des sorts, zone, lien exact avec les fleurs).
> Évolutions : Soldalia → Coquelicogne (niv. 20) → Cameliache (niv. 36).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Aucun code de combat.

Constantes : `SPECIES_SOLDALIA`, `SPECIES_COQUELICOGNE`,
`SPECIES_CAMELIACHE` (placeholders existants).

Valeurs non choisies explicitement, adaptées à des golems animés (comme
Golemastoc) plutôt que reprises de Bitouf : asexués (`MON_GENDERLESS`),
`.eggCycles = 25`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`, groupe
d'œuf `EGG_GROUP_MINERAL`, couleur `BODY_COLOR_BROWN` (à ajuster selon le
sprite).

## Intention

Archétype : **tank offensif** (bulky attacker), lent, avec un volet
**Distorsion** facultatif. Il s'enracine (Racines), encaisse, et frappe de
plus en plus fort (Poing de Colère).

Références : **Golemastoc** (Sol/Spectre, golem animé spectral),
**Gigalithe** (Roche, gros caillou lent), **Bourrinos** (profil de stats
quasi identique au stade final).

Pourquoi : premier Spectre d'Osatopia, et le Roche/Spectre n'existe chez
aucun Pokémon officiel. Le twist plante passe par Racines, Tambour Battant,
Balle Graine et le talent caché Herbivore.

Distinction avec la future famille **Craqueleur** (Roche pur, même
archétype) : Soldalia est le côté offensif et spectral. **Aucune attaque
Sol** (ni par niveau, ni par CT, ni par tuteur), et **pas de Lame de Roc**,
laissées à Craqueleur.

## Stades

| | Soldalia | Coquelicogne | Cameliache |
|---|---|---|---|
| Types | Roche/Spectre | Roche/Spectre | Roche/Spectre |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 60 / 72 / 62 / 30 / 46 / 25 | 80 / 98 / 82 / 40 / 62 / 33 | 93 / 128 / 105 / 50 / 82 / 40 |
| Total | **295** | **395** | **498** |
| Talents | Fermeté / Corps Maudit · caché : Herbivore | idem | idem |
| Capture / Exp. | 190 / 62 | 100 / 142 | 45 / 240 |
| EV | Att 1 | Att 2 | Att 2, Déf 1 |

Stats sacrifiées : AtqSpé (inutile, kit 100 % physique) et Vitesse (défaut
assumé, compensé par Grimace, Ombre Portée et Distorsion).

Faiblesses Roche/Spectre : Eau, Plante, Sol, Acier, Spectre, Ténèbres.
Immunités : Normal, Combat.

## Talents

| Talent | Constante | Intérêt |
|---|---|---|
| **Fermeté** (Sturdy) | `ABILITY_STURDY` | Le soldat qui tient debout. |
| **Corps Maudit** (Cursed Body) | `ABILITY_CURSED_BODY` | Le côté spectral. |
| **Herbivore** (Sap Sipper), caché | `ABILITY_SAP_SIPPER` | Twist plante : annule sa faiblesse Plante et monte son Attaque. |

## Kit final (niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB Spectre | Poing de Colère (Rage Fist) | Spectre | Phys. | 50+ |
| STAB Roche | Hache de Pierre (Stone Axe) | Roche | Phys. | 65 (pose Piège de Roc) |
| Soin / tenue | Racines (Ingrain) | Plante | Statut | – |
| Boost | Gonflette (Bulk Up) | Combat | Statut | – |

Variantes : Lame Puissante ou Esprit Frappeur pour plus de puissance,
Distorsion pour une équipe Trick Room, Tambour Battant / Poing Éclair /
Poing Glace en couverture.

Exclue : **Malédiction**, qui devient la version Spectre (sacrifice de PV).

## Capacités custom

Aucune.

## Learnsets

### Soldalia

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Étonnement (Astonish) | Spectre | Phys. | 30 |
| 1 | Grimace (Scary Face) | Normal | Statut | – |
| 5 | Jet-Pierres (Rock Throw) | Roche | Phys. | 50 |
| 8 | Ombre Portée (Shadow Sneak) | Spectre | Phys. | 40 (prio +1) |
| 11 | Racines (Ingrain) | Plante | Statut | – |
| 14 | Tomberoche (Rock Tomb) | Roche | Phys. | 60 |
| 17 | Poing Ombre (Shadow Punch) | Spectre | Phys. | 60 |

### Coquelicogne

Reprend les attaques de Soldalia aux mêmes niveaux, plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Tambour Battant (Drum Beating) | Plante | Phys. | 80 |
| 22 | Gonflette (Bulk Up) | Combat | Statut | – |
| 26 | Éboulement (Rock Slide) | Roche | Phys. | 75 |
| 30 | Poing de Colère (Rage Fist) | Spectre | Phys. | 50+ |
| 33 | Mur de Fer (Iron Defense) | Acier | Statut | – |

### Cameliache

Reprend les attaques de Coquelicogne aux mêmes niveaux (Tambour Battant au
niv. 1), plus :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Hache de Pierre (Stone Axe) | Roche | Phys. | 65 |
| 38 | Hantise (Phantom Force) | Spectre | Phys. | 90 |
| 42 | Distorsion (Trick Room) | Psy | Statut | – |
| 46 | Lame Puissante (Mighty Cleave) | Roche | Phys. | 95 |
| 50 | Esprit Frappeur (Poltergeist) | Spectre | Phys. | 110 |

Hache de Pierre est exclusive à Cameliache (le seul des trois qui porte une
hache). Rien au-dessus de 80 avant le niv. 36.

## CT, CS et tuteurs

| Source | Attaques | Stades |
|---|---|---|
| CT (socle) | Toxik, Abri, Repos, Reflet, Façade, Attraction, Provoc, Tourmente, Larcin, Hurlement | tous |
| Tuteurs (socle) | Blabla Dodo, Ronflement, Ténacité, Vantardise | tous |
| CT (thème) | Tempête de Sable, Gonflette, Balle Graine | tous |
| CT (couverture) | Casse-Brique | tous |
| Tuteurs (couverture) | Poing Éclair, Poing Glace, Riposte, Danse Lames | tous |
| CS | Force, Éclate-Roc | tous |
| CS | Coupe | Cameliache |

Exclusions volontaires :
- **Séisme, Tunnel, Coud'Boue** : Sol, réservé à Craqueleur.
- **Tomberoche, Éboulement** : déjà au learnset.
- **Ball'Ombre, Lance-Soleil, Giga-Sangsue, Ultralaser** : spéciales, AtqSpé 50.
- **Poing Feu** : Éclair et Glace couvrent mieux ses faiblesses.
- **Explosion, Mitra-Poing, Dynamo-Poing** : trop puissantes ou hors thème.
- **Plaquage, Damoclès** : couverture Normal redondante.
- **Queue de Fer, Aile d'Acier, Vol, Surf, Cascade, Plongée, Zénith,
  Danse Pluie, Grêle** : pas de sens pour ce monstre.
