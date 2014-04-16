// Problem 9 from Project Euler
// http://projecteuler.net/problem=9

#include <cmath>
#include <array>
#include <numeric>
#include <iostream>

int main()
{
  std::array<unsigned int, 1000> range;
  std::iota(range.begin(), range.end(), 1); // Populate the range array

  // We set 'a's upper bound to 997 so that the max value of 'int_a' will be 998,
  // thus making sure that it will always be possible to get an 'int_b' and 'c' larger than 'a'
  for (unsigned int a = 0; a <= 997; a++)
    {
      unsigned int int_a = range[a];
      for (unsigned int b = a + 1; b < 998; b++) // Note that 'b' will always be greater than 'a'
        {
          unsigned int int_b = range[b];
          unsigned int int_c = 1000 - (int_a + int_b);

          if (pow(int_a, 2) + pow(int_b, 2) == pow(int_c, 2))
            {
              std::cout << int_a << " * " << int_b << " * " << int_c << " = " << int_a * int_b * int_c << std::endl;
              return 0;
            }
        }
    }
}
