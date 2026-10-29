# Famille Wabbit

> Lapins de l'île des Wabbits, gouvernés par le Wa Wabbit, qui cultivent et
> vénèrent la **cawotte** (orthographe Dofus, à respecter dans tous les textes
> du jeu). Sorts Neutre et Terre.
> Évolutions : Tiwabbit → Wabbit (niv. 20) → Wo Wabbit (niv. 38).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`, code de combat). Une capacité custom (Potager) et un
talent custom (Terrier).

Zone : **Tunnel Mérazon**, à la place de Chuchmur (rencontres niv. 5–8).

Valeurs non choisies, reprises de la famille Bitouf : `PERCENT_FEMALE(50)`,
`.eggCycles = 15`, `STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW` (comme
Chuchmur) ; groupe d'œuf `EGG_GROUP_FIELD`, couleur `BODY_COLOR_WHITE` (à
ajuster selon le sprite).

Constantes : `SPECIES_TIWABBIT`, `SPECIES_WABBIT`, `SPECIES_WO_WABBIT`.
Nom affiché à corriger à l'intégration : « Tiwabit » → « Tiwabbit ».

## Intention

Archétype : **soutien / perturbateur**, sur une base de **mur**. Le Wo Wabbit
ne cherche pas à frapper : il entre, plante son Potager pour soigner les
alliés qui le suivent, endort ou gêne l'adversaire (Bâillement, Encore,
Chatouille, Barrage, Provoc) et tient grâce à Paresse.

Référence : **Écrémeuh** (Miltank, Normal, 490) pour le côté utilitaire et
le soin (Lait à Boire, Glas de Soin), en plus lent et plus résistant côté
spécial.

Se distingue du **Roi Bouftou** (Normal, 530) : même type, mais le Bouftou
est un gros sac à PV qui frappe, sans aucun utilitaire. Le Wo Wabbit a moins
d'Attaque (75 contre 87) et vit pour son équipe.

## Stades

| | Tiwabbit | Wabbit | Wo Wabbit |
|---|---|---|---|
| Types | Normal | Normal | Normal |
| PV | 60 | 90 | 110 |
| Attaque | 45 | 55 | 75 |
| Défense | 55 | 85 | 110 |
| Atq. Spé | 25 | 35 | 45 |
| Déf. Spé | 40 | 70 | 90 |
| Vitesse | 30 | 45 | 70 |
| **Total** | **255** | **380** | **500** |
| Évolution | niv. 20 | niv. 38 | – |
| Talents | Ramassage / Terrier / *Isograisse* | idem | idem |
| Capture / Exp. | 190 / 58 | 100 / 140 | 45 / 220 |
| EV | PV +1 | PV +1, Déf +1 | PV +2, Déf +1 |

Stats sacrifiées : l'AtqSpé (tank physique Normal) et l'Attaque (il soutient
plus qu'il ne frappe). Vitesse moyenne-basse plutôt que très basse : il n'est
pas fait pour Distorsion.

Comparaisons (outil `similaires`) :
- Tiwabbit : Keunotor (250), Gourmelet (254) ; remplace Chuchmur (240).
- Wabbit : Excelangue (385) ; côté Osatopia, Gwotofu (370), dont il s'écarte
  par moins d'Attaque et plus de PV / DéfSpé.
- Wo Wabbit : Écrémeuh (490), Roi Bouftou (530).

## Talents

| Emplacement | Talent | Note |
|---|---|---|
| 1 | Ramassage (Pickup) | Ramasse des objets hors combat, utile en aventure. |
| 2 | **Terrier** (custom) | Voir ci-dessous. |
| Caché | Isograisse (Thick Fat) | Divise par deux les dégâts Feu et Glace. |

Écartés : Bajoues, Récolte, Régé-Force (pas de cumul de talents « carotte »),
Annule Garde (le rendrait facile à toucher).

## Kit final (Wo Wabbit, niv. 40–50)

| Emplacement | Attaque | Type | Cat. | Puiss. | Note |
|---|---|---|---|---|---|
| Signature | **Potager** (custom) | Normal | Statut | – | Soigne les alliés qui entrent |
| Soin | Paresse (Slack Off) | Normal | Statut | – | 50 % des PV max |
| Gêne | Bâillement (Yawn) | Normal | Statut | – | Touche même sous terre avec Terrier |
| Utilitaire | Croc Fatal (Super Fang) | Normal | Phys. | ½ PV | Indépendant de ses stats |

Alternatives : Encore, Chatouille, Barrage (learnset) ; Provoc, Tourmente,
Hurlement (CT) ; Par Ici, Coup d'Main en duo.

## Capacités custom

### Potager

| Champ | Valeur |
|---|---|
| Nom | Potager (7 caractères) |
| Type / Cat. | Normal · Statut |
| Puissance / Précision / PP | – / – / 20 |
| Cible | Côté du lanceur |
| Description | « Plante des cawottes qui soignent les alliés entrant au combat. » |

Effet : pose un état de terrain **du côté du lanceur**, cumulable sur 3
couches comme Picots. Chaque allié qui entre au combat récupère 1/8, 1/6 ou
1/4 de ses PV max selon le nombre de couches. Le champ reste en place.
- Comme Picots, ne profite pas aux Pokémon qui ne touchent pas le sol (type
  Vol, Lévitation, Ballon).
- Retiré par Anti-Brume et Grand Nettoyage (qui nettoient les deux côtés).
  **Pas** par Tour Rapide, qui ne nettoie que le côté du lanceur et ne doit
  pas détruire le Potager d'un allié.
- Échoue à la 4e couche.

Modèles : Picots (`EFFECT_SPIKES`) pour la pose et les couches, Vœu
(`EFFECT_WISH`) pour le soin.

Difficulté : **difficile**. Nouvel état de côté de terrain, déclencheur à
l'entrée en combat calqué sur Picots, message et animation, et un score dans
l'IA pour que les dresseurs l'utilisent.

### Terrier (talent)

Description : « Ses capacités atteignent les ennemis sous terre et leur
infligent le double de dégâts. »

Effet :
- les capacités du Pokémon (y compris de statut) touchent une cible sous
  terre (Tunnel), comme Annule Garde, mais seulement dans ce cas ;
- les capacités offensives infligent le double de dégâts à cette cible, comme
  Séisme.

Hors Tunnel, aucun effet sur la précision : contrairement à Annule Garde, le
Wo Wabbit ne devient pas plus facile à toucher.

Code : test de précision à côté d'Annule Garde (`battle_util.c`, vers
`abilityAtk == ABILITY_NO_GUARD`), doublement à côté de
`MoveDamagesUnderground`. Difficulté : **moyenne**.

## Learnsets

### Tiwabbit

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Écras'Face (Pound) | Normal | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 7 | Bluff (Fake Out) | Normal | Phys. | 40 (prio +3) |
| 10 | Bâillement (Yawn) | Normal | Statut | – |
| 13 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 16 | Paresse (Slack Off) | Normal | Statut | – |

### Wabbit

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Barrage (Block) | Normal | Statut | – |
| 1 | Écras'Face (Pound) | Normal | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 7 | Bluff (Fake Out) | Normal | Phys. | 40 (prio +3) |
| 10 | Bâillement (Yawn) | Normal | Statut | – |
| 13 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 16 | Paresse (Slack Off) | Normal | Statut | – |
| 23 | Croc Fatal (Super Fang) | Normal | Phys. | ½ PV |
| 27 | Encore | Normal | Statut | – |
| 31 | Tunnel (Dig) | Sol | Phys. | 80 |
| 35 | Chatouille (Tickle) | Normal | Statut | – |

### Wo Wabbit

| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | **Potager** (custom) | Normal | Statut | – |
| 1 | Barrage (Block) | Normal | Statut | – |
| 1 | Écras'Face (Pound) | Normal | Phys. | 40 |
| 1 | Mimi-Queue (Tail Whip) | Normal | Statut | – |
| 4 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 7 | Bluff (Fake Out) | Normal | Phys. | 40 (prio +3) |
| 10 | Bâillement (Yawn) | Normal | Statut | – |
| 13 | Morsure (Bite) | Ténèbres | Phys. | 60 |
| 16 | Paresse (Slack Off) | Normal | Statut | – |
| 23 | Croc Fatal (Super Fang) | Normal | Phys. | ½ PV |
| 27 | Encore | Normal | Statut | – |
| 31 | Tunnel (Dig) | Sol | Phys. | 80 |
| 35 | Chatouille (Tickle) | Normal | Statut | – |
| 42 | Par Ici (Follow Me) | Normal | Statut | – (prio +2) |
| 46 | Plaquage (Body Slam) | Normal | Phys. | 85 |
| 50 | Coup d'Main (Helping Hand) | Normal | Statut | – (prio +5) |

Points d'attention : Paresse au niv. 16 (tôt, à repousser si les arènes
deviennent trop faciles) ; Potager réservé au Wo Wabbit ; aucune attaque à
90+ ; Par Ici arrive pour Lévy & Tatia (niv. 42).

## CT, CS et tuteurs

| Attaque | Source | Tiwabbit | Wabbit | Wo Wabbit |
|---|---|---|---|---|
| Provoc (Taunt) | CT | ✓ | ✓ | ✓ |
| Tourmente (Torment) | CT | ✓ | ✓ | ✓ |
| Hurlement (Roar) | CT | ✓ | ✓ | ✓ |
| Toxik (Toxic) | CT | ✓ | ✓ | ✓ |
| Abri (Protect) | CT | ✓ | ✓ | ✓ |
| Repos (Rest) | CT | ✓ | ✓ | ✓ |
| Protection (Reflect) | CT | ✓ | ✓ | ✓ |
| Mur Lumière (Light Screen) | CT | ✓ | ✓ | ✓ |
| Rune Protect (Safeguard) | CT | ✓ | ✓ | ✓ |
| Attraction (Attract) | CT | ✓ | ✓ | ✓ |
| Larcin (Thief) | CT | ✓ | ✓ | ✓ |
| Façade (Facade) | CT | ✓ | ✓ | ✓ |
| Tunnel (Dig) | CT | ✓ | ✓ | ✓ |
| Zénith (Sunny Day) | CT | ✓ | ✓ | ✓ |
| Séisme (Earthquake) | CT | | | ✓ |
| Ultralaser (Hyper Beam) | CT | | | ✓ |
| Coupe (Cut) | CS | ✓ | ✓ | ✓ |
| Force (Strength) | CS | ✓ | ✓ | ✓ |
| Éclate-Roc (Rock Smash) | CS | ✓ | ✓ | ✓ |
| Coud'Boue (Mud-Slap) | Tuteur | ✓ | ✓ | ✓ |
| Ténacité (Endure) | Tuteur | ✓ | ✓ | ✓ |
| Blabla Dodo (Sleep Talk) | Tuteur | ✓ | ✓ | ✓ |
| Ronflement (Snore) | Tuteur | ✓ | ✓ | ✓ |
| Vantardise (Swagger) | Tuteur | ✓ | ✓ | ✓ |
| Frappe Atlas (Seismic Toss) | Tuteur | ✓ | ✓ | ✓ |
| Riposte (Counter) | Tuteur | ✓ | ✓ | ✓ |
| Boost (Psych Up) | Tuteur | ✓ | ✓ | ✓ |
| Métronome (Metronome) | Tuteur | ✓ | ✓ | ✓ |
| Ultimawashi (Mega Kick) | Tuteur | | | ✓ |
| Damoclès (Double-Edge) | Tuteur | | | ✓ |

Exclusions volontaires :
- **Plaquage** en tuteur : STAB principal du learnset au niv. 46.
- **Coups de poing** (Poing Feu, Poing Éclair, Poing-Glace, Ultimapoing,
  Mitra-Poing, Dynamopoing) : un lapin donne des coups de pied.
- **Attaques spéciales** (Laser Glace, Tonnerre, Lance-Flammes, Psyko,
  Ball'Ombre…) : AtqSpé sacrifiée.
- **Gonflette, Danse-Lames** : il reste un soutien.
- **Cage Éclair** : paralysie électrique hors thème (comme Regard Médusant).
- **E-Coque** : doublon de Paresse.
- **Échange** (Skill Swap) : écarté.

## Intégration (code)

- **Terrier** : `ABILITY_TERRIER` (`include/constants/abilities.h`,
  `src/data/abilities.h`). Précision dans `CanMoveSkipAccuracyCalc`, dégâts
  doublés dans `GetUndergroundModifier` (`src/battle_util.c`).
- **Potager** : `MOVE_POTAGER` / `EFFECT_POTAGER`. Compteur
  `gSideTimers[side].potagerAmount` (0–3) et drapeau
  `gDisableStructs[battler].potagerDone`. Pose via `BS_TrySetPotager`
  (macro `trysetpotager`), soin dans `DoSwitchInEffectsForBattler` juste après
  les pièges, retrait dans `DefogClearHazards` (Anti-Brume, Grand Nettoyage).
  Non échangé par Change Côté. IA : pénalisé à 3 couches ou sans remplaçant,
  bonus sinon (`battle_ai_main.c`). Animation de Racines, textes en français
  (`STRINGID_POTAGER*`).
