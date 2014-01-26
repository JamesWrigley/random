// Problem 2 from Project Euler
// http://projecteuler.net/problem=2

#include <iostream>
#include <math.h>
#include <limits>

int main()
{
  for (int n = 1; n < std::numeric_limits<int>::max(); n++)
    {
      bool is_multiple = true;
      for (int i = 1; i < 20; i++)
        {
          if (n % i != 0)
            {
              is_multiple = false;
            }
        }
      if (is_multiple)
        {
          std::cout << "The answer is " << n << std::endl;
          exit(0);
        }
    }
}
