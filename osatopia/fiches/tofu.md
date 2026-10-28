# Famille Tofu

> Petit oiseau jaune de l'élément Air, très rapide et fragile, croisé dès le
> début de l'aventure (Incarnam, Astrub). Le Tofu ventripotent est sa version
> engraissée ; le Tofu Royal est le boss du donjon des Tofus.
> Évolutions : Tofu → Gwotofu (niv. 16) → Tofu Royal (niv. 32).
> Maletofu (Tofu maléfique) est une espèce à part.

**État : en cours.** Étapes 1 à 4 validées (identité, références, archétype,
stats). Restent : kit final, learnsets, CT, catch rate / exp, zone de capture.

## Intention

Une famille qui **change de rôle à chaque stade** :

| Stade | Rôle | Archétype |
|---|---|---|
| Tofu | Nuisible rapide : frappe le premier, gêne avec des attaques de statut | Perturbateur |
| Gwotofu | Devenu trop gros : lent et robuste, cloué au sol | Tank offensif / mur physique |
| Tofu Royal | Équilibré, retrouve sa vitesse | Polyvalent, orienté physique |

Références : Nirondelle et Étourmi (oiseau de route), Scorvol (Sol/Vol),
Roucarnage (oiseau équilibré). Il doit rester distinct de la famille Bitouf
(oiseau rapide avec Turbo) : Tofu Royal est moins rapide que Bitouvol, et le
Tofu se distingue de Bebitouf par son kit de statut plutôt qu'offensif.

## Mécanique : temporiser l'évolution de Gwotofu

Gwotofu apprend des attaques Sol **à un niveau supérieur à celui de son
évolution** (32). Le joueur peut annuler l'évolution quelques niveaux pour les
obtenir, puis les garder une fois devenu Tofu Royal.

Première esquisse, à affiner à l'étape du learnset :
- Piétisol (Bulldoze, 60) vers le niv. 20 ;
- Picots (Spikes) et Amass'Sable (Shore Up) avant le niv. 32 ;
- **Séisme (Earthquake, 100) au niv. 36** : la récompense de la temporisation.

Sur un Tofu Royal Vol pur, Séisme est une couverture précieuse contre
Électrik, Roche et Acier.

Contraintes techniques :
- `P_PRE_EVO_MOVES` est à `FALSE` (`include/config/summary_screen.h`) :
  Tofu Royal ne peut pas réapprendre les attaques de Gwotofu. ✅
- Ne **pas** donner ces attaques Sol (notamment Séisme) à Tofu Royal dans ses
  CT, sinon la mécanique perd son intérêt.

Clin d'œil possible : Atterrissage (Roost) retire le type Vol pendant un tour,
Tofu Royal redevient brièvement « cloué au sol » comme Gwotofu.

## Stades

| | Tofu | Gwotofu | Tofu Royal |
|---|---|---|---|
| Types | Vol | Sol / Vol | Vol |
| PV | 35 | 85 | 85 |
| Attaque | 45 | 70 | 90 |
| Défense | 30 | 85 | 80 |
| Atq. Spé | 30 | 35 | 70 |
| Déf. Spé | 30 | 65 | 75 |
| Vitesse | 80 | 30 | 95 |
| **Total** | **250** | **370** | **495** |
| Évolution | niv. 16 | niv. 32 | – |

Comparaisons (outil `similaires`) :
- Tofu : Nirondelle (270), Rattata (253) ; côté Osatopia, Bebitouf (250).
  Option si on veut les séparer davantage : Tofu à 30 PV / 85 Vit.
- Gwotofu : Amassel (355), Excelangue (385), Hippopotas (330) ; Shin Larve (370).
- Tofu Royal : Roucarnage (479), Manternel (500) ; Bitouvol (523).
  Repère Sol/Vol : Scorvol 75/95/125/45/75/95 (510).

## Talents

Le talent se transmet par emplacement à l'évolution, d'où trois lignées :

| Emplacement | Tofu | Gwotofu | Tofu Royal |
|---|---|---|---|
| 1 | Farceur (Prankster) | Isograisse (Thick Fat) | Prestance Royale (Queenly Majesty) |
| 2 | Délestage (Unburden) | Gloutonnerie (Gluttony) | Intimidation (Intimidate) |
| Caché | Pickpocket (Pickpocket) | Bajoues (Cheek Pouch) | Ailes Bourrasque (Gale Wings) |

- Isograisse ramène la faiblesse Glace de Gwotofu (×4 en Sol/Vol) à ×2.
- Prestance Royale (talent de Sucreine) : l'adversaire ne peut pas le viser
  avec une attaque prioritaire.
- Lignée cachée sur le thème des objets : il vole l'objet, puis le mange.
- Si Farceur paraît trop fort en début de partie : Fuite ou Regard Vif.

## Kit final

_À faire._

## Learnsets

_À faire._
