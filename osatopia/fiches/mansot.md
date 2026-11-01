# Famille Mansot

> Pingouins de l'île de Frigost (Champs de Glace, Banquise). Le Fu Mansot est
> un maître d'arts martiaux qui se bat avec un poisson ; la Mamansot porte son
> petit dans une poche ventrale. *(Lore de mémoire, à vérifier : éléments des
> sorts et zone des quatre monstres.)*
> Évolutions : Timansot → Mansobèse (niv. 16) → Fu Mansot (♂, niv. 36) ou
> Mamansot (♀, niv. 36).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `STANDARD_FRIENDSHIP`,
`GROWTH_MEDIUM_SLOW`. Choisies pour la famille : `PERCENT_FEMALE(50)` pour
Timansot et Mansobèse, `MON_MALE` pour Fu Mansot, `MON_FEMALE` pour Mamansot ;
`.eggCycles = 20`, groupes d'œuf `EGG_GROUP_WATER_1` + `EGG_GROUP_FIELD`
(comme Tiplouf), couleur `BODY_COLOR_BLACK` (à vérifier).

## Intention

Archétypes :
- **Mansobèse** : tank de passage, gros en PV, Isograisse.
- **Fu Mansot** : **attaquant physique équilibré**, plutôt rapide pour doubler
  Branchicrok (le poisson), Gonflette en boost.
- **Mamansot** : **tank offensif spécial** ; Amour Filial (comme
  Méga-Kangourex) fait frapper chaque attaque deux fois (2e coup à 25 %,
  `B_PARENTAL_BOND_DMG` Gen 7+) et double les chances d'effet secondaire.

Références : **Tiplouf / Pingoléon** (pingouin lent et spécial),
**Kaimorse** (Glace/Eau, Isograisse), **Kangourex** (la mère et son petit).

Eau/Glace tout du long, sauf Fu Mansot en **Glace/Combat** (kung-fu) pour
éviter un quatrième Eau/Combat (Grenn, Raphaela, Tortue Bleue). Évolution
selon le sexe comme Cheniti → Cheniselle / Papilord.

## Stades

| | Timansot | Mansobèse | Fu Mansot ♂ | Mamansot ♀ |
|---|---|---|---|---|
| Types | Eau/Glace | Eau/Glace | Glace/Combat | Eau/Glace |
| PV | 55 | 95 | 85 | 105 |
| Attaque | 48 | 65 | 105 | 55 |
| Défense | 47 | 70 | 80 | 90 |
| Atq. Spé | 50 | 65 | 60 | 95 |
| Déf. Spé | 50 | 65 | 80 | 85 |
| Vitesse | 40 | 40 | 95 | 55 |
| **Total** | **290** | **400** | **505** | **485** |
| Évolution | niv. 16 | niv. 36 selon le sexe | – | – |
| Capture / Exp. | 45 / 63 | 45 / 147 | 45 / 239 | 45 / 239 |
| EV | PV +1 | PV +2 | Att +2, Vit +1 | AtqSpé +2, Déf +1 |
| Sexe | 50 % ♀ | 50 % ♀ | 100 % ♂ | 100 % ♀ |

Stats sacrifiées :
- Timansot et Mansobèse : la Vitesse (40), comme Tiplouf ; Mansobèse mise
  tout sur les PV.
- Fu Mansot : l'AtqSpé ; Vit 95 pour agir en premier et doubler Branchicrok ;
  défenses 80/80 car Glace/Combat a 5 faiblesses (Feu, Combat, Psy, Fée,
  Acier).
- Mamansot : l'Att et la Vit ; AtqSpé 95 qui vaut ~119 avec Amour Filial ;
  total plus bas que Fu Mansot pour compenser le talent.

Comparaisons (outil `similaires`) : Stalgamin, Tiplouf (Timansot) ; Phogleur,
Insolourdo (Mansobèse) ; Manternel, Insécateur (Fu Mansot) ; Moyade,
Ampibidou (Mamansot). Côté Osatopia : Kwak Terre et Lapigro (Fu Mansot),
Ronronchon (Mamansot, plus spéciale et plus fragile).

## Talents

| Emplacement | Timansot / Mansobèse | Fu Mansot | Mamansot |
|---|---|---|---|
| 1 | Isograisse (Thick Fat) | Attention (Inner Focus) | Amour Filial (Parental Bond) |
| 2 | Corps Gel (Ice Body) | Querelleur (Scrappy) | Amour Filial (Parental Bond) |
| Caché | Glissade (Swift Swim) | Impudence (Moxie) | Amour Filial (Parental Bond) |

- Isograisse : le gras de Mansobèse, divise par deux les dégâts Feu (sa
  faiblesse) et Glace.
- Attention : pas de peur, immunité à Intimidation (mental de moine).
- Querelleur : ses attaques Combat touchent les Spectres, immunité à
  Intimidation.
- Amour Filial dans les trois emplacements : le talent garde son emplacement
  à l'évolution, toutes les Mamansot l'ont donc.

## Kit final (niv. 40–50)

### Fu Mansot

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| Le poisson | Branchicrok (Fishious Rend) | Eau | Phys. | 85 | ×2 s'il agit en premier ; couvre Feu, Roche, Acier |
| STAB Combat | Talon-Marteau (Axe Kick) | Combat | Phys. | 120 | 90 %, confusion, se blesse s'il rate |
| STAB Glace | Chute Glace (Icicle Crash) | Glace | Phys. | 85 | peur 30 % |
| Boost | Gonflette (Bulk Up) | Combat | Statut | – | Att +1, Déf +1 |

Alternatives : Close Combat, Vampi-Poing, Prio-Parade, Triple Axel,
Cryo-Pirouette, Eau Revoir, Danse Lames. Branchicrok est aussi chez Raul
Mops (famille Dagon), au niveau 40.

### Mamansot

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Eau | Ébullition (Scald) | Eau | Spé. | 80 | brûlure 30 % ×2 avec Amour Filial |
| STAB Glace | Laser Glace (Ice Beam) | Glace | Spé. | 90 | gel ×2 |
| Soin | Fontaine de Vie (Life Dew) | Eau | Statut | – | soigne 25 % |
| Couverture | Mégaphone (Hyper Voice) | Normal | Spé. | 90 | le petit crie |

Alternatives : Surf, Hydrocanon, Vibraqua, Saumure, Lyophilisation, Vent
Glace, Plénitude, Vœu, Pouvoir Lunaire, Écho.

## Capacités custom

Aucune : Branchicrok porte le poisson du Fu Mansot.

## Learnsets

### Timansot

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Écras'Face (Pound) | Normal | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Pistolet à O (Water Gun) | Eau | Spé. | 40 |
| 7 | Poudreuse (Powder Snow) | Glace | Spé. | 40 |
| 10 | Boul'Armure (Defense Curl) | Normal | Statut | – |
| 13 | Roulade (Rollout) | Roche | Phys. | 30 |
| 17 | Vibraqua (Water Pulse) | Eau | Spé. | 60 |
| 19 | Vent Glace (Icy Wind) | Glace | Spé. | 55 |
| 23 | Saumure (Brine) | Eau | Spé. | 65 |
| 27 | Bâillement (Yawn) | Normal | Statut | – |
| 31 | Plaquage (Body Slam) | Normal | Phys. | 85 |
| 34 | Repos (Rest) | Psy | Statut | – |

### Mansobèse

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Vibraqua (Water Pulse) | Eau | Spé. | 60 |
| 1–13 | *attaques de Timansot, mêmes niveaux* | | | |
| 19–34 | *attaques de Timansot, mêmes niveaux* | | | |
| 38 | Ocroupi (Muddy Water) | Eau | Spé. | 90 |
| 44 | Hydrocanon (Hydro Pump) | Eau | Spé. | 110 |

### Fu Mansot

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Branchicrok (Fishious Rend) | Eau | Phys. | 85 |
| 1–13, 19–34 | *attaques de Timansot, mêmes niveaux (sans Vibraqua)* | | | |
| 38 | Balayette (Low Sweep) | Combat | Phys. | 65 |
| 41 | Gonflette (Bulk Up) | Combat | Statut | – |
| 44 | Triple Axel | Glace | Phys. | 20×3 |
| 48 | Chute Glace (Icicle Crash) | Glace | Phys. | 85 |
| 52 | Talon-Marteau (Axe Kick) | Combat | Phys. | 120 |

### Mamansot

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Fontaine de Vie (Life Dew) | Eau | Statut | – |
| 1–13, 19–34 | *attaques de Timansot, mêmes niveaux (sans Vibraqua)* | | | |
| 38 | Ébullition (Scald) | Eau | Spé. | 80 |
| 41 | Mégaphone (Hyper Voice) | Normal | Spé. | 90 |
| 44 | Laser Glace (Ice Beam) | Glace | Spé. | 90 |
| 48 | Plénitude (Calm Mind) | Psy | Statut | – |
| 52 | Hydrocanon (Hydro Pump) | Eau | Spé. | 110 |

17 attaques par stade final. Rien à 90+ avant le niveau 31 (Plaquage, 85).
Tronc Boul'Armure → Roulade (le pingouin glisse sur le ventre) → Bâillement →
Repos inédit parmi les monstres custom. Temporisation : Ocroupi et Hydrocanon
(44) sont exclusifs à Mansobèse, qui a donc un intérêt à ne pas évoluer ;
Mamansot n'a Hydrocanon qu'au 52.

## CT, CS et tuteurs

| | Timansot | Mansobèse | Fu Mansot | Mamansot |
|---|---|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet, Vantardise (CT) | ✅ | ✅ | ✅ | ✅ |
| Danse Pluie, Grêle, Vibraqua, Laser Glace, Blizzard (CT) | ✅ | ✅ | ✅ | ✅ |
| Surf, Cascade, Plongée, Force, Éclate-Roc (CS) | ✅ | ✅ | ✅ | ✅ |
| Blabla Dodo, Ronflement, Ténacité, Vent Glace (tuteurs) | ✅ | ✅ | ✅ | ✅ |
| Plaquage, Boul'Armure, Roulade (tuteurs) | ✅ | ✅ | ✅ | ✅ |
| Ultralaser (CT), Damoclès (tuteur) | – | ✅ | – | ✅ |
| Gonflette, Casse-Brique, Mitra-Poing, Provoc, Tomberoche (CT) | – | – | ✅ | – |
| Poing Glace, Ultimawashi, Riposte, Éboulement, Frappe Atlas (tuteurs) | – | – | ✅ | – |
| Plénitude, Mur Lumière, Protection, Rune Protect (CT) | – | – | – | ✅ |

Exclus volontairement :
- Frappe Atlas pour Mamansot : avec Amour Filial, deux fois des dégâts égaux
  au niveau ;
- Danse Lames (tuteur) pour Fu Mansot : son boost est Gonflette ;
- E-Coque pour Mamansot : elle a déjà Fontaine de Vie ;
- Séisme, Tunnel, Aéropique, Queue de Fer : peu cohérents pour un pingouin ;
- Explosion, Dévorêve, Cage Éclair, Métronome ;
- inutilisables : Saisie, Flash, Retour, Frustration, Puissance Cachée.
