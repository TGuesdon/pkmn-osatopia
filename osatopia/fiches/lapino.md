# Famille Lapino

> Petit lapin soigneur de Dofus qui ne se bat vraiment qu'après sa mutation
> (lore et élément des sorts **à vérifier**). — Évolutions : Lapino → Lapigro
> (niv. 30). Constantes : `SPECIES_LAPINO`, `SPECIES_LAPINO_MUTANT`.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`, talent `ABILITY_SOIN_ALCHIMIQUE`). Compilation OK.

## Intention

Archétype : **soigneur-endurant** (principal) + **attaquant physique à
priorité** (secondaire). Références : Lockpin (physique lapin), Kapoera
(coups de poing, priorité), Mélodelfe/Chansey (soin).

Pourquoi : Lapino est un pur soigneur Fée. Le type Combat, Vampi-Poing et
toute l'offensive physique n'arrivent qu'avec Lapigro (niv. 30). Lapigro est
volontairement viable : 490 de total, stats équilibrées (seule l'AtqSpé est
basse), au niveau de Tofu Royal (495) mais Fée/Combat.

Distinct des monstres custom : aucun autre n'est Fée/Combat. Tigrimas et
Ronronchon sont des lanceurs spéciaux lents, Lapigro est un physique
polyvalent, plus rapide, qui se soigne.

## Mécanique : le combat arrive à l'évolution

- Lapino n'apprend **aucune attaque Combat**. Vampi-Poing arrive à l'évolution
  (niv. 30), Mach Punch à 32.
- Récompense inverse : un Lapino dont on bloque l'évolution apprend **Éclat
  Magique au niv. 36**, que Lapigro n'apprend jamais (`P_PRE_EVO_MOVES` à
  `FALSE`).
- Toutes les CT Combat sont réservées à Lapigro.

## Stades

| | Lapino | Lapigro |
|---|---|---|
| Types | Fée | Fée / Combat |
| PV | 60 | 85 |
| Attaque | 50 | 90 |
| Défense | 50 | 80 |
| Atq. Spé | 50 | 60 |
| Déf. Spé | 60 | 85 |
| Vitesse | 60 | 90 |
| Total | 330 | 490 |
| Talents | Poing de Fer / Soin Alchimique / caché : Prioguérison | idem |
| Capture / Exp. | 120 / 75 | 45 / 185 |
| EV | 1 Déf. Spé. | 1 Att. + 1 Déf. Spé. |

Stats sacrifiées : l'AtqSpé uniquement. Comparaison : Tofu Royal
(85 / 90 / 80 / 70 / 75 / 95 = 495), Moumouflon (490), Manternel (500).

Autres champs : `PERCENT_FEMALE(50)`, `.eggCycles = 15`,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`,
`MON_EGG_GROUPS(EGG_GROUP_FIELD, EGG_GROUP_FAIRY)`, `.bodyColor` à choisir
selon le sprite (`BODY_COLOR_PINK` par défaut).

## Talents

| Talent | Effet | Pourquoi |
|---|---|---|
| Poing de Fer (Iron Fist) | +20 % aux coups de poing | Vampi-Poing, Mach Punch, Poing Feu/Glace/Éclair, Dynamo-Poing |
| **Soin Alchimique** (custom) | Régénère 1/16 des PV max en fin de tour, **cumulable avec Restes** | Le côté soigneur : s'allie au drain et à Rayon Lune |
| Prioguérison (Triage) — caché | Capacités de soin prioritaires (+3) | Vampi-Poing est une capacité de soin dans le code : il passe prio +3 |

## Capacités custom

Aucune capacité. **Un talent custom**, Soin Alchimique : difficulté
**moyenne**. Il faut une constante `ABILITY_SOIN_ALCHIMIQUE`
(`include/constants/abilities.h`, comme Sève Avide et Terrier), une entrée dans
`src/data/abilities.h`, un cas en fin de tour dans `battle_util.c` calqué sur
Corps Gel (`ABILITY_ICE_BODY`, `SetHealAmount` à `maxHP / 16`), un script de
combat et sa chaîne de texte.

## Learnsets

Lapino (stade 1, jusqu'au niv. 30, plus la récompense à 36) :

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Physique | 40 | attaque de base |
| 1 | Rugissement (Growl) | Normal | Statut | – | baisse d'Attaque |
| 4 | Vent Féérique (Fairy Wind) | Fée | Spéciale | 40 | STAB faible |
| 8 | Vœu (Wish) | Normal | Statut | – | soin différé |
| 11 | Vampibaiser (Draining Kiss) | Fée | Spéciale | 50 | STAB drain |
| 14 | Rayon Lune (Moonlight) | Fée | Statut | – | soin |
| 17 | Charme (Charm) | Fée | Statut | – | baisse d'Attaque |
| 20 | Glas de Soin (Heal Bell) | Normal | Statut | – | soigne l'équipe |
| 24 | Voix Envoûtante (Alluring Voice) | Fée | Spéciale | 80 | STAB |
| 27 | Choc Émotionnel (Spirit Break) | Fée | Physique | 75 | STAB physique |
| 36 | Éclat Magique (Dazzling Gleam) | Fée | Spéciale | 80 | récompense si bloqué |

Lapigro (reprend les attaques de Lapino jusqu'au niv. 27 aux mêmes niveaux) :

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| Évo | Vampi-Poing (Drain Punch) | Combat | Physique | 75 | STAB drain |
| 32 | Mach Punch | Combat | Physique | 40 (prio +1) | priorité |
| 35 | Gonflette (Bulk Up) | Combat | Statut | – | boost Att/Déf |
| 38 | Câlinerie (Play Rough) | Fée | Physique | 90 | STAB fort |
| 46 | Close Combat | Combat | Physique | 120 | attaque finale |

Kit final : Vampi-Poing, Mach Punch, Câlinerie, Rayon Lune.

## CT, CS et tuteurs

| Attaque | Lapino | Lapigro |
|---|---|---|
| Toxik, Abri, Repos, Reflet, Clonage, Attraction, Blabla Dodo, Ténacité, Ronflement, Façade | ✔ | ✔ |
| E-Coque (Soft-Boiled), Rune Protect, Mur Lumière, Protection | ✔ | ✔ |
| Plaquage, Damoclès (tuteurs) | | ✔ |
| Poing Feu, Poing Glace, Poing Éclair, Ultimapoing | | ✔ |
| Casse-Brique, Gonflette, Dynamo-Poing, Mitra-Poing | | ✔ |
| Frappe Atlas, Riposte, Tunnel, Ultimawashi | | ✔ |

Exclusions volontaires : Vantardise, Danse-Lames, Séisme et les attaques
Psy ou Spectre, incohérentes avec le physique ; toute CT Combat pour Lapino.

## Annexe — bloc C
(à fournir sur demande)
