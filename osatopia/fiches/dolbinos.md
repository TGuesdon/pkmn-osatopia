# Famille Dolbinos

> Gros oiseau un peu bizarre, dont l'évolution, Dokachu, s'inspire de Pikachu.
> Lore Dofus (éléments des sorts, zone) **à vérifier**.
> Évolutions : Dolbinos → Dokachu (niv. 32).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

## Intention

Archétype : attaquant à boost (sweeper spécial), secondaire nettoyeur rapide.
Références : Raichu (kit Électrik, Hâte), Fulgulairo (profil Électrik/Vol
spécial), Kwak Feu (autre oiseau spécial déjà dans Osatopia).

Mécanique « bizarre » : **Lunatique** (Moody) comme talent principal. Le seul
boost direct est **Hâte** (Vit +2). Pas de Machination ni de Plénitude :
l'AtqSpé ne monte que par hasard avec Lunatique. Garde-fou contre l'Esquive que
Lunatique peut monter : **Météores** (ne rate jamais).

## Stades

| | Dolbinos | Dokachu |
|---|---|---|
| Types | Vol | Vol / Électrik |
| PV | 60 | 80 |
| Attaque | 45 | 55 |
| Défense | 50 | 65 |
| Atq. Spé | 65 | 100 |
| Déf. Spé | 45 | 70 |
| Vitesse | 65 | 90 |
| **Total** | **330** | **460** |
| Évolution | niv. 32 | – |
| Talents | Lunatique / Statik / Paratonnerre (caché) | idem |
| Capture / Exp. | 120 / 90 | 60 / 185 |
| EV | AtqSpé +1 | AtqSpé +2, Vit +1 |

Comparaisons (outil `similaires`) : Fulgulairo (490, Vit 125), Élecsprint (475),
Élektek (490) ; côté Osatopia, Kwak Feu (500, Feu/Vol) : pas de doublon.
Stats sacrifiées : l'Attaque (purement spécial) et les défenses, moyennes.

## Kit final

| Emplacement | Choix | Type · Cat. | Puiss. |
|---|---|---|---|
| Boost | **Hâte** (Agility) | Psy · Statut | – |
| Garde-fou | **Météores** (Swift) | Normal · Spé. | 60 |
| STAB Électrik | **Tonnerre** (Thunderbolt) | Électrik · Spé. | 90 |
| STAB Vol | **Lame d'Air** (Air Slash) | Vol · Spé. | 75 |

Talents : Lunatique (Moody), Statik (Static), Paratonnerre (Lightning Rod) en
talent caché.

## Capacités custom

Aucune.

## Learnsets

Dokachu reprend les attaques de Dolbinos aux mêmes niveaux et apprend en plus
celles de la seconde table.

### Dolbinos

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| 1 | Tornade (Gust) | Vol | Spé. | 40 | STAB faible |
| 1 | Danse Plumes (Feather Dance) | Vol | Statut | – | Att −2 |
| 5 | Éclair (Thunder Shock) | Électrik | Spé. | 40 | Annonce le futur type |
| 9 | Cage Éclair (Thunder Wave) | Électrik | Statut | – | Paralysie |
| 12 | Météores (Swift) | Normal | Spé. | 60 | Garde-fou |
| 16 | Tranch'Air (Air Cutter) | Vol | Spé. | 60 | STAB, critiques |
| 20 | Change Éclair (Volt Switch) | Électrik | Spé. | 70 | Pivot |
| 24 | Hâte (Agility) | Psy | Statut | – | Boost de Vit |
| 28 | Lame d'Air (Air Slash) | Vol | Spé. | 75 | STAB principal |

### Dokachu

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| Évo | Coup d'Jus (Discharge) | Électrik | Spé. | 80 | Premier STAB Électrik fort |
| 34 | Vent Arrière (Tailwind) | Vol | Statut | – | Soutien |
| 38 | Tonnerre (Thunderbolt) | Électrik | Spé. | 90 | STAB principal |
| 42 | Atterrissage (Roost) | Vol | Statut | – | Soin |
| 46 | Vent Violent (Hurricane) | Vol | Spé. | 110 | Attaque finale |
| 50 | Fatal-Foudre (Thunder) | Électrik | Spé. | 110 | Attaque finale |

Temporisation : Tonnerre arrive 6 niveaux après l'évolution (32 → 38).

## CT, CS et tuteurs

| | Dolbinos | Dokachu |
|---|---|---|
| Toxik, Abri, Repos, Façade, Reflet, Attraction | ✅ | ✅ |
| Tourmente, Provoc | ✅ | ✅ |
| Mur Lumière, Protection, Rune Protect | ✅ | ✅ |
| Onde de Choc | ✅ | ✅ |
| Vol (CS) | ✅ | ✅ |
| Blabla Dodo, Ténacité (tuteurs) | ✅ | ✅ |
| Psyko, Ball'Ombre | – | ✅ |
| Ultralaser | – | ✅ |

Exclus volontairement :
- **Tonnerre** et **Fatal-Foudre** en CT : ils casseraient la temporisation ;
- **Laser Glace** : pas de sens pour ce monstre ;
- **Plénitude**, Gonflette, Danse Lames, Vantardise : boosts refusés ;
- **Boost Copie** et **Échange Talent** : trop forts avec Lunatique ;
- attaques physiques et coups de poing (Att 55).

## Annexe — bloc C

Voir `src/data/pokemon/species_info.h` (`SPECIES_DOLBINOS`, `SPECIES_DOKACHU`).
