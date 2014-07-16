/*
  A program that generates various statistical data from a user in-putted bunch
  of numbers. Specifically, it calculates the mean, median (AKA middle quartile),
  mode, lower quartile and upper quartile.
*/

#include <vector>
#include <string>
#include <iostream>
#include <exception>
#include "stats_functions.h"
#include <boost/algorithm/string.hpp>

int main()
{
  std::vector<float> numbers_vect;
  std::string raw_input;
  std::vector<std::string> raw_input_vect;

  // Input section
  std::cout << "Enter the list of numbers separated by spaces: ";
  std::getline(std::cin, raw_input); // I should put this in a header
  // Trim whitespace, then split raw_input into numbers_str by whitespace, then converts the string vector into an float vector
  boost::trim(raw_input);
  boost::split(raw_input_vect, raw_input, boost::is_any_of("\t "));
  try
    {
      std::transform(raw_input_vect.begin(), raw_input_vect.end(), std::back_inserter(numbers_vect), [](const std::string& val) { return std::stof(val); });
    }
  catch (std::exception e)
    {
      std::cout << "Invalid input! An element was entered that is not a number." << std::endl;
      return 1;
    }


  // Sorts the numbers numerically
  std::sort(numbers_vect.begin(), numbers_vect.end());

  std::cout << "Mean: " << mean(numbers_vect) << std::endl;
  std::cout << "Median (also middle quartile): " << median(numbers_vect) << std::endl;
  std::cout << "Lower Quartile: " << lower_quartile(numbers_vect) << std::endl;
  std::cout << "Upper Quartile: " << upper_quartile(numbers_vect) << std::endl;
  std::cout << "Mode: " << print_mode(numbers_vect) << std::endl;
}
