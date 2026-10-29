# Famille Champchamp

> Petit champignon des zones de bas niveau (forêt et champs d'Astrub et
> d'Amakna) qui se soigne et se renforce ; le Champ à Gnon est sa forme
> massive qui distribue des gnons au corps à corps. *(Lore de mémoire, à
> vérifier : sorts surtout Terre.)*
> Évolutions : Champchamp → Champagnon (niv. 22).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

Croissance `GROWTH_MEDIUM_FAST`, comme les dernières familles ajustées.

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP` ; groupe d'œuf `EGG_GROUP_GRASS`,
couleur `BODY_COLOR_BROWN` (inchangée).

## Intention

Archétype : **statut / stall**, avec une pointe de **tank offensif**.
Champagnon endort, paralyse et empoisonne, puis use l'adversaire en se
soignant. Sa particularité : il se soigne en frappant avec ses poings
(Vampi-Poing), là où Gaulet passe par Giga-Sangsue.

Référence : **Gaulet** (Amoonguss, Plante/Poison, 464), même profil (beaucoup
de PV, très lent), mais orienté physique : Att 95 contre 85, AtqSpé 65 contre
85.

Champchamp n'a pas de mains : aucun coup de poing avant l'évolution.
**Vampi-Poing arrive à l'évolution** et marque le passage à Champagnon.

Se distingue de la Bloqueuse (Plante/Psy, support spécial défensif) et du
Cdg Bouftou (même total, mur physique rapide sans AtqSpé). Évite Giga-Sangsue
et Vampigraine par niveau, déjà très présents chez les monstres Plante custom.

## Stades

| | Champchamp | Champagnon |
|---|---|---|
| Types | Plante / Poison | Plante / Poison |
| PV | 65 | 110 |
| Attaque | 55 | 95 |
| Défense | 50 | 75 |
| Atq. Spé | 45 | 65 |
| Déf. Spé | 50 | 75 |
| Vitesse | 20 | 35 |
| **Total** | **285** | **455** |
| Évolution | niv. 22 | – |
| Capture / Exp. | 190 / 59 | 75 / 165 |
| EV | PV +1 | PV +2 |

Stats sacrifiées : la Vitesse (il frappe en second, c'est un style d'usure)
et l'AtqSpé (Giga-Sangsue ne reste qu'en CT, pour se soigner).

Comparaisons (outil `similaires`) :
- Champchamp : Trompignon (294), Rongourmand (275).
- Champagnon : Gaulet (464), Rongrigou (460) ; côté Osatopia, Cdg Bouftou
  (455) et Tourneroi (459), profils différents.

## Talents

| Emplacement | Champchamp | Champagnon |
|---|---|---|
| 1 | Pose Spore (Effect Spore) | Pose Spore (Effect Spore) |
| 2 | Toxitouche (Poison Touch) | Toxitouche (Poison Touch) |
| Caché | Poing de Fer (Iron Fist) | Poing de Fer (Iron Fist) |

- Pose Spore : le talent de Gaulet, punit les attaques directes.
- Toxitouche : empoisonne au contact, se combine avec les poings.
- Poing de Fer : le « Gnon ». Inutile chez Champchamp (pas de poings), utile
  après l'évolution.
- Écarté : Régé-Force, peu utile en aventure.

## Kit final (Champagnon, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| Signature | Vampi-Poing (Drain Punch) | Combat | Phys. | 75 | Rend 50 % des dégâts |
| STAB Plante | Canon Graine (Seed Bomb) | Plante | Phys. | 80 | Inédit chez les custom |
| Contrôle | Spore | Plante | Statut | – | Sommeil garanti |
| Utilitaire | Blockhaus (Baneful Bunker) | Poison | Statut | prio +4 | Protège et empoisonne au contact |

Alternatives dans le learnset ou en CT : Toxik, Gonflette, Marto-Poing,
Mégafouet, Para-Spore, Synthèse, Giga-Sangsue, Bombe Beurk, poings
élémentaires.

## Capacités custom

Aucune.

## Learnsets

### Champchamp

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Balle Graine (Bullet Seed) | Plante | Phys. | 25 |
| 1 | Purédpois (Smog) | Poison | Spé. | 30 |
| 5 | Poudre Toxik (Poison Powder) | Poison | Statut | – |
| 8 | Toupie Éclat (Mortal Spin) | Poison | Phys. | 30 |
| 12 | Para-Spore (Stun Spore) | Plante | Statut | – |
| 15 | Synthèse (Synthesis) | Plante | Statut | – |
| 18 | Écrasement (Stomp) | Normal | Phys. | 65 |
| 26 | Canon Graine (Seed Bomb) | Plante | Phys. | 80 |
| 30 | Toxik (Toxic) | Poison | Statut | – |
| 35 | Spore Coton (Cotton Spore) | Plante | Statut | – |
| 40 | Racines (Ingrain) | Plante | Statut | – |

### Champagnon

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Vampi-Poing (Drain Punch) | Combat | Phys. | 75 |
| 1 | Balle Graine (Bullet Seed) | Plante | Phys. | 25 |
| 1 | Purédpois (Smog) | Poison | Spé. | 30 |
| 5 | Poudre Toxik (Poison Powder) | Poison | Statut | – |
| 8 | Toupie Éclat (Mortal Spin) | Poison | Phys. | 30 |
| 12 | Para-Spore (Stun Spore) | Plante | Statut | – |
| 15 | Synthèse (Synthesis) | Plante | Statut | – |
| 18 | Écrasement (Stomp) | Normal | Phys. | 65 |
| 26 | Canon Graine (Seed Bomb) | Plante | Phys. | 80 |
| 30 | Toxik (Toxic) | Poison | Statut | – |
| 34 | Blockhaus (Baneful Bunker) | Poison | Statut | – |
| 38 | Gonflette (Bulk Up) | Combat | Statut | – |
| 42 | Marto-Poing (Hammer Arm) | Combat | Phys. | 100 |
| 46 | Spore | Plante | Statut | – |
| 50 | Mégafouet (Power Whip) | Plante | Phys. | 120 |

Vampi-Poing (75) au niveau 22, juste avant Voltère ; rien à 90+ avant le
niveau 42. Spore gardé après Juan. Recoupements avec les custom limités à
Para-Spore (Bloqueuse) et Toxik (Minoskito, Shin Larve).

## CT, CS et tuteurs

| | Champchamp | Champagnon |
|---|---|---|
| Toxik, Abri, Repos, Façade, Attraction, Reflet (CT) | ✅ | ✅ |
| Ténacité, Blabla Dodo, Ronflement, Vantardise (tuteurs) | ✅ | ✅ |
| Balle Graine, Giga-Sangsue, Lance-Soleil, Zénith (CT) | ✅ | ✅ |
| Bombe Beurk (CT) : STAB Poison spécial | ✅ | ✅ |
| Coud'Boue (tuteur) : clin d'œil aux sorts Terre | ✅ | ✅ |
| Roulade, Boul'Armure (tuteurs) : il roule sur son chapeau | ✅ | ✅ |
| Explosion (tuteur) : il éclate en spores | ✅ | ✅ |
| Tunnel (CT) : le mycélium | ✅ | ✅ |
| Plaquage (tuteur), Force (CS) | – | ✅ |
| Éclate-Roc (CS), Casse-Brique, Gonflette, Mitra-Poing (CT) | – | ✅ |
| Poing Feu, Poing Glace, Poing Éclair, Dynamo-Poing, Ultimapoing (tuteurs) | – | ✅ |

Exclus volontairement :
- tous les coups de poing (dont Éclate-Roc) chez Champchamp : pas de mains ;
- Coupe, Danse Lames, Taillade : ni lame ni griffe ;
- Ultralaser : hors du style stall ;
- Séisme : Tunnel reste sa seule attaque Sol physique ;
- inutilisables : Flash, Saisie, Retour, Frustration, Puissance Cachée,
  Force Cachée.
