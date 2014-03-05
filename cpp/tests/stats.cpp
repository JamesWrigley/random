/*
  A program that generates various statistical data from a user inputted bunch
  of numbers. Specifically, it calculates the mean and median. Support for the
  quartiles is coming.
*/

#include <math.h>
#include <algorithm>
#include <boost/algorithm/string.hpp>

float median(std::vector<float> numbers)
{
  int vector_size = numbers.size();

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

float mean(std::vector<float> numbers)
{
  // Self-explanatory, this calculates the mean of the numbers
  float mean_value = std::accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
  return mean_value;
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
      for (unsigned int n = 0; n < numbers.size(); n++)
        {
          if (numbers[n] >= numbers_median)
            {
              upper_half.push_back(numbers[n]);
            }
          else
            {
              continue;
            }
        }
    }
  else
    {
      for (unsigned int n = 0; n < numbers.size(); n++)
        {
          if (numbers[n] > numbers_median)
            {
              upper_half.push_back(numbers[n]);
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


int main()
{
  std::vector<float> numbers_vect;
  std::string raw_input;
  std::vector<std::string> raw_input_vect;

  std::cout << "Enter the list of numbers separated by spaces: ";
  std::getline(std::cin, raw_input);

  // Split numbers_str by whitespace, then converts the string vector into an float vector
  boost::split(raw_input_vect, raw_input, boost::is_any_of("\t "));
  std::transform(raw_input_vect.begin(), raw_input_vect.end(), std::back_inserter(numbers_vect), [](const std::string& val) { return std::stof(val); });

  // Sorts the numbers numerically
  std::sort(numbers_vect.begin(), numbers_vect.end());

  std::cout << "Mean: " << mean(numbers_vect) << std::endl;
  std::cout << "Median (also middle quartile): " << median(numbers_vect) << std::endl;
  std::cout << "Lower Quartile: " << lower_quartile(numbers_vect) << std::endl;
  std::cout << "Upper Quartile: " << upper_quartile(numbers_vect) << std::endl;
}
