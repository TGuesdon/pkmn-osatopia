# Famille Pousse

> Plantes des champs d'Astrub (niv. 10–20). La Gardienne Champêtre vole la
> vie (*Désherbant*, Feu) et dope ses alliés (*Engrais*). Le Tournesol
> Sauvage frappe avec *Racine Pivotante* (Terre). Le Tournesol Affamé, boss
> de la Grange, dévore ses cibles (*Goinfrage* : vol de vie et bonus de
> dégâts), se soigne (*Soin Feuillu*) et invoque des Gardiennes.
> Évolutions : Pousse → Tournesovage (niv. 14) → Tourneroi (niv. 30).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Refonte d'une première version : stats légèrement relevées (220/357/459),
learnset presque copié sur Héliatronc (Racines, Soucigraine, Effort,
Damoclès, Tempête Verte), Ventouse au premier stade, pas de CT. Niveaux
d'évolution, croissance (moyenne-rapide), groupe d'œuf (Plante), couleur
(vert), sexe 50 % et cycles d'œuf (15) sont conservés.

## Intention

Archétype : **profiteur du soleil** + **attaquant mixte qui draine**. Monstre
de début de jeu, Plante pur aux trois stades. Sous le soleil, Chlorophylle
double sa Vitesse et Croissance lui donne +2 en Attaque et en AtqSpé.
Goinfrage se retrouve dans Encornebois et Giga-Sangsue, la faim dans
Morsure puis Mâchouille.

Références : **Héliatronc** (tournesol, Chlorophylle / Force Soleil,
Lance-Soleil), **Tengalice** (Plante mixte et rapide avec Chlorophylle).

Il se démarque des autres Plante custom : plus mixte et plus rapide
qu'Abrakleur ou Grokoko, plus offensif que Bulbisauge ; il partage avec
Bourgeon seulement le socle de drain (Vole-Vie, Méga-Sangsue, Vampigraine,
Giga-Sangsue, Synthèse).

## Stades

| | Pousse | Tournesovage | Tourneroi |
|---|---|---|---|
| Types | Plante | Plante | Plante |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 48 / 38 / 34 / 46 / 36 / 43 | 70 / 72 / 52 / 70 / 54 / 62 | 82 / 100 / 68 / 88 / 65 / 75 |
| Total | 245 | 380 | 478 |
| Talents | Chlorophylle / Engrais / *Feuille Garde* | Chlorophylle / Force Soleil / *Feuille Garde* | Chlorophylle / Force Soleil / *Feuille Garde* |
| Capture / Exp. | 235 / 56 | 120 / 130 | 45 / 221 |
| EV | 1 AtqSpé | 1 Att, 1 AtqSpé | 2 Att, 1 AtqSpé |

Défenses sacrifiées : il doit frapper vite sous le soleil, pas encaisser.

## Kit final

| Emplacement | Choix | Alternatives |
|---|---|---|
| STAB physique | Lame Feuille (Plante, Phys., 90) | Encornebois (75, draine), Lame Solaire (125), Tempête Florale (90) |
| STAB spécial | Giga-Sangsue (Plante, Spé., 75, draine) | Lance-Soleil (120), Danse Fleurs (120, Tournesovage) |
| Boost | Croissance (+1/+1, +2/+2 au soleil) | Zénith, Danse Lames (tuteur), Synthèse |
| Couverture | Mâchouille (Ténèbres, Phys., 80) | Larcin (CT), Bombe Beurk (CT) |

Talents : Chlorophylle (Vitesse ×2 au soleil), Engrais au premier stade
(nom du sort de la Gardienne) puis Force Soleil, talent caché Feuille Garde
(immunité aux statuts au soleil).

## Capacités custom

Aucune.

## Learnsets

Tronc commun aux trois stades jusqu'au niveau 28.

### Pousse

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Vole-Vie (Absorb) | Plante | Spé. | 20 |
| 1 | Croissance (Growth) | Normal | Statut | – |
| 4 | Feuillage (Leafage) | Plante | Phys. | 40 |
| 7 | Balle Graine (Bullet Seed) | Plante | Phys. | 25 |
| 10 | Méga-Sangsue (Mega Drain) | Plante | Spé. | 40 |
| 13 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 16 | Désherbaffe (Trailblaze) | Plante | Phys. | 50 |
| 19 | Vampigraine (Leech Seed) | Plante | Statut | – |
| 22 | Giga-Sangsue (Giga Drain) | Plante | Spé. | 75 |
| 25 | Synthèse (Synthesis) | Plante | Statut | – |
| 28 | Encornebois (Horn Leech) | Plante | Phys. | 75 |
| 32 | Zénith (Sunny Day) | Feu | Statut | – |
| 36 | Canon Graine (Seed Bomb) | Plante | Phys. | 80 |

### Tournesovage

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Tranch'Herbe (Razor Leaf) | Plante | Phys. | 55 |
| 1–28 | tronc commun | | | |
| 31 | Zénith (Sunny Day) | Feu | Statut | – |
| 34 | Lame Feuille (Leaf Blade) | Plante | Phys. | 90 |
| 38 | Lance-Soleil (Solar Beam) | Plante | Spé. | 120 |
| 43 | Danse Fleurs (Petal Dance) | Plante | Spé. | 120 |

Lame Feuille à 34 (37 chez Tourneroi) et Danse Fleurs (exclusive)
récompensent qui retarde l'évolution.

### Tourneroi

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Mâchouille (Crunch) | Ténèbres | Phys. | 80 |
| 1–28 | tronc commun | | | |
| 33 | Zénith (Sunny Day) | Feu | Statut | – |
| 37 | Lame Feuille (Leaf Blade) | Plante | Phys. | 90 |
| 41 | Lance-Soleil (Solar Beam) | Plante | Spé. | 120 |
| 46 | Tempête Florale (Petal Blizzard) | Plante | Phys. | 90 |
| 52 | Lame Solaire (Solar Blade) | Plante | Phys. | 125 |

## CT, CS et tuteurs

| Attaque | Pousse | Tournesovage | Tourneroi |
|---|---|---|---|
| Toxik, Abri, Zénith, Giga-Sangsue, Lance-Soleil, Balle Graine, Façade, Repos, Attraction, Reflet, Larcin (CT) | ✓ | ✓ | ✓ |
| Coupe (CS) | ✓ | ✓ | ✓ |
| Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✓ | ✓ | ✓ |
| Bombe Beurk, Rune Protect (CT) | | ✓ | ✓ |
| Danse Lames, Damoclès (tuteurs) | | ✓ | ✓ |
| Ultralaser (CT) | | | ✓ |

Exclusions volontaires : Lance-Flammes, Déflagration, Surchauffe (pas de
couverture Feu, choix de conception) ; Séisme, Tunnel ; aucun coup de poing
(pas de bras).
