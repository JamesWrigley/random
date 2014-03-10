#include <vector>
#include "gtest/gtest.h"
#include "stats_functions.h"

// Tests for the mean() function
TEST(MeanTest, NaturalAndRealNumbers)
{
  std::vector<float> natural_numbers_1 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  std::vector<float> natural_numbers_2 = {34666, 461, 72, 28, 356, 293, 1024, 6096};
  std::vector<float> real_numbers_1 = {-50, 30.68, 200.7, -8, 545.2, 7.4452, -34.2913, 4500};
  std::vector<float> real_numbers_2 = {-687.128, -3824.85353897, -597.129422, -9723.3783463, 3563.234, 996.22, 0, 0, -1, 1};

  EXPECT_EQ(5.5, mean(natural_numbers_1));
  EXPECT_EQ(5374.5, mean(natural_numbers_2));
  EXPECT_EQ(648.697, mean(real_numbers_1));
  EXPECT_EQ(-1027.3, mean(real_numbers_2));
}

int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
