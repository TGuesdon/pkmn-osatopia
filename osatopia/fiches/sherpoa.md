# Famille Sherpoa

> Monstre des mines et des carrières, qui trimballe des pierres dans son sac
> (lore Dofus **à vérifier** : élément des sorts et zone exacts). Un seul
> stade, pas d'évolution.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Aucun code de combat.

Constante : `SPECIES_SHERPOA`. Le monstre existe en placeholder dans
`src/data/pokemon/species_info.h` (Plante, 10 partout).

Valeurs non choisies, reprises de la famille Wabbit et de Gigalithe :
`PERCENT_FEMALE(50)`, `.eggCycles = 15`, `STANDARD_FRIENDSHIP`,
`GROWTH_MEDIUM_SLOW`, groupe d'œuf `EGG_GROUP_MINERAL`, couleur
`BODY_COLOR_BROWN` (à ajuster selon le sprite).

## Intention

Archétype : **attaquant physique rapide** (Roche), avec un volet **poseur de
pièges** (Piège de Roc, Tempête de Sable). Il pose ses pierres, monte sa
vitesse avec Poliroche, puis frappe.

Références : **Gigalithe** (Roche, 515) pour le physique de porteur de
rochers, **Absol** (465) et **Mysdibule** (380) pour la place dans la
progression d'un monstre unique et rare. Se distingue de Milirat (profil de
stats proche, mais Normal/Ténèbres, plus rapide et plus gros en PV) par son
kit Roche, ses pièges et sa météo.

Placement : monstre de mine, sans évolution, total 420.

## Stades

| | Sherpoa |
|---|---|
| Types | Roche |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 70 / 100 / 80 / 40 / 55 / 75 |
| Total | **420** |
| Talents | Fermeté / Porte-Roche · caché : Force Sable |
| Capture / Exp. | 60 / 150 |
| EV | Att 2, Vit 1 |

Stats sacrifiées : AtqSpé (40), car c'est un porteur physique, et DéfSpé
(55), qui le rend fragile face au spécial. Faiblesses Roche : Eau, Plante,
Combat, Sol, Acier.

## Talents

| Talent | Constante | Intérêt |
|---|---|---|
| **Fermeté** (Sturdy) | `ABILITY_STURDY` | Survit à 1 PV, utile avec PV 70 et DéfSpé 55. |
| **Porte-Roche** (Rocky Payload) | `ABILITY_ROCKY_PAYLOAD` | +50 % aux attaques Roche, colle au sac de pierres. |
| **Force Sable** (Sand Force), caché | `ABILITY_SAND_FORCE` | +30 % Roche, Sol, Acier sous tempête de sable. |

## Kit final (niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB principal | Lame de Roc (Stone Edge) | Roche | Phys. | 100 |
| Piège | Piège de Roc (Stealth Rock) | Roche | Statut | – |
| Couverture | Séisme (Earthquake) | Sol | Phys. | 100 |
| Boost | Poliroche (Rock Polish) | Roche | Statut | – |

Variante poseur pur : Tempête de Sable à la place de Poliroche. Éboulement
reste l'alternative fiable à Lame de Roc.

Exclues volontairement : Orage Adamantin et Hache de Pierre (incohérentes
avec le monstre), y compris des CT et tuteurs.

## Capacités custom

Aucune.

## Learnsets

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 5 | Jet-Pierres (Rock Throw) | Roche | Phys. | 50 |
| 9 | Vif Roc (Accelerock) | Roche | Phys. | 40 (prio +1) |
| 13 | Tomberoche (Rock Tomb) | Roche | Phys. | 60 |
| 17 | Piège de Roc (Stealth Rock) | Roche | Statut | – |
| 21 | Coup d’Boule (Headbutt) | Normal | Phys. | 70 |
| 25 | Éboulement (Rock Slide) | Roche | Phys. | 75 |
| 29 | Poliroche (Rock Polish) | Roche | Statut | – |
| 33 | Piétisol (Bulldoze) | Sol | Phys. | 60 |
| 37 | Tempête de Sable (Sandstorm) | Roche | Statut | – |
| 41 | Séisme (Earthquake) | Sol | Phys. | 100 |
| 45 | Lame de Roc (Stone Edge) | Roche | Phys. | 100 |
| 49 | Tunnel (Dig) | Sol | Phys. | 80 |

Rien de fort trop tôt : Éboulement (75) au niv. 25, les attaques à 100 aux
niv. 41 et 45. Le kit complet est là avant Lévy & Tatia (niv. 42). Piège de
Roc au niv. 17 est tôt ; il peut passer à 21–25 si besoin.

## CT, CS et tuteurs

| Source | Attaques |
|---|---|
| CT (socle) | Toxik, Abri, Repos, Reflet, Provoc, Façade, Attraction, Hurlement, Tourmente |
| Tuteurs (socle) | Blabla Dodo, Ténacité, Vantardise |
| CT (couverture) | Casse-Brique, Queue de Fer, Larcin (facultatif) |
| Tuteur (couverture) | Plaquage |
| CS | Force, Éclate-Roc |

Exclusions volontaires :
- **Séisme et Tunnel (CT)** : le learnset les donne aux niv. 41 et 49 ; les
  CT casseraient ce rythme.
- **Éboulement, Tomberoche, Tempête de Sable** : déjà au learnset.
- **Poing Feu, Poing Glace** : retirés (ne collent pas au monstre).
- **Danse Lames** : Poliroche suffit comme boost.
- **Zénith, Grêle, Danse Pluie** : hors thème d'un mineur.
- **Explosion, Mitra-Poing, Ultralaser** : trop puissantes ou hors thème.
- **Boul’Armure, Roulade** : inutiles à un attaquant.
- **Coupe, Vol, Surf, Cascade, Plongée** : pas de sens pour ce monstre.
