// Problem 5 from Project Euler
// http://projecteuler.net/problem=5

#include <iostream>
#include <math.h>
#include <limits>

int main()
{
  bool is_multiple;

  while (!is_multiple)
    {
      for (unsigned int n = 0; n < std::numeric_limits<unsigned int>::max(); n += 80)
        {
          is_multiple = true;

          if (n == 0)
            {
              continue;
            }

          for (unsigned int i = 2; i <= 20; i++)
            {
              if (n % i != 0)
                {
                  is_multiple = false;
                  break;
                }
            }
          if (is_multiple)
            {
              std::cout << "The answer is " << n << std::endl;
              exit(0);
            }
        }
    }
}
