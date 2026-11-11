# Famille Bitouf

> Oiseaux-plantes de l'Otomaï. Le Bitouf des Plaines (Plaines herbeuses,
> niv. 97–109) a 10 PM et une grosse Fuite ; *Vrüt vrüt* frappe en Air d'autant
> plus fort que le lanceur a perdu de PV et réduit les soins, *Plumeau
> Cécitant* réduit la portée. Le Bitouf Aérien (Canopée du Kimbo, niv. 144–160)
> résiste à l'Air, craint la Terre ; *Envolupté* donne +2 PM à tout le
> terrain, *Tornade pernicieuse* repousse, *Aéroportage* échange les
> positions. Le Disciple du Kimbo (Peuple de l'Arbre) sert de bébé : lien de
> famille **à vérifier**. — Évolutions : Bebitouf → Bitouf (niv. 16) →
> Bitouvol (niv. 36).

**État** : validée et intégrée.

## Intention
Archétype : attaquant à boost (setup sweeper), pivot en secondaire ·
Références : Flambusard (oiseau physique très rapide), Miascarade (Plante
physique rapide), Brutalibré (profil de stats du brouillon) ·
Pourquoi : Turbo fait le travail de la Vitesse, Danse Lames celui de
l'Attaque ; Gigotage traduit *Vrüt vrüt* (plus fort à PV bas) et profite du
contrecoup de Rapace. Se distingue de Kwak Vent, oiseau physique rapide mais
nettoyeur à priorités (Peau Céleste).

## Stades
| | Bebitouf | Bitouf | Bitouvol |
|---|---|---|---|
| Constante | `SPECIES_DISCIPLE_DU_KIMBO` | `SPECIES_BITOUF_PLAINE` | `SPECIES_BITOUF_AERIEN` |
| Types | Plante | Plante/Vol | Plante/Vol |
| PV / Att / Déf / AtqSpé / DéfSpé / Vit | 45 / 52 / 35 / 25 / 35 / 68 | 65 / 80 / 55 / 35 / 50 / 100 | 80 / 110 / 68 / 45 / 62 / 130 |
| Total | 260 | 385 | 495 |
| Talents | Turbo / Acharné / caché Délestage | idem | idem |
| Capture / Exp. | 190 / 64 | 100 / 145 | 45 / 225 |
| EV | Vit +1 | Vit +2 | Att +1, Vit +2 |

Stats sacrifiées : AtqSpé (tout est physique), défenses moyennes à faibles
(il doit trouver un tour pour booster, pas tout encaisser). Faiblesse ×4 à la
Glace assumée.

Autres champs (repris du brouillon) : 50 % femelle, 20 cycles d'œuf,
`STANDARD_FRIENDSHIP`, `GROWTH_MEDIUM_SLOW`, couleur marron. Groupes d'œuf
Vol + Plante (au lieu de Vol + Monstre).

## Kit final
| Rôle | Attaque | Alternatives |
|---|---|---|
| Boost | Danse Lames (Swords Dance) | Aiguisage, Gonflette, Abri (tour de Turbo gratuit) |
| STAB Plante | Lame Feuille (Leaf Blade, 90) | Botte Sucrette, Mégafouet, Encornebois, Canon Graine |
| STAB Vol | Rapace (Brave Bird, 120) | Bec Vrille, Acrobatie, Rebond |
| Mécanique | Gigotage (Flail) | Pied Voltige, Éboulement, Demi-Tour, Coup Bas |

Synergies : Turbo + Danse Lames ; Rapace (contrecoup) et Ténacité (tuteur) →
Gigotage à pleine puissance ; Délestage après une Baie consommée.

## Capacités custom
Aucune.

## Learnsets
### Bebitouf
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| 1 | Charge (Tackle) | Normal | Phys. | 40 |
| 1 | Groz'Yeux (Leer) | Normal | Statut | – |
| 4 | Feuillage (Leafage) | Plante | Phys. | 40 |
| 7 | Vive-Attaque (Quick Attack) | Normal | Phys. | 40 prio+1 |
| 10 | Jet de Sable (Sand Attack) | Sol | Statut | – |
| 13 | Tranch'Herbe (Razor Leaf) | Plante | Phys. | 55 |
| 16 | Double Pied (Double Kick) | Combat | Phys. | 30×2 |
| 20 | Botte Sucrette (Trop Kick) | Plante | Phys. | 70 |
| 24 | Gigotage (Flail) | Normal | Phys. | var. |
| 28 | Lame Feuille (Leaf Blade) | Plante | Phys. | 90 |
| 32 | Danse Lames (Swords Dance) | Normal | Statut | – |

### Bitouf
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Cru-Ailes (Wing Attack) | Vol | Phys. | 60 |
| 1–13 | mêmes que Bebitouf | | | |
| 20 | Botte Sucrette (Trop Kick) | Plante | Phys. | 70 |
| 23 | Demi-Tour (U-turn) | Insecte | Phys. | 70 |
| 26 | Gigotage (Flail) | Normal | Phys. | var. |
| 30 | Lame Feuille (Leaf Blade) | Plante | Phys. | 90 |
| 33 | Aiguisage (Hone Claws) | Ténèbres | Statut | – |
| 38 | Bec Vrille (Drill Peck) | Vol | Phys. | 80 |
| 42 | Danse Lames (Swords Dance) | Normal | Statut | – |
| 46 | Rapace (Brave Bird) | Vol | Phys. | 120 |

### Bitouvol
| Niv. | Attaque | Type | Cat. | Puiss. |
|---|---|---|---|---|
| Évo | Danse Lames (Swords Dance) | Normal | Statut | – |
| 1 | Cru-Ailes (Wing Attack) | Vol | Phys. | 60 |
| 1–13 | mêmes que Bebitouf | | | |
| 20–38 | mêmes que Bitouf | | | |
| 43 | Atterrissage (Roost) | Vol | Statut | – |
| 46 | Rapace (Brave Bird) | Vol | Phys. | 120 |
| 52 | Vent Arrière (Tailwind) | Vol | Statut | – |

Bitouvol reçoit Danse Lames dès l'évolution (36) ; Bitouf ne l'a qu'au 42.

## CT, CS et tuteurs
| Attaque | Source | Bebitouf | Bitouf | Bitouvol |
|---|---|:-:|:-:|:-:|
| Toxik, Abri, Zénith, Repos, Attraction, Façade, Reflet | CT | ✓ | ✓ | ✓ |
| Balle Graine, Aéropique, Tomberoche | CT | ✓ | ✓ | ✓ |
| Provoc, Faux-Chage, Larcin | CT | ✓ | ✓ | ✓ |
| Gonflette, Ailes d'Acier | CT | | ✓ | ✓ |
| Coupe, Éclate-Roc, Force | CS | ✓ | ✓ | ✓ |
| Vol | CS | | | ✓ |
| Danse Lames, Ténacité, Coud'Boue, Blabla Dodo, Ronflement | Tuteur | ✓ | ✓ | ✓ |
| Éboulement, Ultimawashi | Tuteur | | ✓ | ✓ |

Exclusions volontaires : attaques spéciales (Lance-Soleil, Méga-Sangsue,
Ultralaser…), Séisme, Queue de Fer, Casse-Brique et coups de poing (oiseau
sans bras), Vol pour Bitouf (coureur des plaines).
