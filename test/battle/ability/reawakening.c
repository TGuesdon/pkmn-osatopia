#include "global.h"
#include "test/battle.h"

// Osatopia : talent d'Ilyzaelle, calqué sur Power Construct

SINGLE_BATTLE_TEST("Reawakening switches Ilyzaelle to its golden form when HP is below half")
{
    u16 hpBefore = 0;
    GIVEN {
        PLAYER(SPECIES_ILYZAELLE)
        {
            Ability(ABILITY_REAWAKENING);
            HP((GetMonData(&PLAYER_PARTY[0], MON_DATA_MAX_HP) / 2) + 1);
        }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { MOVE(opponent, MOVE_WATER_GUN); MOVE(player, MOVE_CELEBRATE); }
    } SCENE {
        HP_BAR(player, captureHP: &hpBefore);
        MESSAGE("Ilyzaelle's soul is stirring!");
        ABILITY_POPUP(player, ABILITY_REAWAKENING);
        MESSAGE("Ilyzaelle revealed its true form!");
    } THEN {
        EXPECT_EQ(player->species, SPECIES_ILYZAELLE_DOREE);
        EXPECT_GT(player->hp, hpBefore);
    }
}

WILD_BATTLE_TEST("Reawakening Ilyzaelle reverts to its original form upon catching")
{
    GIVEN {
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_ILYZAELLE)
        {
            Ability(ABILITY_REAWAKENING);
            HP((GetMonData(&OPPONENT_PARTY[0], MON_DATA_MAX_HP) / 2) + 1);
        }
    } WHEN {
        TURN { MOVE(player, MOVE_WATER_GUN); }
        TURN { USE_ITEM(player, ITEM_MASTER_BALL); }
    } SCENE {
        ABILITY_POPUP(opponent, ABILITY_REAWAKENING);
        ANIMATION(ANIM_TYPE_SPECIAL, B_ANIM_BALL_THROW, player);
    } THEN {
        EXPECT_EQ(GetMonData(&gPlayerParty[1], MON_DATA_SPECIES), SPECIES_ILYZAELLE);
    }
}
