// A weird temperature converter from http://www.cprogramming.com/challenges/celsius_converter_table.html

#include <iostream>
#include <iomanip>

using std::cout;
using std::cin;

float convert_to_fahrenheit(float celsius_temp)
{
  return celsius_temp * 1.8 + 32;
}

int main()
{
  // Declare temperature variables
  float lower_limit;
  float upper_limit;
  float step_size;

  // Gets input from the user and checks that they're valid
  while (true)
    {
      // -50 is an arbitrary number
      cout << "Please enter a lower limit (it must be more than or equal to -50): ";
      cin >> lower_limit;
      if (lower_limit < -50)
        {
          continue;
        }
      else
        {
          break;
        }
    }

  while (true)
    {
      cout << "Please enter an upper limit (it must be more than " << lower_limit << "): ";
      cin >> upper_limit;
      if (upper_limit <= lower_limit)
        {
          continue;
        }
      else
        {
          break;
        }
    }

  while (true)
    {
      cout << "Please enter a step size (it must be less than " << upper_limit - lower_limit << "): ";
      cin >> step_size;
      if (step_size >= upper_limit - lower_limit)
        {
          continue;
        }
      else
        {
          break;
        }
    }

  cout << "Celsius      Fahrenheit" << std::endl;
  cout << "-------      ----------" << std::endl;

  float step_value = lower_limit;
  while (step_value < upper_limit)
    {
      // Regulate the spacing between the temperatures, doesn't fully work yet
      std::string spacing = "       ";
      if (step_value < 0)
        {
          spacing = "      ";
        }
      cout << std::fixed << std::setprecision(4) << step_value << spacing << convert_to_fahrenheit(step_value) << std::endl;
      step_value += step_size;
    }

  return 0;
}
