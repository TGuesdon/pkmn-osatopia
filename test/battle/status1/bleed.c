#include "global.h"
#include "test/battle.h"

// Osatopia : Saignement (STATUS1_BLEED), Déchirure, Lacération et Hémorragie.

SINGLE_BATTLE_TEST("Bleed deals 1/16 to 1/8 of max HP per turn depending on base Speed")
{
    s16 damage;
    u32 species, numerator;
    // Dégâts = PV max * (Vitesse de base bornée à [50, 110] + 10) / 960
    PARAMETRIZE { species = SPECIES_WOBBUFFET; numerator = 60; }  // Vitesse 33 -> 1/16
    PARAMETRIZE { species = SPECIES_PIKACHU;   numerator = 100; } // Vitesse 90
    PARAMETRIZE { species = SPECIES_JOLTEON;   numerator = 120; } // Vitesse 130 -> 1/8
    GIVEN {
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(species) { Status1(STATUS1_BLEED); }
    } WHEN {
        TURN {}
    } SCENE {
        HP_BAR(opponent, captureDamage: &damage);
    } THEN {
        EXPECT_EQ(damage, opponent->maxHP * numerator / 960);
    }
}

SINGLE_BATTLE_TEST("Bleed: Dechirure inflicts Bleed")
{
    GIVEN {
        ASSUME(GetMoveNonVolatileStatus(MOVE_DECHIRURE) == MOVE_EFFECT_BLEED);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(player, MOVE_DECHIRURE); }
    } SCENE {
        ANIMATION(ANIM_TYPE_MOVE, MOVE_DECHIRURE, player);
        ANIMATION(ANIM_TYPE_STATUS, B_ANIM_STATUS_BLD, opponent);
        MESSAGE("The opposing Wobbuffet saigne!");
        MESSAGE("The opposing Wobbuffet perd du sang!");
        ANIMATION(ANIM_TYPE_STATUS, B_ANIM_STATUS_BLD, opponent);
    } THEN {
        EXPECT(opponent->status1 & STATUS1_BLEED);
    }
}

SINGLE_BATTLE_TEST("Bleed: Ghost, Steel and Rock types can't Bleed")
{
    u32 species;
    PARAMETRIZE { species = SPECIES_GASTLY; }
    PARAMETRIZE { species = SPECIES_MAGNEMITE; }
    PARAMETRIZE { species = SPECIES_GEODUDE; }
    GIVEN {
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(species);
    } WHEN {
        TURN { MOVE(player, MOVE_DECHIRURE); }
    } SCENE {
        NOT ANIMATION(ANIM_TYPE_MOVE, MOVE_DECHIRURE, player);
    } THEN {
        EXPECT(!(opponent->status1 & STATUS1_BLEED));
    }
}

SINGLE_BATTLE_TEST("Bleed: Laceration has a 10% chance to inflict Bleed")
{
    PASSES_RANDOMLY(10, 100, RNG_SECONDARY_EFFECT);
    GIVEN {
        ASSUME(GetMovePower(MOVE_LACERATION) == 75);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(player, MOVE_LACERATION); }
    } SCENE {
        ANIMATION(ANIM_TYPE_MOVE, MOVE_LACERATION, player);
        MESSAGE("The opposing Wobbuffet saigne!");
    }
}

SINGLE_BATTLE_TEST("Bleed: Hemorragie has a 20% chance to inflict Bleed with physical moves")
{
    PASSES_RANDOMLY(20, 100, RNG_POISON_TOUCH);
    GIVEN {
        PLAYER(SPECIES_WOBBUFFET) { Ability(ABILITY_HEMORRAGIE); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(player, MOVE_TACKLE); }
    } SCENE {
        ANIMATION(ANIM_TYPE_MOVE, MOVE_TACKLE, player);
        ABILITY_POPUP(player, ABILITY_HEMORRAGIE);
        MESSAGE("The opposing Wobbuffet saigne!");
    }
}

SINGLE_BATTLE_TEST("Bleed: Hemorragie doesn't trigger on special moves")
{
    GIVEN {
        ASSUME(GetMoveCategory(MOVE_SWIFT) == DAMAGE_CATEGORY_SPECIAL);
        PLAYER(SPECIES_WOBBUFFET) { Ability(ABILITY_HEMORRAGIE); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(player, MOVE_SWIFT); }
    } SCENE {
        ANIMATION(ANIM_TYPE_MOVE, MOVE_SWIFT, player);
        NOT ABILITY_POPUP(player, ABILITY_HEMORRAGIE);
    } THEN {
        EXPECT(!(opponent->status1 & STATUS1_BLEED));
    }
}

SINGLE_BATTLE_TEST("Bleed: Lum Berry cures Bleed")
{
    GIVEN {
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET) { Item(ITEM_LUM_BERRY); }
    } WHEN {
        TURN { MOVE(player, MOVE_DECHIRURE); }
    } SCENE {
        MESSAGE("The opposing Wobbuffet saigne!");
        ANIMATION(ANIM_TYPE_GENERAL, B_ANIM_HELD_ITEM_EFFECT, opponent);
    } THEN {
        EXPECT(!(opponent->status1 & STATUS1_BLEED));
    }
}

SINGLE_BATTLE_TEST("Bleed: Magic Guard prevents Bleed damage")
{
    GIVEN {
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_CLEFABLE) { Ability(ABILITY_MAGIC_GUARD); Status1(STATUS1_BLEED); }
    } WHEN {
        TURN {}
    } SCENE {
        NOT MESSAGE("The opposing Clefable perd du sang!");
    }
}
