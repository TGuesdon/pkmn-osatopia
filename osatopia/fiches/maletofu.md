# Famille Maletofu

> Le Tofu Maléfique hante le Cimetière, ses Cryptes et la Maison Fantôme
> (niv. 32–40). Ses sorts sont tous Air : Béco Maléfique vole de la vie,
> Maléfice rend Insoignable, Punksnotdède lui fait esquiver les coups.
> Karnhell est la monture du Dark Vlad, le gardien du Dofus Émeraude :
> énorme réserve de PV, sorts Feu et Terre, soin total (Envolée sauvage),
> attraction et repousse.
> Évolutions : Maletofu → Karnhell (niv. 42).

**État : validée et intégrée** (`species_info.h`, `gen_9.h`,
`teachable_learnsets.h`). Pas de capacité custom.

## Intention

Archétype : Maletofu **perturbateur rapide** et fragile → Karnhell **tank
offensif / pivot** physique · Références : Grodrive (le Spectre/Vol de base),
Corvaillus (oiseau robuste avec Atterrissage), Sulfura (couverture Feu) ·
Pourquoi : un oiseau maléfique de fin de partie, premier Vol/Spectre
d'Osatopia, qui évolue tard (après Lévy & Tatia). Il reste distinct de la
famille Tofu : kit Spectre/Feu, Intimidation, temporisation sur Rapace.

## Stades

| | Maletofu | Karnhell |
|---|---|---|
| Types | Vol/Spectre | Vol/Spectre |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 55 / 70 / 45 / 50 / 45 / 95 | 110 / 105 / 85 / 55 / 80 / 80 |
| Total | 360 | 515 |
| Talents | Infiltration / Corps Maudit / Régé-Force (caché) | Intimidation / Corps Maudit / Régé-Force (caché) |
| Capture / Exp. | 75 / 125 | 45 / 250 |
| EV | 1 Vit | 2 PV, 1 Att |

Autres valeurs (reprises de la famille Bitouf) : 50 % femelles, 15 cycles
d'œuf, bonheur standard, croissance moyenne-lente, groupe Vol, couleur noire.

Stats sacrifiées : les défenses de Maletofu (il esquive au lieu d'encaisser),
l'AtqSpé de Karnhell (physique pur). Karnhell a un total proche de Crocoburio
et Phossile, mais plus de PV et de Vitesse, et une Attaque un cran en dessous.

## Kit final

| Emplacement | Attaque | Note |
|---|---|---|
| STAB Vol | Bec-Canon (Beak Blast, 100) | Brûle qui le frappe pendant la charge |
| STAB Spectre | Tisse Ombre (Spirit Shackle, 80) | Empêche de fuir (Attraction sauvage) |
| Soin | Atterrissage (Roost) | Envolée sauvage |
| Couverture Feu | Boutefeu (Flare Blitz, 120) / Nitrocharge (Flame Charge, 50) | Côté Feu de Karnhell |

Alternatives : Rapace, Hantise, Cyclone, Feu Follet, Séisme (CT).

## Capacités custom

Aucune. Pistes écartées : Béco Maléfik (Vol, vol de vie, `EFFECT_ABSORB`) et
Maléfice (Spectre, effet de Dissonance Psy).

## Learnsets

### Maletofu
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Picpic (Peck) | Vol | Phys | 35 |
| 1 | Étonnement (Astonish) | Spectre | Phys | 30 |
| 5 | Dépit (Spite) | Spectre | Statut | – |
| 9 | Ombre Portée (Shadow Sneak) | Spectre | Phys | 40 |
| 13 | Onde Folie (Confuse Ray) | Spectre | Statut | – |
| 17 | Cru-Ailes (Wing Attack) | Vol | Phys | 60 |
| 21 | Nitrocharge (Flame Charge) | Feu | Phys | 50 |
| 25 | Griffe Ombre (Shadow Claw) | Spectre | Phys | 70 |
| 29 | Feu Follet (Will-O-Wisp) | Feu | Statut | – |
| 33 | Bec Vrille (Drill Peck) | Vol | Phys | 80 |
| 37 | Tisse Ombre (Spirit Shackle) | Spectre | Phys | 80 |
| 41 | Lien du Destin (Destiny Bond) | Spectre | Statut | – |
| 45 | Rapace (Brave Bird) | Vol | Phys | 120 |
| 49 | Hantise (Phantom Force) | Spectre | Phys | 90 |

**Temporisation** : en annulant l'évolution au niv. 42, Maletofu apprend
Rapace (45) et Hantise (49), que Karnhell n'apprend pas.

### Karnhell
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Atterrissage (Roost) | Vol | Statut | – |
| 1–37 | (identique à Maletofu) | | | |
| 45 | Cyclone (Whirlwind) | Normal | Statut | – |
| 48 | Boutefeu (Flare Blitz) | Feu | Phys | 120 |
| 52 | Bec-Canon (Beak Blast) | Vol | Phys | 100 |

## CT, CS et tuteurs

| Attaque | Maletofu | Karnhell |
|---|---|---|
| Toxik, Abri, Repos, Blabla Dodo, Ronflement, Ténacité, Façade, Attraction, Reflet, Vantardise | ✓ | ✓ |
| Aéropique, Vol (CS), Ailes d'Acier | ✓ | ✓ |
| Ball'Ombre | ✓ | ✓ |
| Provoc, Tourmente, Larcin, Hurlement | ✓ | ✓ |
| Danse Lames (tuteur), Dévorêve (tuteur) | ✓ | ✓ |
| Zénith | ✓ | ✓ |
| Séisme | | ✓ |
| Gonflette, Ultralaser | | ✓ |

Exclusions volontaires : poings, Coup d'Boule, Éclate-Roc, Force, Coupe
(c'est un oiseau) ; Lance-Flammes, Déflagration, Surchauffe (Feu spécial,
Karnhell est physique) ; Damoclès (Rapace et Bec-Canon suffisent) ;
attaques inutilisables (Mimique, Puissance Cachée, Retour, Frustration…).
