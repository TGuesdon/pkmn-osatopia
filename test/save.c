#include "global.h"
#include "pokemon_storage_system.h"
#include "test/test.h"

// If you would like to ensure save compatibility, update the values below with those for your hack. You can find these through the debug menu.
// Please note that this simple check is not 100% foolproof, but should be able to catch most unintended shifts.
// Osatopia : dexSeen et dexCaught (SaveBlock1) sont dimensionnés sur NATIONAL_DEX_COUNT, que chaque
// nouveau monstre Osatopia agrandit. 15568 est la taille vanilla (1025 espèces, 2 x 129 octets de
// drapeaux, alignés à 260) ; on remplace cette part par la taille réelle des drapeaux, alignée sur 4
// octets car trainerHillTimes (u32) suit dexCaught.
#define T_SAVEBLOCK1_SIZE (15568 - 260 + ((2 * NUM_DEX_FLAG_BYTES + 3) & ~3))
#define T_SAVEBLOCK2_SIZE 3884
#define T_SAVEBLOCK3_SIZE 4
#define T_POKEMONSTORAGE_SIZE 34144

TEST("SaveBlock1 is backwards compatible")
{
    EXPECT_EQ(sizeof(struct SaveBlock1), T_SAVEBLOCK1_SIZE);
}

TEST("SaveBlock2 is backwards compatible")
{
    EXPECT_EQ(sizeof(struct SaveBlock2), T_SAVEBLOCK2_SIZE);
}

TEST("SaveBlock3 is backwards compatible")
{
    EXPECT_EQ(sizeof(struct SaveBlock3), T_SAVEBLOCK3_SIZE);
}

TEST("PokemonStorage is backwards compatible")
{
    EXPECT_EQ(sizeof(struct PokemonStorage), T_POKEMONSTORAGE_SIZE);
}

#undef T_SAVEBLOCK1_SIZE
#undef T_SAVEBLOCK2_SIZE
#undef T_SAVEBLOCK3_SIZE
#undef T_POKEMONSTORAGE_SIZE
