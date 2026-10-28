# Familles Bwak

> Le Bwak est un petit oiseau né d'un œuf, connu surtout comme familier ; le
> Kwak (Kwakere) est sa forme adulte sauvage, déclinée en quatre éléments, qui
> vit dans les pics autour du Kwakwa (lore à vérifier).
> Évolutions : Bwak X → Kwak X par pierre élémentaire (Pierre Glace, Pierre
> Vent, Pierre Feu, Pierre Terre).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Quatre familles de 2 stades qui **se ressemblent** : même total de stats,
même squelette de learnset, même attaque d'évolution (Vent Arrière). Seuls les
types, la répartition des stats et quelques attaques changent.

| Famille | Bwak | Kwak | Nom affiché | Pierre |
|---|---|---|---|---|
| Glace | `SPECIES_BWAK_GLACE` | `SPECIES_KWAKERE_GLACE` | Bwak Glace → Kwak Glace | `ITEM_ICE_STONE` |
| Vent | `SPECIES_BWAK_VENT` | `SPECIES_KWAKERE_VENT` | Bwak Vent → Kwak Vent | `ITEM_WIND_STONE` |
| Feu | `SPECIES_BWAK_FEU` | `SPECIES_KWAKERE_FEU` | Bwak Feu → Kwak Feu | `ITEM_FIRE_STONE` |
| Terre | `SPECIES_BWAK_TERRE` | `SPECIES_KWAKERE_TERRE` | Bwak Terre → Kwak Terre | `ITEM_EARTH_STONE` |

Pierre Vent et Pierre Terre : ajoutées par le commit `869e6c9818` (icônes
provisoires). Aucune des quatre pierres n'est encore placée sur la carte pour
les Bwak (la Pierre Glace n'existe nulle part dans Émeraude).

## Intention

Archétype commun : **attaquant rapide polyvalent**, avec une nuance par famille.

| Famille | Nuance |
|---|---|
| Feu | Démolisseur spécial |
| Glace | Perturbateur |
| Terre | Tank offensif physique |
| Vent | Nettoyeur rapide, autour de **Peau Céleste** (Normal → Vol, +20 %) |

Références : Flamajou → Flamoutan (familles en miroir, évolution par pierre),
Couaneton → Lakmécygne (oiseau élément/Vol à 2 stades), Étourvol (oiseau
physique à attaques Normal). Kwak Vent est proche de Bitouvol : assumé, on ne
les croise pas au même endroit et Bitouvol sera retravaillé.

## Stades

| | Type | PV | Att | Déf | AtqSpé | DéfSpé | Vit | Total |
|---|---|---|---|---|---|---|---|---|
| Bwak Feu | Feu | 50 | 50 | 45 | 63 | 45 | 57 | 310 |
| Bwak Glace | Glace | 52 | 50 | 45 | 58 | 52 | 53 | 310 |
| Bwak Terre | Sol | 55 | 60 | 55 | 45 | 45 | 50 | 310 |
| Bwak Vent | Vol | 47 | 62 | 42 | 45 | 42 | 72 | 310 |
| Kwak Feu | Feu/Vol | 77 | 82 | 66 | 108 | 70 | 97 | 500 |
| Kwak Glace | Glace/Vol | 82 | 77 | 70 | 98 | 88 | 85 | 500 |
| Kwak Terre | Sol/Vol | 88 | 104 | 88 | 65 | 70 | 85 | 500 |
| Kwak Vent | Vol | 77 | 108 | 66 | 62 | 70 | 117 | 500 |

Talents (identiques pour le Bwak et le Kwak d'une famille) :

| | Talent 1 | Talent 2 | Caché |
|---|---|---|---|
| Feu | Brasier (Blaze) | Cœur de Coq (Big Pecks) | Force Soleil (Solar Power) |
| Glace | Corps Gel (Ice Body) | Cœur de Coq | Peau Gelée (Refrigerate) |
| Terre | Force Sable (Sand Force) | Cœur de Coq | Tête de Roc (Rock Head) |
| Vent | Peau Céleste (Aerilate) | Cœur de Coq | Téméraire (Reckless) |

Capture, expérience et EV :

| | Capture | Exp. | EV |
|---|---|---|---|
| Bwak Feu | 190 | 63 | AtqSpé 1 |
| Bwak Glace | 190 | 63 | DéfSpé 1 |
| Bwak Terre | 190 | 63 | Déf 1 |
| Bwak Vent | 190 | 63 | Vit 1 |
| Kwak Feu | 75 | 175 | AtqSpé 2 |
| Kwak Glace | 75 | 175 | AtqSpé 1, DéfSpé 1 |
| Kwak Terre | 75 | 175 | Att 1, Déf 1 |
| Kwak Vent | 75 | 175 | Att 1, Vit 1 |

Autres champs (repris de la famille Tofu) : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`,
`EGG_GROUP_FLYING`. Couleur d'après les sprites : Glace bleu, Vent blanc,
Feu rouge (Bwak) / marron (Kwak), Terre vert.

## Kit final

Emplacements : ① STAB élément · ② STAB Vol · ③ nuance · ④ Vent Arrière (commun).

| | ① | ② | ③ | ④ |
|---|---|---|---|---|
| Kwak Feu | Lance-Flammes (90) | Lame d'Air (75) | Machination, Danse du Feu, Surchauffe, Feu Follet | Vent Arrière |
| Kwak Glace | Laser Glace (90) | Typhon Hivernal (100) | Voile Aurore, Vent Glace, Chute de Neige, Buée Noire | Vent Arrière |
| Kwak Terre | Séisme (100) | Bec Vrille (80) | Piège de Roc, Éboulement | Vent Arrière |
| Kwak Vent | Damoclès (120 → Vol) | Vive-Attaque (40 → Vol, prio +1) | Danse Lames, Demi-Tour, Rapace | Vent Arrière |

Pas de Vitesse Extrême pour Kwak Vent (signature de Bitouvol).

## Capacités custom

Aucune.

## Learnsets

Le Kwak reprend le learnset du Bwak aux mêmes niveaux, plus **Vent Arrière à
l'évolution** et une **attaque finale au niv. 48** qui lui est réservée.
L'évolution par pierre laisse le joueur évoluer quand il veut sans perdre le
tronc commun. Bwak Vent a déjà Peau Céleste : ses attaques Normal sont des
STAB Vol.

### Squelette commun (Bwak et Kwak)

| Niv. | Feu | Glace | Terre | Vent |
|---|---|---|---|---|
| 1 | Picpic (Peck) · Vol · Phys. · 35 | ← | ← | ← |
| 1 | Rugissement (Growl) · Normal · Statut | ← | ← | ← |
| 4 | Flammèche (Ember) · Feu · Spé. · 40 | Poudreuse (Powder Snow) · Glace · Spé. · 40 | Tourbi-Sable (Sand Tomb) · Sol · Phys. · 35 | Charge (Tackle) · Normal · Phys. · 40 |
| 8 | Vive-Attaque (Quick Attack) · Normal · Phys. · 40 | ← | ← | ← |
| 12 | Danse Flammes (Fire Spin) · Feu · Spé. · 35 | Brume (Mist) · Glace · Statut | Jet de Sable (Sand Attack) · Sol · Statut | Groz'Yeux (Leer) · Normal · Statut |
| 16 | Tranch'Air (Air Cutter) · Vol · Spé. · 60 | Tranch'Air (Air Cutter) · Vol · Spé. · 60 | Cru-Ailes (Wing Attack) · Vol · Phys. · 60 | Cru-Ailes (Wing Attack) · Vol · Phys. · 60 |
| 20 | Calcination (Incinerate) · Feu · Spé. · 60 | Vent Glace (Icy Wind) · Glace · Spé. · 55 | Piétisol (Bulldoze) · Sol · Phys. · 60 | Double Volée (Dual Wingbeat) · Vol · Phys. · 40 ×2 |
| 24 | Feu Follet (Will-O-Wisp) · Feu · Statut | Buée Noire (Haze) · Glace · Statut | Tomberoche (Rock Tomb) · Roche · Phys. · 60 | Danse Plumes (Feather Dance) · Vol · Statut |
| 28 | Ébullilave (Lava Plume) · Feu · Spé. · 80 | Lyophilisation (Freeze-Dry) · Glace · Spé. · 70 | Trépignement (Stomping Tantrum) · Sol · Phys. · 75 | Coup d'Boule (Headbutt) · Normal · Phys. · 70 |
| 32 | Lame d'Air (Air Slash) · Vol · Spé. · 75 | Lame d'Air (Air Slash) · Vol · Spé. · 75 | Bec Vrille (Drill Peck) · Vol · Phys. · 80 | Plaquage (Body Slam) · Normal · Phys. · 85 |
| 36 | Machination (Nasty Plot) · Ténèbres · Statut | Chute de Neige (Snowscape) · Glace · Statut | Éboulement (Rock Slide) · Roche · Phys. · 75 | Danse Lames (Swords Dance) · Normal · Statut |
| 40 | Lance-Flammes (Flamethrower) · Feu · Spé. · 90 | Laser Glace (Ice Beam) · Glace · Spé. · 90 | Séisme (Earthquake) · Sol · Phys. · 100 | Damoclès (Double-Edge) · Normal · Phys. · 120 |
| 44 | Danse du Feu (Fiery Dance) · Feu · Spé. · 80 | Voile Aurore (Aurora Veil) · Glace · Statut | Piège de Roc (Stealth Rock) · Roche · Statut | Demi-Tour (U-turn) · Insecte · Phys. · 70 |

### Exclusivités du Kwak

| Niv. | Feu | Glace | Terre | Vent |
|---|---|---|---|---|
| Évo | Vent Arrière (Tailwind) · Vol · Statut | ← | ← | ← |
| 48 | Surchauffe (Overheat) · Feu · Spé. · 130 | Typhon Hivernal (Bleakwind Storm) · Vol · Spé. · 100 | Rapace (Brave Bird) · Vol · Phys. · 120 | Rapace (Brave Bird) · Vol · Phys. · 120 |

Bwak : 13 attaques ; Kwak : 15 + Évo. Aucune attaque à 90+ avant le niv. 40.

## CT, CS et tuteurs

| | Bwak (×4) | Kwak Feu | Kwak Glace | Kwak Terre | Kwak Vent |
|---|---|---|---|---|---|
| Abri, Repos, Attraction, Reflet, Façade, Aéropique, Larcin, Ailes d'Acier | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ronflement, Blabla Dodo, Vantardise, Ténacité, Météores (tuteurs) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Vol (CS) | ❌ | ✅ | ✅ | ✅ | ✅ |
| Ultralaser | – | ✅ | ✅ | ✅ | ✅ |
| Zénith, Lance-Flammes, Déflagration | Feu | ✅ | | | |
| Surchauffe | ❌ | ✅ | | | |
| Grêle, Laser Glace, Vent Glace (tuteur) | Glace | | ✅ | | |
| Blizzard | ❌ | | ✅ | | |
| Mur Lumière, Protection, Rune Protect, Provoc | Glace | | ✅ | | |
| Tempête de Sable, Séisme, Tunnel, Tomberoche, Coud'Boue (tuteur), Éboulement (tuteur) | Terre | | | ✅ | |
| Force, Éclate-Roc, Gonflette | Terre | | | ✅ | |
| Plaquage (tuteur), Danse Lames (tuteur), Hurlement | Vent | | | | ✅ |
| Damoclès (tuteur d'Atalanopolis) | Vent, Terre | | | ✅ | ✅ |

Exclus volontairement :
- Surchauffe et Blizzard pour les Bwak (attaques finales des Kwak), Vol (CS)
  pour les Bwak (une raison de plus d'utiliser la pierre) ;
- coups de poing, Queue de Fer, Casse-Brique (ce sont des oiseaux) ;
- Toxik, Danse Pluie, Ball'Ombre, Psyko (hors thème).

Le tuteur Damoclès arrive tard (Atalanopolis), il ne casse pas la progression
de Kwak Vent.
