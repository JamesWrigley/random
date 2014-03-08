#include <cmath>
#include <vector>
#include <algorithm>
#include "stats_functions.h"
#include <boost/algorithm/string.hpp>

float mean(std::vector<float> numbers)
{
  // Self-explanatory, this calculates the mean of the numbers
  float mean_value = std::accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
  return mean_value;
}


float median(std::vector<float> numbers)
{
  int vector_size = numbers.size(); // So we don't have to recompute it often

  // Cases for where the vector size is odd and even, respectively
  if (vector_size % 2 != 0)
    {
      return numbers[vector_size / 2];
    }
  else
    {
      float median_value = (numbers[vector_size / 2] + numbers[(vector_size / 2) - 1]) / 2;
      return median_value;
    }
}


std::vector<float> mode(std::vector<float> numbers)
{
  std::vector<float> mode_values; // What the mode(s) will be put into
  unsigned int last_N_occurrences = 0; // Holds the current largest number of occurrences

  for (float n : numbers)
    {
      unsigned int n_occurrences = std::count(numbers.begin(), numbers.end(), n); // The number of occurrences for the current n

      // Is the number of occurrences more than the last mode? If so, then clear
      // mode_values and replace with new mode. Else append.
      if (n_occurrences > last_N_occurrences)
        {
          last_N_occurrences = n_occurrences;
          mode_values.clear();
          mode_values.push_back(n);
        }
      else if (n_occurrences == last_N_occurrences)
        {
          mode_values.push_back(n);
        }
    }

  // Remove doubles from mode_values, could be optimized
  std::vector<float>::iterator rm_doubles = std::unique(mode_values.begin(), mode_values.end());
  mode_values.resize(std::distance(mode_values.begin(), rm_doubles));

  return mode_values;
}


float lower_quartile(std::vector<float> numbers)
{
  std::vector<float> lower_half;
  float numbers_median = median(numbers); // So we don't have to recompute it often
  float lower_quartile_value;

  // If the median is in the numbers vector, then include it in the lower_half
  // vector, else don't include it.
  if (std::find(numbers.begin(), numbers.end(), numbers_median) != numbers.end())
    {
      for (int n = 0; numbers[n] <= numbers_median; n++)
        {
          lower_half.push_back(numbers[n]);
        }
    }
  else
    {
      for (int n = 0; numbers[n] < numbers_median; n++)
        {
          lower_half.push_back(numbers[n]);
        }
    }

  lower_quartile_value = median(lower_half);

  return lower_quartile_value;
}


float upper_quartile(std::vector<float> numbers)
{
  std::vector<float> upper_half;
  float numbers_median = median(numbers); // So we don't have to recompute it often
  float upper_quartile_value;


  // If the median is in the numbers vector, then include it in the upper_half
  // vector, else don't include it.
  if (std::find(numbers.begin(), numbers.end(), numbers_median) != numbers.end())
    {
      for (float n : numbers)
        {
          if (n >= numbers_median)
            {
              upper_half.push_back(n);
            }
          else
            {
              continue;
            }
        }
    }
  else
    {
      for (float n : numbers)
        {
          if (n > numbers_median)
            {
              upper_half.push_back(n);
            }
          else
            {
              continue;
            }
        }
    }

  upper_quartile_value = median(upper_half);

  return upper_quartile_value;
}
