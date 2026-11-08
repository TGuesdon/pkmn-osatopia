#include "global.h"
#include "test/battle.h"

// Osatopia : Vulbis reprend Synergie (Gen 9) : +1 Att, AtqSpé et Vit au premier K.O., une fois par combat.
ASSUMPTIONS
{
    ASSUME(!IsBattleMoveStatus(MOVE_WATER_GUN));
}

SINGLE_BATTLE_TEST("Vulbis increases Atk, SpAtk and Speed by 1 stage after a KO")
{
    GIVEN {
        PLAYER(SPECIES_CROCABULIA) { Ability(ABILITY_VULBIS); }
        OPPONENT(SPECIES_WOBBUFFET) { HP(1); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(player, MOVE_WATER_GUN); SEND_OUT(opponent, 1); }
    } SCENE {
        HP_BAR(opponent);
        MESSAGE("The opposing Wobbuffet fainted!");
        ABILITY_POPUP(player, ABILITY_VULBIS);
    } THEN {
        EXPECT_EQ(player->statStages[STAT_ATK], DEFAULT_STAT_STAGE + 1);
        EXPECT_EQ(player->statStages[STAT_SPATK], DEFAULT_STAT_STAGE + 1);
        EXPECT_EQ(player->statStages[STAT_SPEED], DEFAULT_STAT_STAGE + 1);
    }
}

SINGLE_BATTLE_TEST("Vulbis only activates once per battle")
{
    GIVEN {
        PLAYER(SPECIES_CROCABULIA) { Ability(ABILITY_VULBIS); }
        OPPONENT(SPECIES_WOBBUFFET) { HP(1); }
        OPPONENT(SPECIES_WOBBUFFET) { HP(1); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(player, MOVE_WATER_GUN); SEND_OUT(opponent, 1); }
        TURN { MOVE(player, MOVE_WATER_GUN); SEND_OUT(opponent, 2); }
    } SCENE {
        ABILITY_POPUP(player, ABILITY_VULBIS);
        MESSAGE("The opposing Wobbuffet fainted!");
        NOT ABILITY_POPUP(player, ABILITY_VULBIS);
    } THEN {
        EXPECT_EQ(player->statStages[STAT_ATK], DEFAULT_STAT_STAGE + 1);
        EXPECT_EQ(player->statStages[STAT_SPATK], DEFAULT_STAT_STAGE + 1);
        EXPECT_EQ(player->statStages[STAT_SPEED], DEFAULT_STAT_STAGE + 1);
    }
}
