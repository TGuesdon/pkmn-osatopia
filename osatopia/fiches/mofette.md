# Famille Mofette

> Monstres de roche volcanique : la Mofette, émanation de gaz et de fumée,
> devient l'Obsidiantre, un bloc d'obsidienne en fusion. *(Lore de mémoire, à
> vérifier : zone — Frigost ? — et éléments des sorts, a priori Feu et Terre.)*
> Évolutions : Mofette → Obsidiantre (niv. 40).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_SLOW` (évolution tardive au niv. 40, comme Pyronille) ; groupe d'œuf
`EGG_GROUP_MINERAL`, couleurs `BODY_COLOR_GRAY` (Mofette) et
`BODY_COLOR_BLACK` (Obsidiantre).

## Intention

Archétype : **tank offensif spécial**. Obsidiantre encaisse grâce à ses PV et
ses deux défenses, se renforce avec Plénitude, piège l'adversaire dans Vortex
Magma et frappe en spécial. Monstre de fin d'aventure qui évolue tard.

Références : **Volcaropod** (même typage, Corps Ardent), **Heatran** (feu
spécial lent et robuste, Torche, Vortex Magma) et **Carmadura** (profil de
stats le plus proche).

Feu/Roche aux deux stades, inédit chez les monstres custom. Faiblesses : Eau
×4, Sol ×4, Combat. Résistances : Normal, Feu ×4, Vol, Poison, Insecte, Fée.
La DéfSpé de 90 évite le K.O. sur la première attaque Eau spéciale ; Solide Roc
a été écarté comme trop fort.

## Stades

| | Mofette | Obsidiantre |
|---|---|---|
| Types | Feu/Roche | Feu/Roche |
| PV | 70 | 100 |
| Attaque | 40 | 55 |
| Défense | 75 | 100 |
| Atq. Spé | 80 | 115 |
| Déf. Spé | 60 | 90 |
| Vitesse | 45 | 50 |
| **Total** | **370** | **510** |
| Évolution | niv. 40 | – |
| Capture / Exp. | 75 / 95 | 45 / 215 |
| EV | AtqSpé +1 | AtqSpé +2 |

Stats sacrifiées : l'Attaque (attaquant spécial) et la Vitesse (il se fait
toucher en premier, d'où PV et Déf hauts).

Comparaisons (outil `similaires`) :
- Mofette : Chapotus (370), Mélancolux (370), Lainergie (365) ; côté
  Osatopia, Scarafeuille vert (400).
- Obsidiantre : Pharamp (510), Ampibidou (495), Arboliva (510) ; côté
  Osatopia, Ronronchon (480), Psy/Fée et moins robuste physiquement.

## Talents

| Emplacement | Mofette | Obsidiantre |
|---|---|---|
| 1 | Corps Ardent (Flame Body) | Corps Ardent (Flame Body) |
| 2 | Turbine (Steam Engine) | Turbine (Steam Engine) |
| Caché | Torche (Flash Fire) | Torche (Flash Fire) |

- Corps Ardent : punit les attaquants physiques au contact.
- Turbine : Vitesse +6 s'il est touché par une attaque Eau ou Feu ; un pari
  sur sa faiblesse ×4.
- Torche : immunité Feu et renforcement de ses attaques Feu.
- Écartés : Solide Roc (trop fort), Armumagma, Armurouillée.

## Kit final (Obsidiantre, niv. 40–55)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| STAB Feu | Vortex Magma (Magma Storm) | Feu | Spé. | 100 | Piège et use 4–5 tours, appris à l'évolution |
| STAB Roche | Rayon Gemme (Power Gem) | Roche | Spé. | 80 | Fiable |
| Boost | Plénitude (Calm Mind) | Psy | Statut | – | AtqSpé +1, DéfSpé +1 |
| Couverture | Telluriforce (Earth Power) | Sol | Spé. | 90 | Contre Roche, Acier, Feu, Électrik |

Alternatives : Déflagration, Canicule, Incendie (Feu) ; Laser Météore (Roche) ;
Force Cosmique, Stockage, Piège de Roc (boost/utilitaire) ; Sable Ardent,
Éco-Sphère (couverture).

## Learnsets

Les Feu custom (Crachefoux, Kwak Feu) ont déjà Lance-Flammes, Ébullilave,
Éruption, Surchauffe, Caboche-Kaboum et Danse du Feu : on les évite par niveau.
Fil conducteur : gaz et fumée, puis boue et roche, puis magma.

### Mofette

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Flammèche (Ember) | Feu | Spé. | 40 |
| 1 | Brouillard (Smokescreen) | Normal | Statut | – |
| 5 | Purédpois (Smog) | Poison | Spé. | 30 |
| 9 | Armure (Harden) | Normal | Statut | – |
| 13 | Tir de Boue (Mud Shot) | Sol | Spé. | 55 |
| 17 | Danse Flammes (Fire Spin) | Feu | Spé. | 35 |
| 21 | Pouvoir Antique (Ancient Power) | Roche | Spé. | 60 |
| 25 | Rebondifeu (Flame Burst) | Feu | Spé. | 70 |
| 29 | Feu Follet (Will-O-Wisp) | Feu | Statut | – |
| 33 | Sable Ardent (Scorching Sands) | Sol | Spé. | 70 |
| 37 | Rayon Gemme (Power Gem) | Roche | Spé. | 80 |
| 42 | Plénitude (Calm Mind) | Psy | Statut | – |
| 47 | Telluriforce (Earth Power) | Sol | Spé. | 90 |
| 52 | Déflagration (Fire Blast) | Feu | Spé. | 110 |

### Obsidiantre

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Vortex Magma (Magma Storm) | Feu | Spé. | 100 |
| 1–37 | *comme Mofette* | | | |
| 44 | Plénitude (Calm Mind) | Psy | Statut | – |
| 49 | Telluriforce (Earth Power) | Sol | Spé. | 90 |
| 54 | Laser Météore (Meteor Beam) | Roche | Spé. | 120 |
| 60 | Déflagration (Fire Blast) | Feu | Spé. | 110 |

Temporisation : une Mofette qui refuse d'évoluer obtient Plénitude et
Telluriforce un peu plus tôt, mais jamais Vortex Magma ni Laser Météore.

## CT, CS et tuteurs

| Attaque | Source | Mofette | Obsidiantre |
|---|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Vantardise | CT | ✓ | ✓ |
| Ténacité, Blabla Dodo, Ronflement | tuteurs | ✓ | ✓ |
| Zénith, Tempête de Sable, Protection, Mur Lumière | CT | ✓ | ✓ |
| Plénitude (Calm Mind) | CT04 | ✓ | ✓ |
| Lance-Flammes, Déflagration, Surchauffe | CT35 / CT38 / CT50 | ✓ | ✓ |
| Bombe Beurk (Sludge Bomb) | CT36 | ✓ | ✓ |
| Tomberoche, Séisme, Tunnel | CT | ✓ | ✓ |
| Éclate-Roc, Force | CS | ✓ | ✓ |
| Éboulement, Coud'Boue, Roulade, Boul'Armure, Explosion | tuteurs | ✓ | ✓ |
| Lance-Soleil (Solar Beam) | CT22 | – | ✓ |
| Ultralaser (Hyper Beam) | CT15 | – | ✓ |

Exclusions volontaires : Eau, Glace, Électrik (incohérents avec un monstre de
lave), coups de poing et Vol (ni bras ni ailes), Psyko et Ball'Ombre.
Lance-Soleil réservé à Obsidiantre pour ne pas couvrir trop tôt ses faiblesses
Eau et Sol.
