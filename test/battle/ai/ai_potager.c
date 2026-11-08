#include "global.h"
#include "test/battle.h"
#include "battle_ai_util.h"

// Osatopia : Potager est exclu de « AI can use all moves » (comme Wish ou Lucky Chant) car,
// en double, une capacité qui cible le lanceur y est comparée à Splash contre le partenaire,
// où les deux valent 90. Son comportement IA est vérifié ici.

AI_SINGLE_BATTLE_TEST("AI uses Potager when it has Pokémon left to switch in")
{
    GIVEN {
        ASSUME(GetMoveEffect(MOVE_POTAGER) == EFFECT_POTAGER);
        AI_FLAGS(AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_CHECK_VIABILITY | AI_FLAG_TRY_TO_FAINT);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET) { Moves(MOVE_SPLASH, MOVE_POTAGER); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { EXPECT_MOVE(opponent, MOVE_POTAGER); }
    }
}

AI_SINGLE_BATTLE_TEST("AI does not use Potager without Pokémon left to switch in")
{
    GIVEN {
        AI_FLAGS(AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_CHECK_VIABILITY | AI_FLAG_TRY_TO_FAINT);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET) { Moves(MOVE_SPLASH, MOVE_POTAGER); }
    } WHEN {
        TURN { SCORE_LT_VAL(opponent, MOVE_POTAGER, AI_SCORE_DEFAULT); }
    }
}

AI_SINGLE_BATTLE_TEST("AI stops using Potager once three layers are planted")
{
    GIVEN {
        AI_FLAGS(AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_CHECK_VIABILITY | AI_FLAG_TRY_TO_FAINT);
        PLAYER(SPECIES_WOBBUFFET);
        OPPONENT(SPECIES_WOBBUFFET) { Moves(MOVE_SPLASH, MOVE_POTAGER); }
        OPPONENT(SPECIES_WOBBUFFET);
    } WHEN {
        TURN { EXPECT_MOVE(opponent, MOVE_POTAGER); }
        TURN { EXPECT_MOVE(opponent, MOVE_POTAGER); }
        TURN { EXPECT_MOVE(opponent, MOVE_POTAGER); }
        // Potager échouerait : il ne doit pas valoir mieux que Splash.
        TURN { SCORE_LT_VAL(opponent, MOVE_POTAGER, AI_SCORE_DEFAULT); SCORE_EQ(opponent, MOVE_POTAGER, MOVE_SPLASH); }
    }
}
