# Famille Gobgob

> Petit gobelin malicieux à queue, invocation de l'Osamodas ; le Gobglouton
> est sa version évoluée, plus gourmande. *(Lore de mémoire, à vérifier :
> éléments des sorts, zone, lien exact avec les invocations.)*
> Évolutions : Gobgob → Gobglouton (niv. 32).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` ; groupe d'œuf
`EGG_GROUP_HUMAN_LIKE` et couleur `BODY_COLOR_PURPLE` proposés (comme Gobet),
à confirmer.

## Intention

Archétype : **soutien / setup d'équipe** (le monstre prépare ses alliés, il ne
se booste pas pour taper), avec le **pivot** en secondaire. Il pose un écran,
monte ses défenses avec Stockage, puis passe la main : Queulonage laisse un
clone à l'allié suivant, Relais lui transmet les boosts défensifs.

Référence : **Grimalin / Angoliath** (Ténèbres/Fée, Farceur), dont il reprend
les types et le talent, mais sans le profil offensif. Différences avec les
monstres custom : Gobet / Gob Trotteur sont des Ténèbres rapides et
offensifs, Lapino / Lapigro sont Fée physiques sans écrans.

Rappel de nommage : **Protection = Reflect** (écran physique) et
**Mur Lumière = Light Screen** (écran spécial).

## Stades

| | Gobgob | Gobglouton |
|---|---|---|
| Types | Fée / Ténèbres | Fée / Ténèbres |
| PV | 50 | 90 |
| Attaque | 40 | 55 |
| Défense | 40 | 75 |
| Atq. Spé | 55 | 85 |
| Déf. Spé | 50 | 80 |
| Vitesse | 60 | 80 |
| **Total** | **295** | **465** |
| Talents | Farceur / Infiltration / Fouille (caché) | idem |
| Capture / Exp. | 120 / 68 | 45 / 175 |
| EV | 1 PV | 1 PV + 1 Déf. Spé |

PV et défenses sont favorisés pour encaisser le coût de Queulonage ; l'offensif
est volontairement modéré (Att 55, AtqSpé 85). Vitesse moyenne : la priorité
vient de Farceur, pas de la vitesse brute.

## Kit final

Queulonage · Stockage · Mur Lumière / Protection · Voix Envoûtante ou
Vibrobscur. Alternatives de soutien : Vœu, Provoc, Rayon Lune, Relais.

Talents : **Farceur** (priorité sur Queulonage, écrans, statuts),
**Infiltration** (traverse clones et écrans adverses, clin d'œil aux
invocations), **Fouille** (caché).

## Capacités custom

Aucune.

## Learnsets

Le Gobgob apprend ce qui précède le niveau 32 ; le Gobglouton reprend les mêmes
attaques aux mêmes niveaux et reçoit Queulonage à l'évolution
(`P_PRE_EVO_MOVES` = FALSE).

| Niv. | Attaque | Type | Cat. | Puiss. | Rôle |
|---|---|---|---|---|---|
| 1 | Voix Enjôleuse (Disarming Voice) | Fée | Spé | 40 | STAB faible |
| 1 | Charme (Charm) | Fée | Statut | - | -2 Att |
| 4 | Morsure (Bite) | Ténèbres | Phys | 60 | STAB Ténèbres |
| 8 | Regard Touchant (Baby-Doll Eyes) | Fée | Statut | - | Priorité |
| 12 | Vampibaiser (Draining Kiss) | Fée | Spé | 50 | STAB + drain |
| 16 | Provoc (Taunt) | Ténèbres | Statut | - | Perturbation |
| 20 | Mur Lumière (Light Screen) | Psy | Statut | - | Écran spécial |
| 23 | Aboiement (Snarl) | Ténèbres | Spé | 55 | STAB Ténèbres spé |
| 26 | Protection (Reflect) | Psy | Statut | - | Écran physique |
| 30 | Rayon Lune (Moonlight) | Fée | Statut | - | Soin |
| Évo (32) | Queulonage (Shed Tail) | Normal | Statut | - | Signature, pivot |
| 34 | Voix Envoûtante (Alluring Voice) | Fée | Spé | 80 | STAB principal |
| 38 | Stockage (Stockpile) | Normal | Statut | - | Boost défensif (×3) |
| 38 | Relâche (Spit Up) | Normal | Spé | 1 | Libère Stockage |
| 38 | Avale (Swallow) | Normal | Statut | - | Soin via Stockage |
| 42 | Vibrobscur (Dark Pulse) | Ténèbres | Spé | 80 | STAB Ténèbres |
| 46 | Vœu (Wish) | Normal | Statut | - | Soutien |
| 50 | Relais (Baton Pass) | Normal | Statut | - | Passe les boosts |

Avale et Relâche sont apprises au niveau 38, avec Stockage (comme Avaltout).

## CT, CS et tuteurs

Mêmes attaques pour les deux stades, sauf mention. Les universelles (Clonage,
Copie…) sont déjà incluses pour tous les monstres.

| Attaque | Source | Stades |
|---|---|---|
| Toxik, Repos, Abri | CT | les deux |
| Protection, Mur Lumière, Rune Protect, Reflet | CT | les deux |
| Provoc, Tourmente, Attraction, Échange | CT | les deux |
| Façade, Larcin | CT | les deux |
| Ball'Ombre, Psyko | CT | Gobglouton seul |
| Vantardise, Cage Éclair, Boost, E-Coque, Ténacité, Blabla Dodo | Tuteur | les deux |
| Coupe | CS | Gobglouton seul |

Exclusions volontaires : Plénitude et Gonflette (pas d'auto-boost offensif),
Danse-Lames, Pouvoir Lunaire, Poing Feu / Glace / Éclair, Séisme, Surf,
Lance-Flammes (pas de couverture offensive large).
