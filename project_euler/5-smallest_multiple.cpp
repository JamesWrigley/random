// Problem 5 from Project Euler
// http://projecteuler.net/problem=5

#include <iostream>
#include <limits>

int main()
{
  bool is_multiple;
  unsigned int divisible_range;

  std::cout << "Enter a number (r) representing the highest in a range from 0 to r, and I will spit out the smallest number divisible by all in that range: ";
  std::cin >> divisible_range;

  while (!is_multiple)
    {
      for (unsigned int n = 0; n < std::numeric_limits<unsigned int>::max(); n += divisible_range * 3)
        {
          is_multiple = true;

          if (n == 0)
            {
              continue;
            }

          for (unsigned int i = 2; i <= divisible_range; i++)
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
