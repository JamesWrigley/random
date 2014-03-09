#include "stats_functions.h"
#include "gtest/gtest.h"

// Tests for the mean() function
TEST(MeanTest, PositiveNumbers)
{
  std::vector<float> natural_numbers = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  std::vector<float> real_numbers = {-50, 30.68, 200.7, -8, 545.2, 7.4452, -34.2913, 4500};

  // float natural_numbers_mean = mean(natural_numbers);
  // float real_numbers_mean = mean(real_numbers);

  EXPECT_EQ(5.5, mean(natural_numbers));
  EXPECT_EQ(648.96674, mean(real_numbers));
}
