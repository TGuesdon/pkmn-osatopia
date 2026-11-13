# Éditeur de répartition des Pokémon

Interface web locale pour placer les Pokémon dans le jeu : rencontres sauvages
et équipes des dresseurs, lieu par lieu.

```bash
python3 dev_scripts/distribution_editor/server.py
```

La page s'ouvre sur http://localhost:8643/ (ou le port libre suivant). Le serveur
a besoin de Pillow (`pip install pillow`) pour les sprites et la carte.

## Ce que ça fait

- **Carte de Hoenn et liste des lieux** : vert = zone 100 % custom, orange = en partie custom.
- **Pokémon sauvages** : herbe, surf, Éclate-Roc et pêche, avec le taux réel de chaque
  espèce. « Remplacer » change une espèce sur tous ses emplacements à la fois.
  On peut aussi ajouter une méthode à un lieu qui n'en a pas.
- **Dresseurs** : espèce, niveau, objet tenu, attaques (vide = les 4 dernières
  apprises par niveau). Les autres champs (IVs, talent, nature…) sont conservés tels quels.
- **Vue d'ensemble** : pour chaque Pokémon custom, où on le trouve à l'état sauvage
  et quels dresseurs l'utilisent. Elle permet de repérer ceux qui ne sont placés nulle part.
- **Dresseurs sans lieu** : ceux qui ne sont appelés par aucun script de map.

## Fichiers modifiés

« Enregistrer » (ou Cmd+S) réécrit `src/data/wild_encounters.json` et
`src/data/trainers.party`. Seules les équipes modifiées sont réécrites, le reste
du fichier ne bouge pas : `git diff` montre exactement ce qui a changé.

Avant d'écrire, le serveur vérifie les espèces, les niveaux, les objets et les
attaques (noms reconnus par `trainerproc`). Il refuse aussi d'enregistrer si un
des fichiers a été modifié sur le disque depuis l'ouverture de la page.

## D'où viennent les liens dresseur → lieu

- Les `trainerbattle…` dans `data/maps/*/scripts.inc`.
- Les revanches de `gRematchTable` (`src/battle_setup.c`).
