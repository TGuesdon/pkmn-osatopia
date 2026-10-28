# Famille Tigrimas

> Chats fantômes joyeux d'Incarnam qui tiennent du feu. Tigrimas est rare en
> début d'aventure, Ronronchon est sa forme adulte, plus grosse et plus
> paresseuse.
> Évolutions : Tigrimas → Ronronchon (niv. 30).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

## Intention

Archétype : **Distorsion** (principal) + **tank offensif** (secondaire), en
spécial.

Références :
- **Symbios** (Psy, 110 / 65 / 75 / 125 / 85 / 30) : le modèle. Beaucoup de
  PV, gros AtqSpé, lent.
- **Sorcilence** (Psy/Fée, 510) : même typage, lanceur de Distorsion.
- **Tarsal** pour la rencontre : un monstre peu commun de début de jeu qu'on est
  content de trouver.

Pourquoi : Ronronchon encaisse le tour où il pose Distorsion grâce à ses PV,
puis frappe en premier. Sa Vitesse (45) est moins basse que celle de Symbios
(30), pour que l'aventure ne soit pas frustrante hors Distorsion. Le talent
caché Analyste récompense justement le jeu hors Distorsion. Le feu du lore
donne la couverture Feu et le combo **Feu Follet + Cortège Funèbre**.

Distinct des monstres custom : Bloqueuse (Plante/Psy, 486) est un mur spécial
rapide (Vit 70, AtqSpé 83), Ronronchon est offensif et lent. Aucun monstre
custom n'est Fée. Folle est proche de Tigrimas au premier stade, mais Tigrimas
a un total plus bas (295 contre 345) et un profil plus offensif.

## Mécanique : Distorsion après l'évolution

- Tigrimas est **Fée** pur. Le type **Psy** n'arrive qu'avec Ronronchon, et
  avec lui Extrasenseur (Évo) puis **Distorsion au niv. 39**, entre Alizée et
  Lévy & Tatia.
- Distorsion n'existe pas en CT : le learnset est la seule source.
- Toutes les CT Psy sont réservées à Ronronchon.
- Récompense inverse : un Tigrimas dont on bloque l'évolution apprend
  **Pouvoir Lunaire au niv. 40**, contre 47 pour Ronronchon. `P_PRE_EVO_MOVES`
  est à `FALSE` : Ronronchon ne la réapprend pas plus tôt.

## Stades

| | Tigrimas | Ronronchon |
|---|---|---|
| Types | Fée | Psy / Fée |
| PV | 65 | 110 |
| Attaque | 30 | 50 |
| Défense | 40 | 75 |
| Atq. Spé | 70 | 110 |
| Déf. Spé | 50 | 90 |
| Vitesse | 40 | 45 |
| Total | 295 | 480 |
| Talents | Corps Ardent / Garde Magik / caché : Analyste | idem |
| Capture / Exp. | 120 / 70 | 45 / 165 |
| EV | 1 AtqSpé | 1 PV + 1 AtqSpé |

Stats sacrifiées : l'Attaque (profil spécial) et la Défense, inférieure à la
DéfSpé. Corps Ardent et Feu Follet compensent face aux attaquants physiques.

Autres champs : `PERCENT_FEMALE(50)`, `.eggCycles = 15`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`,
`MON_EGG_GROUPS(EGG_GROUP_FIELD, EGG_GROUP_FAIRY)`, `.bodyColor` à choisir
selon le sprite (`BODY_COLOR_PURPLE` par défaut).

**Rencontre** (hors fiche, pour les tables d'apparition) : Tigrimas est rare,
~5 % à un seul endroit d'Incarnam, comme Tarsal sur la Route 102.

## Talents

| Talent | Effet | Pourquoi |
|---|---|---|
| Corps Ardent (Flame Body) | Peut brûler l'attaquant au contact | Chat fantôme qui tient du feu. Protège sa Déf moyenne. |
| Garde Magik (Magic Guard) | Seules les attaques le blessent | Talent de Symbios. Utile face à sa faiblesse Poison. |
| Analyste (Analytic) — caché | +30 % de puissance s'il agit en dernier | Récompense le jeu hors Distorsion. |

## Kit final

Faiblesses Psy/Fée : Poison, Spectre, Acier. Résistance x4 au Combat,
immunité au Dragon.

| Emplacement | Attaque | Type | Cat. | Puiss. | Alternatives |
|---|---|---|---|---|---|
| Mise en place | **Distorsion** (Trick Room) | Psy | Statut | – | Plénitude, Feu Follet |
| STAB Psy | **Psyko** (Psychic) | Psy | Spéciale | 90 | Choc Psy, Extrasenseur, Prescience |
| STAB Fée | **Pouvoir Lunaire** (Moonblast) | Fée | Spéciale | 95 | Éclat Magique, Vampibaiser |
| Couverture Feu (contre l'Acier) | **Feu Ensorcelé** (Mystical Fire) | Feu | Spéciale | 75 | Lance-Flammes (CT), Cortège Funèbre |

Variante tank : Plénitude · Choc Psy · Vampibaiser · Lance-Flammes ou Feu
Follet. Soin disponible par niveau : Rayon Lune (niv. 25).

## Capacités custom

Aucune.

## Learnsets

### Socle commun (mêmes niveaux pour les deux stades)

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Vent Féérique (Fairy Wind) | Fée | Spéciale | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Flammèche (Ember) | Feu | Spéciale | 40 |
| 7 | Léchouille (Lick) | Spectre | Physique | 30 |
| 10 | Doux Baiser (Sweet Kiss) | Fée | Statut | – |
| 13 | Voix Enjôleuse (Disarming Voice) | Fée | Spéciale | 40 |
| 16 | Feu Follet (Will-O-Wisp) | Feu | Statut | – |
| 19 | Vampibaiser (Draining Kiss) | Fée | Spéciale | 50 |
| 22 | Cortège Funèbre (Infernal Parade) | Spectre | Spéciale | 60 |
| 25 | Rayon Lune (Moonlight) | Fée | Statut | – |
| 28 | Éclat Magique (Dazzling Gleam) | Fée | Spéciale | 80 |

### Tigrimas : exclusives (14 attaques au total)

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 32 | Feu Ensorcelé (Mystical Fire) | Feu | Spéciale | 75 |
| 36 | Charme (Charm) | Fée | Statut | – |
| 40 | Pouvoir Lunaire (Moonblast) | Fée | Spéciale | 95 |

### Ronronchon : exclusives (18 attaques au total)

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Extrasenseur (Extrasensory) | Psy | Spéciale | 80 |
| 33 | Feu Ensorcelé (Mystical Fire) | Feu | Spéciale | 75 |
| 36 | Bâillement (Yawn) | Normal | Statut | – |
| 39 | Distorsion (Trick Room) | Psy | Statut | – |
| 43 | Psyko (Psychic) | Psy | Spéciale | 90 |
| 47 | Pouvoir Lunaire (Moonblast) | Fée | Spéciale | 95 |
| 52 | Prescience (Future Sight) | Psy | Spéciale | 120 |

## CT, CS et tuteurs

| Attaque | Source | Tigrimas | Ronronchon |
|---|---|:-:|:-:|
| Toxik (Toxic) | CT06 | ✓ | ✓ |
| Zénith (Sunny Day) | CT11 | ✓ | ✓ |
| Abri (Protect) | CT17 | ✓ | ✓ |
| Ball'Ombre (Shadow Ball) | CT30 | ✓ | ✓ |
| Reflet (Double Team) | CT32 | ✓ | ✓ |
| Lance-Flammes (Flamethrower) | CT35 | ✓ | ✓ |
| Repos (Rest) | CT44 | ✓ | ✓ |
| Attraction (Attract) | CT45 | ✓ | ✓ |
| Larcin (Thief) | CT46 | ✓ | ✓ |
| Coupe (Cut) | CS01 | ✓ | ✓ |
| Métronome (Metronome) | Tuteur | ✓ | ✓ |
| Météores (Swift) | Tuteur | ✓ | ✓ |
| Ténacité (Endure) | Tuteur | ✓ | ✓ |
| Ronflement (Snore) | Tuteur | ✓ | ✓ |
| Blabla Dodo (Sleep Talk) | Tuteur | ✓ | ✓ |
| Cage Éclair (Thunder Wave) | Tuteur | ✓ | ✓ |
| Vantardise (Swagger) | Tuteur | ✓ | ✓ |
| Plénitude (Calm Mind) | CT04 | | ✓ |
| Ultralaser (Hyper Beam) | CT15 | | ✓ |
| Mur Lumière (Light Screen) | CT16 | | ✓ |
| Psyko (Psychic) | CT29 | | ✓ |
| Protection (Reflect) | CT33 | | ✓ |
| Déflagration (Fire Blast) | CT38 | | ✓ |
| Échange (Skill Swap) | CT48 | | ✓ |
| Surchauffe (Overheat) | CT50 | | ✓ |
| Dévorêve (Dream Eater) | Tuteur | | ✓ |
| Boost (Psych Up) | Tuteur | | ✓ |

Exclusions volontaires :
- coups de poing et attaques physiques lourdes (Séisme, Façade, Plaquage) :
  monstre spécial, et c'est un chat ;
- Laser Glace, Tonnerre, Bomb-Beurk : couvertures hors thème ;
- Provoc : n'irait pas avec un poseur de Distorsion ;
- CT Psy sur Tigrimas : le type Psy doit arriver avec l'évolution.

## Annexe — bloc C (à copier à la main)

```c
// species_info.h — SPECIES_TIGRIMAS
       .baseHP        = 65,
       .baseAttack    = 30,
       .baseDefense   = 40,
       .baseSpeed     = 40,
       .baseSpAttack  = 70,
       .baseSpDefense = 50,
       .types = MON_TYPES(TYPE_FAIRY),
       .catchRate = 120,
       .expYield = 70,
       .evYield_SpAttack  = 1,
       .genderRatio = PERCENT_FEMALE(50),
       .eggCycles = 15,
       .friendship = STANDARD_FRIENDSHIP,
       .growthRate = GROWTH_MEDIUM_SLOW,
       .eggGroups = MON_EGG_GROUPS(EGG_GROUP_FIELD, EGG_GROUP_FAIRY),
       .abilities = { ABILITY_FLAME_BODY, ABILITY_MAGIC_GUARD, ABILITY_ANALYTIC },
       .bodyColor = BODY_COLOR_PURPLE,
       // …
       .levelUpLearnset = sTigrimasLevelUpLearnset,
       .teachableLearnset = sTigrimasTeachableLearnset,
       .evolutions = EVOLUTION({EVO_LEVEL, 30, SPECIES_RONRONCHON}),

// species_info.h — SPECIES_RONRONCHON
       .baseHP        = 110,
       .baseAttack    = 50,
       .baseDefense   = 75,
       .baseSpeed     = 45,
       .baseSpAttack  = 110,
       .baseSpDefense = 90,
       .types = MON_TYPES(TYPE_PSYCHIC, TYPE_FAIRY),
       .catchRate = 45,
       .expYield = 165,
       .evYield_HP        = 1,
       .evYield_SpAttack  = 1,
       .genderRatio = PERCENT_FEMALE(50),
       .eggCycles = 15,
       .friendship = STANDARD_FRIENDSHIP,
       .growthRate = GROWTH_MEDIUM_SLOW,
       .eggGroups = MON_EGG_GROUPS(EGG_GROUP_FIELD, EGG_GROUP_FAIRY),
       .abilities = { ABILITY_FLAME_BODY, ABILITY_MAGIC_GUARD, ABILITY_ANALYTIC },
       .bodyColor = BODY_COLOR_PURPLE,
       // …
       .levelUpLearnset = sRonronchonLevelUpLearnset,
       .teachableLearnset = sRonronchonTeachableLearnset,

// level_up_learnsets/gen_9.h
static const struct LevelUpMove sTigrimasLevelUpLearnset[] = {
    LEVEL_UP_MOVE( 1, MOVE_FAIRY_WIND),
    LEVEL_UP_MOVE( 1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE( 4, MOVE_EMBER),
    LEVEL_UP_MOVE( 7, MOVE_LICK),
    LEVEL_UP_MOVE(10, MOVE_SWEET_KISS),
    LEVEL_UP_MOVE(13, MOVE_DISARMING_VOICE),
    LEVEL_UP_MOVE(16, MOVE_WILL_O_WISP),
    LEVEL_UP_MOVE(19, MOVE_DRAINING_KISS),
    LEVEL_UP_MOVE(22, MOVE_INFERNAL_PARADE),
    LEVEL_UP_MOVE(25, MOVE_MOONLIGHT),
    LEVEL_UP_MOVE(28, MOVE_DAZZLING_GLEAM),
    LEVEL_UP_MOVE(32, MOVE_MYSTICAL_FIRE),
    LEVEL_UP_MOVE(36, MOVE_CHARM),
    LEVEL_UP_MOVE(40, MOVE_MOONBLAST),
    LEVEL_UP_END
};

static const struct LevelUpMove sRonronchonLevelUpLearnset[] = {
    LEVEL_UP_MOVE( 0, MOVE_EXTRASENSORY),
    LEVEL_UP_MOVE( 1, MOVE_FAIRY_WIND),
    LEVEL_UP_MOVE( 1, MOVE_TAIL_WHIP),
    LEVEL_UP_MOVE( 4, MOVE_EMBER),
    LEVEL_UP_MOVE( 7, MOVE_LICK),
    LEVEL_UP_MOVE(10, MOVE_SWEET_KISS),
    LEVEL_UP_MOVE(13, MOVE_DISARMING_VOICE),
    LEVEL_UP_MOVE(16, MOVE_WILL_O_WISP),
    LEVEL_UP_MOVE(19, MOVE_DRAINING_KISS),
    LEVEL_UP_MOVE(22, MOVE_INFERNAL_PARADE),
    LEVEL_UP_MOVE(25, MOVE_MOONLIGHT),
    LEVEL_UP_MOVE(28, MOVE_DAZZLING_GLEAM),
    LEVEL_UP_MOVE(33, MOVE_MYSTICAL_FIRE),
    LEVEL_UP_MOVE(36, MOVE_YAWN),
    LEVEL_UP_MOVE(39, MOVE_TRICK_ROOM),
    LEVEL_UP_MOVE(43, MOVE_PSYCHIC),
    LEVEL_UP_MOVE(47, MOVE_MOONBLAST),
    LEVEL_UP_MOVE(52, MOVE_FUTURE_SIGHT),
    LEVEL_UP_END
};

// teachable_learnsets.h
static const u16 sTigrimasTeachableLearnset[] = {
    MOVE_ATTRACT,
    MOVE_CUT,
    MOVE_DOUBLE_TEAM,
    MOVE_ENDURE,
    MOVE_FLAMETHROWER,
    MOVE_METRONOME,
    MOVE_PROTECT,
    MOVE_REST,
    MOVE_SHADOW_BALL,
    MOVE_SLEEP_TALK,
    MOVE_SNORE,
    MOVE_SUNNY_DAY,
    MOVE_SWAGGER,
    MOVE_SWIFT,
    MOVE_THIEF,
    MOVE_THUNDER_WAVE,
    MOVE_TOXIC,
    MOVE_UNAVAILABLE,
};

static const u16 sRonronchonTeachableLearnset[] = {
    MOVE_ATTRACT,
    MOVE_CALM_MIND,
    MOVE_CUT,
    MOVE_DOUBLE_TEAM,
    MOVE_DREAM_EATER,
    MOVE_ENDURE,
    MOVE_FIRE_BLAST,
    MOVE_FLAMETHROWER,
    MOVE_HYPER_BEAM,
    MOVE_LIGHT_SCREEN,
    MOVE_METRONOME,
    MOVE_OVERHEAT,
    MOVE_PROTECT,
    MOVE_PSYCH_UP,
    MOVE_PSYCHIC,
    MOVE_REFLECT,
    MOVE_REST,
    MOVE_SHADOW_BALL,
    MOVE_SKILL_SWAP,
    MOVE_SLEEP_TALK,
    MOVE_SNORE,
    MOVE_SUNNY_DAY,
    MOVE_SWAGGER,
    MOVE_SWIFT,
    MOVE_THIEF,
    MOVE_THUNDER_WAVE,
    MOVE_TOXIC,
    MOVE_UNAVAILABLE,
};
```
