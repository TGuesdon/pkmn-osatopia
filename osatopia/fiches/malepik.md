# Famille Malepik

> Esprits maléfiques de la forêt (race Malters), qui se dédoublent et passent
> invisibles. Dans le Dofus actuel (niv. 142–150, Dédale du Dark Vlad et
> Tertre du long sommeil), Malepik harcèle avec *Malagile* (taux de critique),
> *Maltitude* (vol de Force) et *Malibi* (Pesanteur) ; Maltrio gêne avec
> *Malenpoint* (insoignable), *Malteration* (−PA) et *Malèze* (−PM). Le
> dédoublement et l'invisibilité viennent de la version de l'utilisateur
> (absents des sorts actuels). — Évolutions : Malepik → Maltrio (niveau 30).

**État** : validée et intégrée.

## Intention
Archétype : perturbateur rapide + attaquant à boost (secondaire) ·
Références : Desséliande (l'esprit-arbre Spectre/Plante), Gourgeist (Spectre/Plante),
Polichombr (repère de spectre de base) ·
Pourquoi : premier Spectre/Plante d'Osatopia (Ténèbres/Plante existe déjà avec
Pampactus). Il disparaît (Hantise), se cache derrière son double (Clonage,
Reflet, Illusion) et vole la force de l'adversaire (Vole-Force, Clepto-Mânes).

## Stades
| | Malepik | Maltrio |
|---|---|---|
| Constante | `SPECIES_MALEPIK` | `SPECIES_MALTRIO` |
| Types | Spectre/Plante | Spectre/Plante |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 50 / 60 / 42 / 40 / 50 / 65 | 75 / 92 / 65 / 60 / 85 / 105 |
| Total | 307 | 482 |
| Talents | Illusion / Chanceux / caché Poing Invisible | idem |
| Capture / Exp. | 190 / 63 | 75 / 172 |
| EV | Vit +1 | Vit +2 |

Stats sacrifiées : AtqSpé (tout le kit est physique) et Déf (l'immunité
Normal/Combat couvre déjà une partie des coups physiques). Se distingue de
Sarkapwane (70/100/60/60/70/105) et Kwak Vent par une Attaque plus basse et une
DéfSpé plus haute : il use plutôt qu'il ne frappe.

Talents choisis pour leur rareté chez les monstres custom (Corps Maudit ×12 et
Infiltration ×7 écartés) : Illusion pour le dédoublement, Chanceux pour les
critiques de Malagile, Poing Invisible pour l'invisibilité.

Autres champs (valeurs Bitouf) : 50 % femelle, 15 cycles d'œuf,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`. Groupes d'œuf Amorphe + Plante,
couleur marron (à vérifier sur les sprites).

## Kit final
| Rôle | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| STAB Spectre, invisibilité | Hantise (Phantom Force) | Spectre | Phys. | 90 |
| STAB Plante | Lame Feuille (Leaf Blade) | Plante | Phys. | 90 |
| Dédoublement | Clonage (Substitute) | Normal | Statut | – |
| Vol de force | Vole-Force (Strength Sap) | Plante | Statut | – |

Alternatives : Griffe Ombre, Clepto-Mânes, Feu Follet, Danse Lames, Provoc (CT),
Éboulement (tuteur).

## Capacités custom
Aucune.

## Learnsets

### Malepik
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Tapotige (Branch Poke) | Plante | Phys. | 40 |
| 1 | Reflet (Double Team) | Normal | Statut | – |
| 4 | Léchouille (Lick) | Spectre | Phys. | 30 |
| 8 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 12 | Ombre Portée (Shadow Sneak) | Spectre | Phys. | 40 (prio) |
| 16 | Tranch'Herbe (Razor Leaf) | Plante | Phys. | 55 |
| 19 | Maléfice Sylvain (Forest's Curse) | Plante | Statut | – |
| 22 | Griffe Ombre (Shadow Claw) | Spectre | Phys. | 70 |
| 25 | Feu Follet (Will-O-Wisp) | Feu | Statut | – |
| 28 | Canon Graine (Seed Bomb) | Plante | Phys. | 80 |
| 31 | Clonage (Substitute) | Normal | Statut | – |
| 35 | Vole-Force (Strength Sap) | Plante | Statut | – |
| 39 | Hantise (Phantom Force) | Spectre | Phys. | 90 |

### Maltrio
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Hantise (Phantom Force) | Spectre | Phys. | 90 |
| 1–35 | mêmes attaques que Malepik (Tapotige → Vole-Force) | | | |
| 39 | Lame Feuille (Leaf Blade) | Plante | Phys. | 90 |
| 43 | Clepto-Mânes (Spectral Thief) | Spectre | Phys. | 90 |
| 47 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 52 | Mégafouet (Power Whip) | Plante | Phys. | 120 |

## CT, CS et tuteurs
| Attaque | Malepik | Maltrio |
|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Larcin, Reflet | ✅ | ✅ |
| Provoc, Tourmente, Zénith | ✅ | ✅ |
| Ball'Ombre, Giga-Sangsue, Lance-Soleil, Balle Graine | ✅ | ✅ |
| Tomberoche, Aéropique, Coupe (CS) | ✅ | ✅ |
| Ultralaser | ❌ | ✅ |
| Tuteurs : Éboulement, Dévorêve, Ténacité, Blabla Dodo, Ronflement, Vantardise, Boost, Taillade | ✅ | ✅ |

Exclusions volontaires : Danse Lames en tuteur (casserait l'apprentissage au
niveau 47), Séisme et Tunnel (un esprit ne creuse pas), Casse-Brique,
Éclate-Roc et coups de poing (pas un combattant), CT offensives Eau, Glace,
Électrik, Psy et Feu (hors thème), Flash (inutilisable).
