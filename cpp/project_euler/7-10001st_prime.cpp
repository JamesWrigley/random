// Problem 1 from Project Euler
// http://projecteuler.net/problem=7

#include <iostream>
#include <limits>

int main()
{
  int prime_index_number = 0;
  int prime;
  //  int n = 4;

  for (int pin = 0; prime_index_number <= 6; pin++)
    {
      bool is_prime = true;

      int divisor = 2;
      while (divisor < (pin / 2))
        {
          if (pin % divisor == 0)
            {
              is_prime = false;
              divisor++;
              break;
            }
          divisor++;
        }

      if (is_prime)
        {
          prime_index_number++;
          std::cout << pin << std::endl;
        }
    }

  std::cout << prime << std::endl;
}
