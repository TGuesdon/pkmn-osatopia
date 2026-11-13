# Famille Folle

> Poupées animées invoquées par les Sadida. *La Folle* agace sa cible
> (*Agacement* : -3 PA, ou poison Air dans la version actuelle) ; *La
> Bloqueuse* n'attaque pas : elle retient l'ennemi (Tacle, *Substitution*,
> *Célérité*) et résiste à tous les éléments (+20 %).
> — Évolutions : Folle → Bloqueuse (niv. 25).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Refonte : les deux espèces existaient avec les stats et le learnset du dex
d'origine, sans CT. Sexe (`PERCENT_FEMALE(50)`), `.eggCycles = 20`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_FAST` (comme Qulbutoké), groupes d'œuf Plante / Fée et
`BODY_COLOR_BROWN` sont conservés.

## Intention

Archétype : **perturbateur** (Folle, « entraver ») → **perturbateur + mur
piégeur** (Bloqueuse, « bloquer »). La Folle ralentit et dérègle (Entrave,
Bombe au Sirop, Para-Spore, Onde Folie) ; la Bloqueuse piège (Barrage,
Marque Ombre), draine (Vampigraine), enferme (Encore) et empêche de se
soigner (Dissonance Psy), avec Requiem comme condition de victoire.

Références : **Qulbutoké** (piège, Encore, Riposte), **Ténéfix** (Farceur
perturbateur).

Plante/Psy : Plante pour la Sadida, Psy pour la poupée animée.

## Stades

| | Folle | Bloqueuse |
|---|---|---|
| Types | Plante/Psy | Plante/Psy |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 70 / 35 / 55 / 60 / 65 / 55 | 115 / 40 / 90 / 65 / 105 / 70 |
| Total | 340 | 485 |
| Talents | Farceur / Corps Maudit / caché : Marque Ombre | Farceur / Corps Maudit / caché : Marque Ombre |
| Capture / Exp. | 120 / 70 | 45 / 175 |
| EV | 1 DéfSpé | 2 PV |

Stats sacrifiées : Attaque (poupée de chiffon, kit spécial ou de statut) et
AtqSpé de la Bloqueuse (elle use, elle ne tue pas). Vitesse 70 pour la
Bloqueuse (les PM et la *Célérité* de Dofus), ce qui la distingue de Mol Usk
(mur spécial lent, 35).

## Kit final (Bloqueuse)

| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Bloquer | Barrage (Block) | Normal | Statut | – |
| Tenir / drainer | Vampigraine (Leech Seed) | Plante | Statut | – |
| Entraver | Encore (Encore) | Normal | Statut | – |
| STAB Psy | Dissonance Psy (Psychic Noise) | Psy | Spé | 75 |

Avec Farceur, Barrage, Vampigraine et Encore passent en priorité.
Alternatives : Regard Noir, Requiem, Possessif, Anti-Soin (bloquer) ;
Provoc, Entrave, Tourmente (entraver) ; Sort Sinistre, Psyko (STAB Psy) ;
Racines, Giga-Sangsue, Synthèse (tenir).

Talents : **Farceur** (statuts prioritaires), **Corps Maudit** (entrave
l'attaque qui le touche), **Marque Ombre** caché (personne ne fuit).

## Capacités custom

Aucune.

## Learnsets

### Folle

| Niv. | Attaque FR (EN) | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Vole-Vie (Absorb) | Plante | Spé | 20 |
| 1 | Rugissement (Growl) | Normal | Statut | – |
| 4 | Onde Folie (Confuse Ray) | Spectre | Statut | – |
| 7 | Choc Mental (Confusion) | Psy | Spé | 50 |
| 10 | Para-Spore (Stun Spore) | Plante | Statut | – |
| 13 | Méga-Sangsue (Mega Drain) | Plante | Spé | 40 |
| 16 | Entrave (Disable) | Normal | Statut | – |
| 19 | Bombe au Sirop (Syrup Bomb) | Plante | Spé | 60 |
| 22 | Rafale Psy (Psybeam) | Psy | Spé | 65 |
| 26 | Encore (Encore) | Normal | Statut | – |
| 30 | Giga-Sangsue (Giga Drain) | Plante | Spé | 75 |
| 34 | Sort Sinistre (Eerie Spell) | Psy | Spé | 80 |
| 38 | Synthèse (Synthesis) | Plante | Statut | – |
| 42 | Psyko (Psychic) | Psy | Spé | 90 |
| 46 | Éco-Sphère (Energy Ball) | Plante | Spé | 90 |

### Bloqueuse

| Niv. | Attaque FR (EN) | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Barrage (Block) | Normal | Statut | – |
| 1–22 | socle identique à la Folle | | | |
| 28 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 31 | Encore (Encore) | Normal | Statut | – |
| 34 | Giga-Sangsue (Giga Drain) | Plante | Spé | 75 |
| 37 | Dissonance Psy (Psychic Noise) | Psy | Spé | 75 |
| 40 | Racines (Ingrain) | Plante | Statut | – |
| 43 | Possessif (Imprison) | Psy | Statut | – |
| 47 | Psyko (Psychic) | Psy | Spé | 90 |
| 51 | Requiem (Perish Song) | Normal | Statut | – |

Temporisation : garder la Folle donne Encore plus tôt et ses exclusives
(Sort Sinistre, Synthèse, Éco-Sphère) ; évoluer donne tout le piège.

## CT, CS et tuteurs

| Attaque | Folle | Bloqueuse |
|---|---|---|
| Toxik, Provoc, Tourmente, Abri, Repos, Attraction, Zénith | ✓ | ✓ |
| Mur Lumière, Protection, Rune Protect, Plénitude, Échange | ✓ | ✓ |
| Giga-Sangsue, Lance-Soleil, Psyko, Ball'Ombre | ✓ | ✓ |
| Tuteurs : Cage Éclair, Vantardise, Métronome, Boost, Ténacité, Blabla Dodo, Ronflement | ✓ | ✓ |
| Tuteur : Riposte (clin d'œil à Qulbutoké) | | ✓ |

Exclusions volontaires : poings et Danse-Lames (poupée de chiffon), Balle
Graine et Façade (physiques, inutiles avec 35–40 d'Attaque), Reflet
(l'esquive n'est pas un piège), Coupe, Flash et les autres CS.
