// Problem 1 from Project Euler
// http://projecteuler.net/problem=7

#include <iostream>

int main()

{
  unsigned int prime_index_number = 0;
  unsigned int prime_number;

  for (unsigned int n = 0; prime_index_number < 10001; n++)
    {
      bool is_prime = true;

      unsigned int divisor = 2;
      if (n < 2)
        {
          continue;
        }
      else if (n > 2 && (n % 2 == 0))
        {
          continue;
        }
      else{
        while (divisor < (n / 2))
          {
            if (n % divisor == 0)
              {
                is_prime = false;
                break;
              }
            divisor++;
          }
      }

      if (is_prime)
        {
          prime_index_number++;
          prime_number = n;
        }
    }

  std::cout << "Index is " << prime_index_number << std::endl;
  std::cout << "Prime is " << prime_number << std::endl;
}
