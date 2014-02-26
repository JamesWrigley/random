/*
  A program that generates various statistical data from a user inputted bunch
  of numbers. Specifically, it calculates the mean and median. Support for the
  quartiles is coming.
*/

// IMPORTANT:
// To get the first and third quatiles, get the median of the upper and lower parts of the median


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
  std::copy_n(numbers.begin(), median(numbers), lower_half.begin());

  return 42.0;
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
}
