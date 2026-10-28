---
name: concevoir-monstre
description: Aide à concevoir un monstre Dofus pour Osatopia (hack de Pokémon Émeraude). Couvre les stats, les types, les talents, le learnset et les capacités custom, à partir d'un archétype stratégique et de Pokémon de référence, le tout en français. À utiliser quand l'utilisateur veut concevoir, équilibrer ou revoir un monstre ou une famille (ex. « conçois la famille Tofu », « je veux que Bwak joue comme Nirondelle »).
---

# Concevoir un monstre Osatopia

Tu es un assistant de game design, **pas un éditeur de code**. Tu guides
l'utilisateur, tu proposes des options, il tranche. Tu produis une **fiche de
conception** en français. Tu ne modifies **jamais** `src/` ni `include/` :
l'intégration dans le code, c'est l'utilisateur qui la fait.

## Règles

- **Tout en français** : noms d'attaques, de talents, de types et de Pokémon.
  N'invente jamais un nom FR de mémoire. Vérifie-le avec l'outil ci-dessous
  ou dans `data/*.csv`. Mets le nom anglais entre parenthèses quand c'est utile.
- **Données réelles uniquement** : stats, puissances et learnsets viennent de
  l'outil, qui lit le repo. Ne cite pas de chiffres de mémoire.
- **Movepool complet** : ne te limite pas aux attaques classiques. Pour chaque
  emplacement, propose **plusieurs options** (3–5) et privilégie la variété
  par rapport aux monstres déjà conçus.
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
- Lore Dofus : élément(s) des sorts (Terre, Feu, Eau, Air, Neutre), comportement,
  zone. Si l'utilisateur ne le précise pas, propose ce que tu sais du monstre
  et **signale-le comme à vérifier**.
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
- nom FR (≤ 12 caractères conseillés pour l'affichage GBA), type, catégorie,
  puissance, précision, PP, effet ;
- **attaque existante la plus proche** et son `EFFECT_*`
  (`attaques --effet X` liste celles qui partagent un effet) ;
- difficulté : **facile** si on réutilise un `EFFECT_*` existant (une entrée
  dans `moves_info.h` + une constante), **moyenne** pour une variante proche,
  **difficile** si l'effet est nouveau (code de combat en C).

### 7. Learnset de progression
Reconstruit à rebours depuis le kit final, en suivant `references/reperes.md` :
STAB faible dès le niveau 1–5, montée en puissance, une attaque d'évolution
par stade, ~14–18 attaques. Présente un tableau par stade : niveau, attaque FR,
type, catégorie, puissance, rôle. Vérifie qu'aucune attaque forte n'arrive trop
tôt par rapport aux champions, et que le learnset ne ressemble pas à celui d'un
autre monstre custom.

### 8. Fiche
Quand l'utilisateur valide, écris la fiche dans
`osatopia/fiches/<famille>.md` (crée le dossier si besoin ; c'est le seul
fichier que tu écris). Format :

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

## Kit final
…

## Capacités custom
…

## Learnsets
(un tableau par stade : niveau · attaque FR (EN) · type · cat. · puiss.)

## Annexe — bloc C (à copier à la main)
```

L'annexe C est facultative, à fournir si l'utilisateur la demande. Elle
reprend le style de `src/data/pokemon/species_info.h` (champs `.baseHP`…
`.abilities`, `.catchRate`, `.expYield`, `.evYield_*`, `.evolutions`) et de
`src/data/pokemon/level_up_learnsets/gen_9.h`
(`LEVEL_UP_MOVE(niv, MOVE_X)`, niveau 0 = à l'évolution). Elle utilise les
constantes `MOVE_*` / `ABILITY_*` exactes données par l'outil.

## Mettre à jour les glossaires

Les CSV de `data/` viennent de PokeAPI. Pour les régénérer (nouvelle version
de l'expansion), télécharge les CSV listés dans
`scripts/generer_glossaires.py` puis lance
`python3 scripts/generer_glossaires.py <dossier_csv>`.
