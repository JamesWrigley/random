#include <vector>
#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include "stats_functions.h"


TEST(StatsTests, MeanTests)
{
  std::vector<float> natural_numbers_1 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
  std::vector<float> natural_numbers_2 = {34666, 461, 72, 28, 356, 293, 1024, 6096};
  std::vector<float> real_numbers_1 = {-50, 30.68, 200.7, -8, 545.2, 7.4452, -34.2913, 4500};
  std::vector<float> real_numbers_2 = {-687.128, -3824.85353897, -597.129422, -9723.3783463, 3563.234, 996.22, 0, 0, -1, 1};

  EXPECT_FLOAT_EQ(5.5, mean(natural_numbers_1));
  EXPECT_FLOAT_EQ(5374.5, mean(natural_numbers_2));
  EXPECT_FLOAT_EQ(648.967, mean(real_numbers_1));
  EXPECT_FLOAT_EQ(-1027.3035, mean(real_numbers_2));
}


TEST(StatsTests, MedianTests)
{
  // This won't be run through main(), so the vectors need to be sorted first
  std::vector<float> even_vector = {-129, -57.2303, 0, 1, 1, 438};
  std::vector<float> uneven_vector = {-29, -2.5, 0.8, 50, 79.29, 254, 560.69};

  EXPECT_FLOAT_EQ(0.5, median(even_vector));
  EXPECT_FLOAT_EQ(50, median(uneven_vector));
}


TEST(StatsTests, ModeTests) // I couldn't think of a better name...
{
  std::vector<float> generic_vector = {-592, 1294, -5797.69, .0039, -.0039, .0039};
  std::vector<float> no_mode_vector = {-20, -9.469, 50.1, 4096};

  std::vector<float> generic_vector_result = mode(generic_vector);
  std::vector<float> no_mode_vector_result = mode(no_mode_vector);

  EXPECT_FLOAT_EQ(0.0039, generic_vector_result[0]);
  EXPECT_THAT(no_mode_vector, ::testing::ContainerEq(no_mode_vector_result));
}


TEST(StatsTests, LowerQuartileTests)
{
  std::vector<float> even_vector = {-1, -.0293, 0, 56, 128, 489};
  std::vector<float> uneven_vector = {-128, -64, 0.349245, 28, 3930, 3931, 4096};

  EXPECT_FLOAT_EQ(-0.0293, lower_quartile(even_vector));
  EXPECT_FLOAT_EQ(-31.825378, lower_quartile(uneven_vector));
}


TEST(StatsTests, UpperQuartileTests)
{
  std::vector<float> even_vector = {-1, -.0293, 0, 56, 128, 489};
  std::vector<float> uneven_vector = {-128, -64, 0.349245, 28, 3930, 3931, 4096};

  EXPECT_FLOAT_EQ(128, upper_quartile(even_vector));
  EXPECT_FLOAT_EQ(3930.5, upper_quartile(uneven_vector));
}


int main(int argc, char **argv)
{
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
