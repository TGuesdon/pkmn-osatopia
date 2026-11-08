#include "global.h"
#include "test/battle.h"
#include "battle_ai_util.h"

// Osatopia : Lait de Coco est exclu de « AI can use all moves » (comme Soft-Boiled ou Refresh) car,
// en double, une capacité qui cible le lanceur y est comparée à Splash contre le partenaire,
// où les deux valent 90. Son comportement IA est vérifié ici.

AI_SINGLE_BATTLE_TEST("AI uses Lait de Coco when its HP are low")
{
    GIVEN {
        ASSUME(GetMoveEffect(MOVE_LAIT_DE_COCO) == EFFECT_LAIT_DE_COCO);
        AI_FLAGS(AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_CHECK_VIABILITY | AI_FLAG_TRY_TO_FAINT);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET) { HP(30); MaxHP(100); Moves(MOVE_SPLASH, MOVE_LAIT_DE_COCO); }
    } WHEN {
        TURN { EXPECT_MOVE(opponent, MOVE_LAIT_DE_COCO); }
    }
}

AI_SINGLE_BATTLE_TEST("AI uses Lait de Coco to cure its status at full HP")
{
    GIVEN {
        AI_FLAGS(AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_CHECK_VIABILITY | AI_FLAG_TRY_TO_FAINT);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET) { Status1(STATUS1_PARALYSIS); Moves(MOVE_SPLASH, MOVE_LAIT_DE_COCO); }
    } WHEN {
        TURN { EXPECT_MOVE(opponent, MOVE_LAIT_DE_COCO); }
    }
}

AI_SINGLE_BATTLE_TEST("AI does not use Lait de Coco at full HP without status")
{
    GIVEN {
        AI_FLAGS(AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_CHECK_VIABILITY | AI_FLAG_TRY_TO_FAINT);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET) { Moves(MOVE_SPLASH, MOVE_LAIT_DE_COCO); }
    } WHEN {
        TURN { SCORE_LT_VAL(opponent, MOVE_LAIT_DE_COCO, AI_SCORE_DEFAULT); }
    }
}
