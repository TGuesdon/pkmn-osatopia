---
name: concevoir-monstre
description: Aide à concevoir un monstre Dofus pour Osatopia (hack de Pokémon Émeraude). Couvre les stats, les types, les talents, le learnset, les capacités custom, les CT, la capture et l'intégration dans le code, à partir d'un archétype stratégique et de Pokémon de référence, le tout en français. À utiliser quand l'utilisateur veut concevoir, équilibrer ou revoir un monstre ou une famille (ex. « conçois la famille Tofu », « je veux que Bwak joue comme Nirondelle »).
---

# Concevoir un monstre Osatopia

Tu es un assistant de game design. Tu guides l'utilisateur, tu proposes des
options, il tranche. Tu produis une **fiche de conception** en français, puis
tu l'intègres dans le code. Tu ne modifies `src/` qu'une fois la fiche
validée (étape 10). Jamais `include/`.

La validation de la fiche est le **dernier point d'arrêt** : ensuite tu
enchaînes seul l'écriture de la fiche, l'intégration, la compilation, le
commit, le push et la PR, sans redemander de confirmation entre ces étapes.
Tu ne t'arrêtes que si quelque chose bloque (échec de `make`, écart avec la
fiche que tu ne sais pas résoudre, conflit) ou si l'utilisateur a dit qu'il
ne voulait que la fiche.

## Règles

- **Conception en français** : la discussion et la fiche utilisent les noms
  FR d'attaques, de talents, de types et de Pokémon. N'invente jamais un nom
  FR de mémoire. Vérifie-le avec l'outil ci-dessous ou dans `data/*.csv`.
  Mets le nom anglais entre parenthèses quand c'est utile.
- **Jeu en anglais** : tout texte affiché en jeu (nom et description de
  capacité ou de talent custom, messages de combat, catégorie Pokédex, objet)
  est en anglais, comme le reste de pokeemerald-expansion. Seules exceptions :
  les noms propres inventés par Dofus (Tofu, Blop, cawotte…) et les talents
  liés à un Dofus (Turquoise, Pourpre, Ébène, Vulbis…). Les constantes
  (`MOVE_*`, `ABILITY_*`) gardent le nom FR de conception. Reporte chaque
  nouveau nom dans `osatopia/noms_en_jeu.md`.
- **Données réelles uniquement** : stats, puissances et learnsets viennent de
  l'outil, qui lit le repo. Ne cite pas de chiffres de mémoire.
- **Movepool complet** : ne te limite pas aux attaques classiques. Pour chaque
  emplacement, propose **plusieurs options** (3–5) et privilégie la variété
  par rapport aux monstres déjà conçus.
- **Attaques inutilisables** : écarte celles dont la description dit « Cette
  capacité ne peut pas être utilisée » (Retour, Frustration, Puissance Cachée,
  Force Cachée, Feinte, Poursuite, Saisie, Flash, Mimique…).
- **Une étape à la fois** : pose les questions d'une étape, attends la
  réponse, puis passe à la suivante. Si l'utilisateur donne déjà beaucoup
  d'infos d'entrée, saute les questions déjà répondues.

## L'outil

Depuis la racine du repo :

```bash
T=".claude/skills/concevoir-monstre/scripts/osatopia.py"
python3 $T fiche Scarabrute            # stats, types, talents, learnset en FR (aussi : nom EN, SPECIES_X, monstre custom)
python3 $T fiche Scarabrute --complet  # + CT/tuteurs et attaques œuf
python3 $T attaques --type plante --categorie physique --pmin 60 --pmax 90
python3 $T attaques --prio                     # attaques prioritaires
python3 $T attaques --texte "soigne" --desc    # recherche dans les descriptions FR
python3 $T attaques --effet HIT_ESCAPE         # par effet technique (EFFECT_X), ici les attaques pivot
python3 $T talents --texte vitesse
python3 $T similaires 70 69 54 53 50 95        # Pokémon au profil de stats proche (PV Att Déf AtqSpé DéfSpé Vit)
python3 $T similaires 70 69 54 53 50 95 --custom  # … parmi les monstres Osatopia
python3 $T custom                              # monstres conçus / à concevoir + learnsets en double
```

Pour le lore Dofus, `dofusdb.py` interroge l'API de DofusDB (réseau requis,
réponses en cache 30 jours dans `data/dofusdb_cache/`) :

```bash
D=".claude/skills/concevoir-monstre/scripts/dofusdb.py"
python3 $D fiche Tofu             # grades (PV, PA, PM, caracs), résistances, sorts détaillés, zones
python3 $D fiche 98 --grade 1     # par id DofusDB (utile s'il y a des homonymes)
python3 $D famille Tofu           # tous les monstres de la race, triés par niveau
python3 $D cherche bouftou        # trouver le bon nom ou id
```

Lecture des données Dofus → Pokémon :
- **Élément des sorts** → type principal (Terre → Sol/Roche, Feu → Feu,
  Eau → Eau/Glace, Air → Vol/Électrik, Neutre → Normal/Combat…).
- **Résistances négatives / positives** → idée de faiblesses / résistances.
- **PV, PM, PA, caractéristiques** → tendance du profil (PM élevés = Vitesse,
  PV élevés = encaisseur…), à relativiser par rapport à la famille.
- **Effets des sorts** (vol de vie, poison, retrait de PA, invocation,
  bouclier, poussée…) → capacités custom et `EFFECT_*` proches (étape 6).
- **Zones** → habitat, utile pour le lore et le placement dans le jeu.
- **Famille** → candidats pour les stades et les évolutions.

Les données reflètent la version actuelle de Dofus : si l'utilisateur a
une autre version en tête, sa parole prime.

Références à lire au moment voulu :
- `references/archetypes.md` : archétypes stratégiques et d'aventure (étape 3).
- `references/reperes.md` : total de stats par stade, niveaux d'évolution,
  progression des puissances, niveaux des champions (étapes 4 et 7).

## Déroulé

Commence par `osatopia.py custom` pour situer le monstre parmi ceux déjà
conçus. Si le monstre existe déjà en placeholder, lis aussi sa fiche
(`fiche <nom>`) pour récupérer sa constante et sa chaîne d'évolution.

### 1. Identité
- Nom Dofus, famille et nombre de stades, constantes `SPECIES_*` si elles existent.
- Lore Dofus : lance `dofusdb.py fiche <nom>` (et `famille` pour une famille)
  et résume l'élément des sorts, les sorts marquants, le profil (PV/PM/PA,
  résistances) et les zones. Si DofusDB ne trouve pas le monstre ou si le
  réseau est indisponible, propose ce que tu sais et **signale-le comme à vérifier**.
- Niveaux d'évolution.

### 2. Références
Demande 1 à 3 Pokémon : « il joue comme X », « il a le physique de stats de Y ».
Lis la fiche de chacun. Résume ce que chaque référence apporte (profil de stats,
idée de kit, talent intéressant). Si l'utilisateur n'a pas d'idée, propose-en
à partir de l'archétype ou de `similaires`.

### 3. Archétype et types
Propose 1 archétype principal (+1 secondaire facultatif), tiré de
`references/archetypes.md`, avec une phrase sur ce que ça implique. Propose
les types (lien avec l'élément Dofus) et leur évolution éventuelle par stade
(ex. Plante → Plante/Vol).

### 4. Stats
Pour chaque stade, propose les 6 stats et leur total en respectant les
fourchettes de `references/reperes.md`. Présente un tableau comparatif :
le monstre, ses références, et 2–3 résultats de `similaires` (dont un
`--custom` pour vérifier qu'il ne double pas un monstre Osatopia). Justifie
en une ligne les stats sacrifiées.

### 5. Kit final (stade final, vers niv. 40–50)
4 emplacements, chacun avec un rôle (« STAB fort », « boost », « couverture
contre Sol », « utilitaire »…). Pour chacun, liste **3–5 options** trouvées
avec `attaques`, avec type, catégorie, puissance et une note courte. Puis
2–3 talents possibles (`talents`), dont un éventuel talent caché.

### 6. Capacités custom (si l'utilisateur en veut)
Pour chaque capacité inspirée d'un sort Dofus :
- nom FR de conception et **nom anglais affiché en jeu** (≤ 12 caractères
  conseillés pour l'affichage GBA), type, catégorie,
  puissance, précision, PP, effet ;
- **attaque existante la plus proche** et son `EFFECT_*`
  (`attaques --effet X` liste celles qui partagent un effet) ;
- difficulté : **facile** si on réutilise un `EFFECT_*` existant (une entrée
  dans `moves_info.h` + une constante), **moyenne** pour une variante proche,
  **difficile** si l'effet est nouveau (code de combat en C).

Textes en anglais (vérifiés par `test/text.c`, en pixels et non en caractères) :
description de talent ≤ 146 px (≈ 25 caractères, une ligne), description
d'attaque ≤ 152 px par ligne (≈ 27 caractères, deux lignes), nom d'attaque
≤ 72 px en police étroite, description Pokédex ≤ 224 px par ligne
(≈ 40 caractères, 4 lignes max), catégorie Pokédex ≤ 12 caractères. La
taille (`.height`) est en décimètres et le poids (`.weight`) en hectogrammes
(Tacle Lourd, Balayage et Nœud Herbe en dépendent). Les accents, `m`, `w` et `%` sont larges. Mesure
avec `python3 .claude/skills/concevoir-monstre/scripts/largeur_textes.py
"Texte"` ; sans argument, le script liste tous les textes trop larges.

Une capacité custom touche souvent des listes de tests codées en dur, à
mettre à jour dans le même commit (`make check` les signale) :
- attaque offensive avec `additionalEffects` (chance > 0) : ajoute-la à
  `IsMoveSheerForceBoosted` dans `test/battle/ability/sheer_force.c` ;
- capacité qui cible le lanceur (`MOVE_TARGET_USER`), ou effet `EFFECT_OHKO` :
  exclus son effet de « AI can use all moves, 801-900 »
  (`test/battle/ai/can_use_all_moves.c`), comme Wish ou Guillotine, et teste
  son IA à part (`test/battle/ai/ai_potager.c` sert de modèle).

Chaque nouvelle espèce agrandit les drapeaux Pokédex de SaveBlock1 ;
`test/save.c` en tient compte automatiquement.

### 7. Learnset de progression
Reconstruit à rebours depuis le kit final, en suivant `references/reperes.md` :
STAB faible dès le niveau 1–5, montée en puissance, une attaque d'évolution
par stade, ~14–18 attaques. Présente un tableau par stade : niveau, attaque FR,
type, catégorie, puissance, rôle. Vérifie qu'aucune attaque forte n'arrive trop
tôt par rapport aux champions, et que le learnset ne ressemble pas à celui d'un
autre monstre custom.

Les stades suivants reprennent les attaques de base du premier stade aux mêmes
niveaux. `P_PRE_EVO_MOVES` est à `FALSE` : un stade final ne réapprend pas les
attaques exclusives du stade précédent, ce qui permet des mécaniques de
temporisation (une attaque apprise après le niveau d'évolution, comme Séisme
chez Gwotofu).

### 8. CT, CS et tuteurs
Pars de ce qui existe dans le jeu, pas de mémoire :
- CT et CS : `FOREACH_TM` / `FOREACH_HM` dans `include/constants/tms_hms.h` ;
- tuteurs : `grep -h "setvar VAR_0x8005, MOVE_" data/scripts/*.inc data/maps/*/scripts.inc` ;
- universelles : `sUniversalMoves` dans `src/pokemon.c` (Copie, Clonage…).
  Tous les monstres les ont, ne les liste pas.

Propose un tableau par stade : un socle commun (statut, STAB, attaques
d'objet), puis 2–4 couvertures **cohérentes avec le physique du monstre**
(un oiseau n'a pas de coups de poing). Note ce qui est exclu volontairement,
surtout les CT qui casseraient une mécanique du learnset.

### 9. Capture, expérience et EV
Valeurs de `references/reperes.md`. EV selon le rôle de chaque stade : 1 au
premier stade, 2 au deuxième, 3 au final, sur la ou les stats qui définissent
le rôle. Compare avec une famille custom proche (`grep -A45 "\[SPECIES_X\]"
src/data/pokemon/species_info.h`).

### Fiche (après validation)
Avant d'écrire, présente le récapitulatif complet et demande une seule fois
« Je valide et j'intègre ? ». Cette réponse vaut feu vert pour la fiche,
l'intégration, le commit et la PR. Quand l'utilisateur valide, écris la fiche
dans `osatopia/fiches/<famille>.md` (crée le dossier si besoin) et passe
directement à l'étape 10. Format :

```markdown
# Famille <Nom>

> <Lore Dofus en 1-2 phrases> — Évolutions : …

## Intention
Archétype : … · Références : … · Pourquoi : …

## Stades
| | Bebitouf | Bitouf | Bitouvol |
|---|---|---|---|
| Types | … | … | … |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | … | … | … |
| Total | … | … | … |
| Talents | … | … | … |
| Capture / Exp. | … | … | … |
| EV | … | … | … |

## Kit final
…

## Capacités custom
…

## Learnsets
(un tableau par stade : niveau · attaque FR (EN) · type · cat. · puiss.)

## CT, CS et tuteurs
(un tableau des attaques × stades, puis les exclusions volontaires)

## Annexe — bloc C (à copier à la main)
```

La fiche peut être écrite au fil des étapes avec un champ **État** (« en
cours », « validée », « validée et intégrée »).

L'annexe C est facultative, à fournir si l'utilisateur la demande. Elle
reprend le style de `src/data/pokemon/species_info.h` (champs `.baseHP`…
`.abilities`, `.catchRate`, `.expYield`, `.evYield_*`, `.evolutions`) et de
`src/data/pokemon/level_up_learnsets/gen_9.h`
(`LEVEL_UP_MOVE(niv, MOVE_X)`, niveau 0 = à l'évolution). Elle utilise les
constantes `MOVE_*` / `ABILITY_*` exactes données par l'outil.

### 10. Intégration (enchaînée après la validation)
Les monstres à concevoir existent déjà en placeholder dans
`src/data/pokemon/species_info.h` (Plante, 10 partout, Puanteur, capture 3,
asexué, sans œuf, bonheur 0, croissance lente). Pour chaque stade :
- remplace stats, types, `.catchRate`, `.expYield`, `.evYield_*`,
  `.abilities` ;
- remplace aussi les autres placeholders, faute de choix de l'utilisateur, par
  les valeurs de la famille Bitouf : `PERCENT_FEMALE(50)`, `.eggCycles = 15`,
  `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`, `EGG_GROUP_FLYING` ou le
  groupe adapté, `.bodyColor` selon le monstre. Signale-le dans ton compte
  rendu ;
- ajoute `.levelUpLearnset`, `.teachableLearnset` et `.evolutions` avant
  `FOOTPRINT(...)` ;
- ne touche pas aux champs Pokédex et graphismes.

Learnsets : ajoute les tableaux à la fin de
`src/data/pokemon/level_up_learnsets/gen_9.h`. CT : ajoute
`s<Nom>TeachableLearnset` à la main à la fin de
`src/data/pokemon/teachable_learnsets.h` (triés, terminés par
`MOVE_UNAVAILABLE`). Les monstres custom ne sont pas dans les JSON de
`make_teachables.py`, qui laisse leurs tableaux tels quels (correctif de la
PR #4 ; sans lui, le script plante sur une espèce custom à la régénération).

Une capacité ou un talent custom s'ajoute aussi à `osatopia/noms_en_jeu.md`
(nom de conception → nom anglais en jeu).

Vérifie avec `osatopia.py fiche <nom> --complet` que tout correspond à la
fiche, puis compile (`make`, long : en arrière-plan). Si `make` échoue,
corrige et relance ; ne t'arrête pour demander que si tu ne trouves pas la
cause. Passe la fiche à « validée et intégrée ».

### 11. Commit et PR (enchaînés, sans redemander)
Dès que `make` passe :
- si tu es sur `master`, crée d'abord une branche `claude/<famille>-…` ;
- un seul commit avec la fiche et le code :
  `feat(dex): intègre la famille <Nom>` (ajoute « et la capacité <X> » s'il y
  a une capacité custom) ;
- `git push -u origin HEAD`, puis `gh pr create --base master` avec le même
  titre et ce corps :

```markdown
## Résumé
- Intègre <Stade 1> (<Types>, <Total>) → … à partir de la fiche `osatopia/fiches/<famille>.md`.
- <Archétype, talents, mécanique clé du kit>
- <Learnsets et CT, exclusions volontaires>
- <Placeholders remplacés par les valeurs Bitouf, le cas échéant>

## Vérifications
- `osatopia.py fiche <Noms> --complet` correspond à la fiche.
- `make` passe.
- <Points à vérifier, ex. lore Dofus>
```

Termine par un compte rendu court avec le lien de la PR et ce qui reste à
vérifier.

## Mettre à jour les glossaires

Les CSV de `data/` viennent de PokeAPI. Pour les régénérer (nouvelle version
de l'expansion), télécharge les CSV listés dans
`scripts/generer_glossaires.py` puis lance
`python3 scripts/generer_glossaires.py <dossier_csv>`.
