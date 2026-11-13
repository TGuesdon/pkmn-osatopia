# Famille Minikrone

> Licorne féerique, joyeuse et rapide, qui sombre dans la mélancolie en
> évoluant. DofusDB ne donne ni sorts ni résistances (Minikrone : invocation
> et monstre de quête ; Rainikrone : monstre de quête de Nimotopia) : le
> concept vient de la conception, **lore à vérifier**. — Évolutions :
> Minikrone → Rainikrone (niv. 35). Constantes : `SPECIES_MINIKRONE`,
> `SPECIES_RAINIKRONE`.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Compilation OK.

## Intention

Archétype : **tank offensif mixte** (principal) + **monstre de niche**
(secondaire, mécanique de la dépression). Référence : Galopa de Galar
(licorne Fée mixte, Vent Féérique, Hâte, Vœu Soin, corne).

Pourquoi : Lunatique donne +2 à une stat au hasard chaque tour (pas
Précision ni Esquive, réglage Gen 8+). Rainikrone doit donc **tenir** pour
cumuler les humeurs et pouvoir frapper en physique comme en spécial, avec
Force Ajoutée qui grandit à chaque boost. Le récit est dans les stats :
Minikrone est rapide et joyeuse, Rainikrone **perd de la Vitesse** (80 → 65)
et gagne PV, défenses et Attaque Spéciale.

Distinct des monstres custom : aucun Fée pur mixte et lent. Lapino/Lapigro
(Fée/Combat soigneur), Kitsou (Fée rapide spécial), Tigrimas (Fée/Feu
spécial) jouent autrement.

## Stades

| | Minikrone | Rainikrone |
|---|---|---|
| Types | Fée | Fée |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 50 / 65 / 45 / 60 / 50 / 80 | 85 / 80 / 75 / 100 / 85 / 65 |
| Total | 350 | 490 |
| Talents | Fuite / Voile Pastel / caché : Lunatique | Lunatique / Voile Pastel / caché : Lunatique |
| Capture / Exp. | 120 / 80 | 45 / 180 |
| EV | 1 Vit. | 1 PV + 1 AtqSpé |

Stats sacrifiées : défenses de Minikrone (jeune pouliche), Vitesse de
Rainikrone (la dépression, compensée par Lunatique). Comparaison : Galopa de
Galar (65 / 100 / 70 / 80 / 80 / 105 = 500), Mélodelfe (483), Cupcanaille
(480) ; custom les plus proches : Minotot, Gangredogue (plus offensifs).

Autres champs : `PERCENT_FEMALE(50)`, `.eggCycles = 15`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_FAST` (comme Ponyta),
`MON_EGG_GROUPS(EGG_GROUP_FIELD, EGG_GROUP_FAIRY)`, `BODY_COLOR_PINK`
(Minikrone) et `BODY_COLOR_BLUE` (Rainikrone).

## Kit final (Rainikrone, niv. 40–50)

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB Fée spécial | Vapeur Féérique (Strange Steam) — 90, confusion | Pouvoir Lunaire, Voix Envoûtante, Éclat Magique |
| STAB physique / corne | Choc Émotionnel (Spirit Break) — 75, baisse AtqSpé | Câlinerie, Estocorne, Coupe Psycho |
| Synergie Lunatique | Force Ajoutée (Stored Power) — 20 +20/boost | Arrogance, Relais, Boost |
| Dépression | Croco Larme (Fake Tears) — DéfSpé −2 | Larme à l'Œil, Rayon Lune, Vœu Soin |

## Capacités custom

Aucune.

## Learnsets

Tronc commun (les deux stades, aux mêmes niveaux) :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Physique | 40 |
| 1 | Regard Touchant (Baby-Doll Eyes) | Fée | Statut | – (prio +1) |
| 5 | Voix Enjôleuse (Disarming Voice) | Fée | Spéciale | 40 |
| 9 | Doux Baiser (Sweet Kiss) | Fée | Statut | – |
| 13 | Koud'Korne (Horn Attack) | Normal | Physique | 65 |
| 17 | Rafale Psy (Psybeam) | Psy | Spéciale | 65 |
| 21 | Hâte (Agility) | Psy | Statut | – |
| 25 | Choc Émotionnel (Spirit Break) | Fée | Physique | 75 |
| 29 | Estocorne (Smart Strike) | Acier | Physique | 70 |
| 33 | Rayon Lune (Moonlight) | Fée | Statut | – |

Minikrone seule (si l'évolution est bloquée, elle reste joyeuse) :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 38 | Câlinerie (Play Rough) | Fée | Physique | 90 |
| 44 | Pouvoir Lunaire (Moonblast) | Fée | Spéciale | 95 |

Rainikrone seule (`P_PRE_EVO_MOVES` à `FALSE`) :

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Croco Larme (Fake Tears) | Ténèbres | Statut | – |
| 38 | Larme à l'Œil (Tearful Look) | Normal | Statut | – |
| 41 | Force Ajoutée (Stored Power) | Psy | Spéciale | 20 +20/boost |
| 44 | Vapeur Féérique (Strange Steam) | Fée | Spéciale | 90 |
| 48 | Vœu Soin (Healing Wish) | Psy | Statut | – |

## CT, CS et tuteurs

Identiques pour les deux stades :

| Source | Attaques |
|---|---|
| CT socle | Toxik, Abri, Repos, Façade, Attraction, Reflet, Mur Lumière, Protection, Rune Protect, Zénith, Danse Pluie |
| CT couverture | Psyko, Ball'Ombre, Queue de Fer, Tonnerre, Provoc, Échange, Ultralaser |
| CS | Force, Éclate-Roc |
| Tuteurs | Plaquage, Damoclès, Ultimawashi, Ténacité, Boost, Météores, Cage Éclair, Vantardise, Dévorêve, Métronome, Blabla Dodo, Ronflement |

Exclusions volontaires : **Plénitude** (la source de boosts doit rester
Lunatique, aléatoire) ; coups de poing, Lance-Soleil, Surf, Vol
(incohérents avec une licorne) ; capacités inutilisables (Frustration,
Retour, Puissance Cachée, Force Cachée, Saisie, Flash).

## Annexe — bloc C
(à fournir sur demande)
