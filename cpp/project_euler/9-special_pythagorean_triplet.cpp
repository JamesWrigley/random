// Problem 9 from Project Euler
// http://projecteuler.net/problem=9

#include <cmath>
#include <array>
#include <numeric>
#include <iostream>

int main()
{
  std::array<unsigned int, 1000> range;
  std::iota(range.begin(), range.end(), 1);

  for (unsigned int a = 0; a < 997; a++)
    {
      unsigned int int_a = range[a];
      for (unsigned int b = a + 1; b < 998; b++)
        {
          unsigned int int_b = range[b];
          unsigned int c = 1000 - (int_a + int_b);

          if (pow(int_a, 2) + pow(int_b, 2) == pow(c, 2))
            {
              std::cout << int_a << " * " << int_b << " * " << c << " = " << int_a * int_b * c << std::endl;
              return 0;
            }
        }
    }
}
