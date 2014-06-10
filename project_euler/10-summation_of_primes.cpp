// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <cmath>
#include <array>
#include <iostream>

int main()
{
  const unsigned int size = 2000000;
  long long primes_sum = 0;
  std::array<bool, size> bool_array;
  bool_array.fill(true);
  bool_array[0] = false;

  // The Sieve of Eratosthenes
  for (unsigned int number = 0; number < size; ++number)
    {
      if (bool_array[number])
        {
          primes_sum += number + 1;
          unsigned int multiplicand = 2;

          // Increment 'number' by 1 to offset the zero numbering
          unsigned int n_product = multiplicand * (number + 1);

          while (n_product <= size)
            {
              bool_array[n_product - 1] = false;
              ++multiplicand;
              n_product = multiplicand * (number + 1);
            }
        }
    }

  std::cout << primes_sum << std::endl;
}
