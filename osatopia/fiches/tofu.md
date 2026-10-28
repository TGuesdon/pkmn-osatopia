# Famille Tofu

> Petit oiseau jaune de l'élément Air, très rapide et fragile, croisé dès le
> début de l'aventure (Incarnam, Astrub). Le Tofu ventripotent est sa version
> engraissée ; le Tofu Royal est le boss du donjon des Tofus.
> Évolutions : Tofu → Gwotofu (niv. 16) → Tofu Royal (niv. 32).
> Maletofu (Tofu maléfique) est une espèce à part.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

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

Dans le learnset de Gwotofu :
- Piétisol (Bulldoze, 60) au niv. 20 ;
- Picots (Spikes) au niv. 29 et Amass'Sable (Shore Up) au niv. 31 ;
- **Séisme (Earthquake, 100) au niv. 36** : la récompense de la temporisation.

Sur un Tofu Royal Vol pur, Séisme est une couverture précieuse contre
Électrik, Roche et Acier.

Contraintes techniques :
- `P_PRE_EVO_MOVES` est à `FALSE` (`include/config/summary_screen.h`) :
  Tofu Royal ne peut pas réapprendre les attaques de Gwotofu. ✅
- Séisme et Tunnel ne sont dans les CT d'**aucun** stade, Gwotofu compris :
  sinon on lui apprend la CT puis on le fait évoluer, et la mécanique perd son
  intérêt.

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
| Capture / Exp. | 255 / 56 | 120 / 140 | 45 / 218 |
| EV | Vit +1 | Déf +2 | Att +2, Vit +1 |

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

Tofu Royal vers le niv. 40–50 : physique solide qui encaisse (Intimidation,
Gonflette, Atterrissage), Séisme en bonus pour qui a temporisé.

| Emplacement | Choix | Type · Cat. | Puiss. | Alternatives |
|---|---|---|---|---|
| STAB Vol | **Bec Vrille** (Drill Peck) | Vol · Phys. | 80 | Bec-Canon, Double Volée (prio avec Ailes Bourrasque), Rebond |
| Couverture | **Séisme** (Earthquake) | Sol · Phys. | 100 | Piétisol (sans temporiser), Ailes d'Acier, Plaquage |
| Boost | **Gonflette** (Bulk Up) | Combat · Statut | – | (Danse Lames / Danse Draco écartées : trop fortes) |
| Utilitaire | **Atterrissage** (Roost) | Vol · Statut | – | Sabotage, Râle Mâle, Provoc |

Variante offensive : **Vive-Attaque** (Quick Attack, prio +1) à la place
d'Atterrissage. Elle compense l'absence de boost de Vitesse et fait miroir à
Prestance Royale (il frappe en priorité, on ne peut pas le viser en priorité).
Vitesse Extrême écartée : trop forte, et déjà sur Bitouvol.

Distinct de Bitouvol : ni Rapace, ni Acrobatie, ni Vent Arrière, ni Demi-Tour.

## Capacités custom

Aucune.

## Learnsets

Les trois stades partagent les attaques de Tofu des niv. 1 à 15. Tofu Royal
n'apprend aucune attaque Sol par niveau.

### Tofu

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| 1 | Picpic (Peck) | Vol | Phys. | 35 | STAB faible |
| 1 | Rugissement (Growl) | Normal | Statut | – | Gêne (prio avec Farceur) |
| 5 | Vive-Attaque (Quick Attack) | Normal | Phys. | 40 prio+1 | Frappe le premier |
| 8 | Jet de Sable (Sand Attack) | Sol | Statut | – | Gêne |
| 12 | Implore (Covet) | Normal | Phys. | 60 | Vole l'objet |
| 15 | Provoc (Taunt) | Ténèbres | Statut | – | Nuisible |
| 19 | Cru-Ailes (Wing Attack) | Vol | Phys. | 60 | STAB (si non évolué) |
| 23 | Danse Plumes (Feather Dance) | Vol | Statut | – | Att −2 (si non évolué) |
| 27 | Double Volée (Dual Wingbeat) | Vol | Phys. | 40×2 | (si non évolué) |
| 31 | Encore (Encore) | Normal | Statut | – | (si non évolué) |

### Gwotofu

Niv. 1 à 15 : comme Tofu (Picpic, Rugissement, Vive-Attaque, Jet de Sable,
Implore, Provoc).

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| Évo | Stockage (Stockpile) | Normal | Statut | – | Il se remplit les joues |
| 20 | Piétisol (Bulldoze) | Sol | Phys. | 60 | STAB Sol |
| 23 | Avale (Swallow) | Normal | Statut | – | Soin avec Stockage |
| 26 | Cru-Ailes (Wing Attack) | Vol | Phys. | 60 | STAB Vol |
| 29 | Picots (Spikes) | Sol | Statut | – | Pièges |
| 31 | Amass'Sable (Shore Up) | Sol | Statut | – | Soin, juste avant l'évolution |
| **36** | **Séisme (Earthquake)** | Sol | Phys. | 100 | **Récompense de la temporisation** |
| 41 | Plaquage (Body Slam) | Normal | Phys. | 85 | Pour qui le garde Gwotofu |
| 46 | Mur de Fer (Iron Defense) | Acier | Statut | – | Mur physique |

### Tofu Royal

Niv. 1 à 15 : comme Tofu. Plus Cru-Ailes au niv. 26 (réapprentissage).

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| Évo | Râle Mâle (Noble Roar) | Normal | Statut | – | Rugissement royal |
| 35 | Gonflette (Bulk Up) | Combat | Statut | – | Boost |
| 38 | Bec Vrille (Drill Peck) | Vol | Phys. | 80 | STAB principal |
| 42 | Atterrissage (Roost) | Vol | Statut | – | Soin |
| 46 | Sabotage (Knock Off) | Ténèbres | Phys. | 65 | Lignée objets |
| 51 | Bec-Canon (Beak Blast) | Vol | Phys. | 100 prio−3 | Attaque finale |

## CT, CS et tuteurs

Séisme et Tunnel : **aucun stade**.

| | Tofu | Gwotofu | Tofu Royal |
|---|---|---|---|
| Abri, Repos, Attraction, Reflet, Provoc, Tourmente | ✅ | ✅ | ✅ |
| Aéropique, Façade, Larcin | ✅ | ✅ | ✅ |
| Ailes d'Acier (couvre Roche et Glace) | ✅ | ✅ | ✅ |
| Copie, Vantardise, Clonage, Blabla Dodo (tuteurs) | ✅ | ✅ | ✅ |
| Vol (CS) | ✅ | ❌ cloué au sol | ✅ |
| Gonflette, Damoclès (tuteur) | – | ✅ | ✅ |
| Roulade (tuteur), Tempête de Sable, Force, Éclate-Roc | – | ✅ | – |
| Hurlement, Ultralaser | – | – | ✅ |

Exclus volontairement : attaques spéciales élémentaires, attaques de poing,
Toxik, Danse Pluie, Zénith.
