# Famille Aminite

> Aminite (DofusDB 4107) : petit champignon fluorescent des mines d'Incarnam
> (Coup de Piléus −1 PA, Spore Tensia réduit les dommages). Dremoan
> (DofusDB 2908) : champignon spectral de la Forêt pétrifiée de Frigost, qui
> vole la vie, corrompt et ramène les morts. Les deux ne sont pas de la même
> race dans Dofus ; ils sont réunis pour leur look fluorescent. — Évolution :
> Aminite → Dremoan au niveau 30.

**État** : validée et intégrée.

## Intention
Archétype : propagateur de statuts (Aminite), puis soutien drainant (Dremoan) · Références : Paras / Parasect, Bourgeon, Gouroutan (profil) · Pourquoi : un Électrik pour New Mauville, avec un double type inédit Plante/Électrik justifié par la bioluminescence. Dremoan se distingue de Dieubouftou (Normal/Électrik spécial) par moins d'AtqSpé et plus de DéfSpé : il draine au lieu de frapper.

## Stades
| | Aminite | Dremoan |
|---|---|---|
| Types | Plante / Électrik | Plante / Électrik |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 60 / 40 / 60 / 55 / 65 / 30 | 100 / 50 / 80 / 90 / 105 / 55 |
| Total | 310 | 480 |
| Talents | Pose Spore / Statik / caché Filtre | Pose Spore / Statik / caché Corps Maudit |
| Capture / Exp. | 190 / 64 | 75 / 170 |
| EV | +1 DéfSpé | +2 DéfSpé |
| Taille / poids | 0,5 m / 6 kg | 1,6 m / 45 kg |

Croissance `GROWTH_MEDIUM_FAST` (comme Paras). 50 % femelles, groupe Plante, 15 cycles.

## Kit final (Dremoan)
| Rôle | Choix | Alternatives |
|---|---|---|
| STAB Plante (drain) | Giga-Sangsue | Éco-Sphère |
| STAB Électrik (drain) | Parabocharge | Tonnerre, Coup d'Jus |
| Usure | Vampigraine (Ronce de dépérissement) | Spore, Para-Spore |
| Soin | Vole-Force (Mains crochues) | Synthèse, Racines |

## Capacités custom
Aucune.

## Learnsets
| Niv. | Aminite | Dremoan |
|---|---|---|
| Évo | | Vole-Force (Strength Sap) |
| 1 | Vole-Vie (Absorb), Éclair (Thunder Shock) | idem |
| 5 | Spore Coton (Cotton Spore) | idem |
| 8 | Para-Spore (Stun Spore) | idem |
| 11 | Méga-Sangsue (Mega Drain) | idem |
| 14 | Vampigraine (Leech Seed) | idem |
| 18 | Parabocharge (Parabolic Charge) | idem |
| 21 | Poudre Dodo (Sleep Powder) | idem |
| 24 | Giga-Sangsue (Giga Drain) | idem |
| 27 | Synthèse (Synthesis) | idem |
| 31 | Coup d'Jus (Discharge) | |
| 33 | | Coup d'Jus |
| 35 | Éco-Sphère (Energy Ball) | |
| 37 | | Racines (Ingrain) |
| 41 | | Spore |
| 45 | | Éco-Sphère |
| 50 | | Tonnerre (Thunderbolt) |

## CT, CS et tuteurs
- Communs : Tonnerre, Fatal-Foudre, Onde de Choc, Giga-Sangsue, Lance-Soleil, Zénith, Danse Pluie, Abri, Repos, Façade, Toxik, Mur Lumière, Rune Protect, Reflet, Attraction, Cage Éclair, Clonage, Ténacité, Vantardise, Blabla Dodo, Ronflement, Coud'Boue.
- Dremoan en plus : Ball'Ombre, Dévorêve.
- Exclusions volontaires : attaques physiques (poings, Balle Graine), vol, nage.

## Sprites
Dremoan est translucide : `translucent_over` dans `overrides.json` garde les doigts de son chapeau visibles.
