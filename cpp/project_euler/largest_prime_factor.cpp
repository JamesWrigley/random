// Problem 3 from Project Euler
// http://projecteuler.net/problem=3

#include <iostream>
#include <vector>
#include <math.h>

int main()
{
  double largest_prime = 1;
  double number = 600851475143;
  std::vector<double> factors;

  for (double f = 1; f < sqrt(number); f++)
    {
      if (fmod(number, f) == 0)
        {
          factors.push_back(f);
        }
    }

  for (unsigned int i = 0; i < factors.size(); i++)
    {
      bool is_prime = true;

      if (fmod(factors[i], 2) == 0)
        {
          continue;
        }
      else if (fmod(factors[i], 3) == 0)
        {
          continue;
        }
      else
        {
          double divisor = 4;
          while (divisor < (factors[i] / 2))
            {
              if (fmod(factors[i], divisor) == 0)
                {
                  is_prime = false;
                }
              divisor++;
            }
        }

      if (is_prime)
        {
          largest_prime = factors[i];
        }
    }
  std::cout << largest_prime << std::endl;
}
