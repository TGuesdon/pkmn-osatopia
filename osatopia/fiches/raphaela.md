# Famille Raphaela

> Tortue ninja bleue (lore et élément des sorts Dofus **à vérifier**),
> inspirée de Raphaël. — Évolutions : Raphaela → Tortue Bleue (niv. 28).
> Constantes : `SPECIES_RAPHAELA`, `SPECIES_TORTUE_BLEU`.

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Compilation OK.

## Intention

Archétype : **attaquant physique rapide** (principal) + **attaquant à
priorité** (secondaire). Références : Colossinge (profil de stats),
Capidextre (sweeper physique), Grenn (même typage Eau/Combat, mais
bruiser lent).

Pourquoi : Eau/Combat dès le premier stade, un ninja qui frappe fort et vite,
fragile en comparaison de Grenn (30 PV de moins, mais +15 Att et +25 Vit).
Les talents Glissade (pluie) et Chanceux (critiques) donnent deux styles de jeu ;
Technicien, en talent caché, valorise les petites attaques prioritaires
(Mach Punch, Aqua-Jet, Poing Karaté, Poing Sonique).

## Stades

| | Raphaela | Tortue Bleue |
|---|---|---|
| Types | Eau / Combat | Eau / Combat |
| PV | 50 | 75 |
| Att | 65 | 115 |
| Déf | 50 | 80 |
| AtqSpé | 35 | 45 |
| DéfSpé | 45 | 65 |
| Vit | 65 | 100 |
| Total | 310 | 480 |
| Talents | Glissade / Chanceux / (caché) Technicien | idem |
| Capture / Exp. | 120 / 70 | 45 / 190 |
| EV | 1 Att | 2 Att + 1 Vit |
| Évolution | niv. 28 | – |

Autres valeurs (faute d'indication, reprises de Lapino/Grenn) : 50 % femelle,
15 cycles d'œuf, croissance Medium Slow, amitié standard, groupes d'œuf
Eau 1 + Humanoïde, bodyColor bleu.

## Kit final

| Rôle | Attaque |
|---|---|
| STAB Eau | Tranch'Aqua (Aqua Cutter), 70, critique élevé |
| STAB Combat fort | Coup Croix (Cross Chop), 100, critique élevé |
| Priorité | Poing Sonique (Jet Punch), 60, prio +1 |
| Boost | Danse Lames (Swords Dance) |

## Capacités custom

Aucune.

## Learnsets

**Raphaela (niv. 1–27)**

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Mach Punch | Combat | Physique | 40, prio +1 |
| 1 | Rugissement (Growl) | Normal | Statut | – |
| 4 | Aqua-Jet | Eau | Physique | 40, prio +1 |
| 8 | Poing Karaté (Karate Chop) | Combat | Physique | 50 |
| 12 | Puissance (Focus Energy) | Normal | Statut | – |
| 16 | Poing Sonique (Jet Punch) | Eau | Physique | 60, prio +1 |
| 20 | Tranch'Aqua (Aqua Cutter) | Eau | Physique | 70 |
| 24 | Détection (Detect) | Combat | Statut | – |
| 27 | Casse-Brique (Brick Break) | Combat | Physique | 75 |

**Tortue Bleue (évolution niv. 28)**

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Danse Lames (Swords Dance) | Normal | Statut | – |
| 34 | Coup Croix (Cross Chop) | Combat | Physique | 100 |
| 38 | Danse Pluie (Rain Dance) | Eau | Statut | – |
| 42 | Cascade (Waterfall) | Eau | Physique | 80 |
| 46 | Gonflette (Bulk Up) | Combat | Statut | – |

Temporisation : Coup Croix arrive 6 niveaux après l'évolution
(`P_PRE_EVO_MOVES` à `FALSE`). Aucune attaque de 90+ avant le niveau 34.

## CT, CS et tuteurs

| Attaque | Source | Raphaela | Tortue Bleue |
|---|---|---|---|
| Toxik | CT | ✔ | ✔ |
| Abri | CT | ✔ | ✔ |
| Repos | CT | ✔ | ✔ |
| Provoc | CT | ✔ | ✔ |
| Façade | CT | ✔ | ✔ |
| Reflet (Double Team) | CT | ✔ | ✔ |
| Vibraqua | CT | ✔ | ✔ |
| Aéropique | CT | ✔ | ✔ |
| Larcin | CT | ✔ | ✔ |
| Séisme | CT | ✗ | ✔ |
| Blabla Dodo | Tuteur | ✔ | ✔ |
| Ténacité | Tuteur | ✔ | ✔ |
| Poing Glace | Tuteur | ✗ | ✔ |
| Poing Éclair | Tuteur | ✗ | ✔ |
| Plongée | CS | ✔ | ✔ |
| Cascade | CS | ✔ | ✔ |
| Surf | CS | ✔ | ✔ |
| Éclate-Roc | CS | ✔ | ✔ |
| Coupe | CS | ✔ | ✔ |
| Force | CS | ✔ | ✔ |

Exclusions volontaires : Queue de Fer (pas de queue), Dynamo-Poing (doublon
avec Coup Croix), Danse Lames en tuteur (déjà par niveau), Poing Feu, Damoclès,
Ultimawashi, Ball'Ombre, Tomberoche. Cascade est bien une CS (logique), son
entrée au niveau 42 est conservée.
