# Famille Scarador

> Petit scarabée qui devient l'un des cinq Scarafeuilles selon le lieu où il
> grandit, puis un Scarabosse Doré qui maîtrise les éléments.
> Évolutions : El Scarador → Scarafeuille (niv. 20, selon le lieu) → Scarabosse Doré (niv. 40).

**État** : validée et intégrée

## Intention
Archétype : attaquant spécial · Pourquoi : dans Dofus, les Scarabosses
maîtrisent les éléments. Le chemin choisi (lieu de l'évolution au niveau 20)
détermine les attaques élémentaires apprises par le Scarafeuille et gardées par
le Scarabosse, qui est une espèce unique de type Insecte.

Talents de la famille : Lentiteintée (Tinted Lens), Essaim (Swarm) ;
talent caché du Scarabosse : Protéen (Protean).

Références : Pyrax (Volcarona) pour l'insecte spécial à Papillodanse,
Lucanon (Vikavolt) pour le scarabée spécial.

## Stades

| | Types | PV | Att | Déf | AtqSpé | DéfSpé | Vit | Total |
|---|---|---|---|---|---|---|---|---|
| El Scarador | Insecte | 45 | 30 | 40 | 55 | 40 | 50 | 260 |
| Scarafeuille Bleu | Insecte/Eau | 75 | 40 | 65 | 80 | 85 | 55 | 400 |
| Scarafeuille Rouge | Insecte/Feu | 60 | 45 | 55 | 100 | 65 | 75 | 400 |
| Scarafeuille Vert | Insecte/Sol | 75 | 55 | 85 | 80 | 60 | 45 | 400 |
| Scarafeuille Noir | Insecte/Ténèbres | 55 | 50 | 50 | 95 | 55 | 95 | 400 |
| Scarafeuille Blanc | Insecte/Vol | 70 | 45 | 60 | 85 | 70 | 70 | 400 |
| Scarabosse Doré | Insecte | 85 | 60 | 80 | 115 | 85 | 95 | 520 |

| | Talents | Capture | Exp. | EV | Couleur |
|---|---|---|---|---|---|
| El Scarador | Lentiteintée / Essaim | 190 | 58 | 1 AtqSpé | Brun |
| Scarafeuille Bleu | Lentiteintée / Essaim | 100 | 140 | 1 AtqSpé, 1 DéfSpé | Bleu |
| Scarafeuille Rouge | Lentiteintée / Essaim | 100 | 140 | 2 AtqSpé | Rouge |
| Scarafeuille Vert | Lentiteintée / Essaim | 100 | 140 | 1 AtqSpé, 1 Déf | Vert |
| Scarafeuille Noir | Lentiteintée / Essaim | 100 | 140 | 1 AtqSpé, 1 Vit | Noir |
| Scarafeuille Blanc | Lentiteintée / Essaim | 100 | 140 | 1 AtqSpé, 1 PV | Blanc |
| Scarabosse Doré | Lentiteintée / Essaim / Protéen (caché) | 45 | 235 | 2 AtqSpé, 1 Vit | Jaune |

Tous les stades : 50 % de femelles, 15 cycles d'œuf, bonheur standard,
croissance moyenne-lente (`GROWTH_MEDIUM_SLOW`), groupe d'œufs Insecte.

## Évolution selon le lieu (El Scarador, niveau 20)

Une condition custom, `IF_IN_EVO_ZONE`, prend une zone `EVO_ZONE_*`
(`include/constants/pokemon.h`). `GetPlayerEvoZone` (`src/pokemon.c`) décide
de la zone du joueur : d'abord les secteurs nommés, puis surf/plongée,
tempête de sable, carte souterraine.

| Scarafeuille | Types | Zone | Lieux |
|---|---|---|---|
| Bleu | Insecte/Eau | `EVO_ZONE_WATER` | en surf, carte sous-marine, Épave abandonnée, planque Aqua |
| Rouge | Insecte/Feu | `EVO_ZONE_VOLCANO` | Mont Chimnée, Chemin Ardent, Passage Escarpé, Route 112, planque Magma |
| Vert | Insecte/Sol | `EVO_ZONE_DESERT` | tempête de sable, Ruines du Désert, Passage du Désert, Tour Mirage |
| Noir | Insecte/Ténèbres | `EVO_ZONE_CAVE` | toute autre carte souterraine (grottes, New Lavandia, Nombril Rocheux…) |
| Blanc | Insecte/Vol | aucune | partout ailleurs (branche par défaut, en dernier) |

Une seule entrée par Scarafeuille : le Pokédex HGSS n'affiche que 10
évolutions par famille (`targetSpecies[10]`), soit ici 5 Scarafeuilles + 5
Scarabosse.

## Kit final (Scarabosse Doré)

| Emplacement | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Boost | Papillodanse (Quiver Dance) | Insecte | Statut | — |
| STAB | Bourdon (Bug Buzz) | Insecte | Spéciale | 90 |
| Attaque du chemin | selon le Scarafeuille (voir learnsets) | — | Spéciale | 75–90 |
| Couverture Feu/Vol | Rayon Gemme (Power Gem) | Roche | Spéciale | 80 |

Talents : Lentiteintée (Tinted Lens) / Essaim (Swarm) ; caché : Protéen (Protean).

## Learnsets

### Tronc commun (tous les stades, mêmes niveaux)

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Sécrétion (String Shot) | Insecte | Statut | — |
| 4 | Harcèlement (Infestation) | Insecte | Spé. | 20 |
| 8 | Armure (Harden) | Normal | Statut | — |
| 11 | Survinsecte (Struggle Bug) | Insecte | Spé. | 50 |
| 15 | Pouvoir Antique (Ancient Power) | Roche | Spé. | 60 |
| 24 | Vent Argenté (Silver Wind) | Insecte | Spé. | 60 |
| 30 | Rayon Signal (Signal Beam) | Insecte | Spé. | 75 |
| 34 | Appel Défense (Defend Order) | Insecte | Statut | — |

El Scarador apprend le tronc commun jusqu'au niveau 15 (6 attaques).

### Scarafeuilles (tronc commun + attaques de chemin)

| Chemin | Évo | 27 | 38 |
|---|---|---|---|
| Bleu | Bulles d'O (Bubble Beam) · Eau · Spé. 65 | Anneau Hydro (Aqua Ring) · Eau · Statut | Ocroupi (Muddy Water) · Eau · Spé. 90 |
| Rouge | Calcination (Incinerate) · Feu · Spé. 60 | Feu Follet (Will-O-Wisp) · Feu · Statut | Danse du Feu (Fiery Dance) · Feu · Spé. 80 |
| Vert | Boue-Bombe (Mud Bomb) · Sol · Spé. 65 | Amass'Sable (Shore Up) · Sol · Statut | Telluriforce (Earth Power) · Sol · Spé. 90 |
| Noir | Aboiement (Snarl) · Ténèbres · Spé. 55 | Croco Larme (Fake Tears) · Ténèbres · Statut | Vibrobscur (Dark Pulse) · Ténèbres · Spé. 80 |
| Blanc | Tranch'Air (Air Cutter) · Vol · Spé. 60 | Vent Arrière (Tailwind) · Vol · Statut | Lame d'Air (Air Slash) · Vol · Spé. 75 |

### Scarabosse Doré (tronc commun + exclusives)

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Papillodanse (Quiver Dance) | Insecte | Statut | — |
| 44 | Bourdon (Bug Buzz) | Insecte | Spé. | 90 |
| 48 | Rayon Gemme (Power Gem) | Roche | Spé. | 80 |
| 53 | Appel Soins (Heal Order) | Insecte | Statut | — |

Les attaques de chemin ne sont pas des CT et le Scarabosse ne les réapprend
pas (`P_PRE_EVO_MOVES` à `FALSE`) : elles sont l'empreinte du chemin.

## CT, CS et tuteurs

Règle : une CT d'attaque d'un élément de chemin n'est donnée qu'au Scarafeuille
de ce chemin, jamais au Scarabosse (elle fait partie de l'empreinte).

Sc = El Scarador · Bl/Ro/Ve/No/Bc = Scarafeuilles · Boss = Scarabosse Doré.

| Attaques | Sc | Bl | Ro | Ve | No | Bc | Boss |
|---|---|---|---|---|---|---|---|
| Abri, Repos, Attraction, Reflet, Façade, Toxik (CT) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Roulade, Boul'Armure (tuteurs) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ténacité, Vantardise, Blabla Dodo, Ronflement, Taillade, Météores (tuteurs) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Mur Lumière, Protection, Rune Protect, Échange (CT) | – | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Giga-Sangsue, Ball'Ombre, Onde de Choc (CT), Vent Glace (tuteur) | – | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ultralaser (CT) | – | – | – | – | – | – | ✅ |
| Vibraqua, Danse Pluie (CT), Surf, Plongée (CS) | – | ✅ | – | – | – | – | – |
| Lance-Flammes, Déflagration, Zénith (CT) | – | – | ✅ | – | – | – | – |
| Tempête de Sable, Tunnel, Séisme (CT), Coud'Boue (tuteur) | – | – | – | ✅ | – | – | – |
| Provoc, Tourmente, Larcin (CT) | – | – | – | – | ✅ | – | – |
| Aéropique (CT), Vol (CS) | – | – | – | – | – | ✅ | – |
| Danse Pluie, Zénith, Tempête de Sable (CT) | – | – | – | – | – | – | ✅ |

Exclus volontairement :
- Psyko, Laser Glace, Blizzard, Tonnerre, Fatal-Foudre, Lance-Soleil, Bombe
  Beurk : couvertures à 90+ qui éclipseraient l'attaque de chemin ;
- Plénitude, Danse Lames : doublon avec Papillodanse ;
- coups de poing, Force, Coupe, Éclate-Roc, Casse-Brique, Éboulement,
  Tomberoche, Queue de Fer, Ailes d'Acier, Gonflette, Cascade : physiques ;
- Cage Éclair, Métronome, Mitra-Poing, Ultimawashi, Damoclès, Bélier,
  Dévorêve, Boost : hors profil ;
- inutilisables : Retour, Frustration, Puissance Cachée, Force Cachée, Saisie,
  Flash.
