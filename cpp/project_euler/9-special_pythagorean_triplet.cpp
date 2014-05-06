// Problem 9 from Project Euler
// http://projecteuler.net/problem=9

#include <cmath>
#include <array>
#include <numeric>
#include <iostream>

int main()
{
  // We set 'a's upper bound to 998, thus making sure that it will always be
  // possible to get a 'b' and 'c' larger than 'a'
  for (unsigned int a = 1; a <= 998; a++)
    {
      for (unsigned int b = a + 1; b <= 999; b++) // Note that 'b' will always be greater than 'a'
        {
          unsigned int c = 1000 - (a + b);

          if (pow(a, 2) + pow(b, 2) == pow(c, 2))
            {
              std::cout << a << " * " << b << " * " << c << " = " << a * b * c << std::endl;
              return 0;
            }
        }
    }
}
