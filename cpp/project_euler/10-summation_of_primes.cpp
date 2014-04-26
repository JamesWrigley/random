// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <array>
#include <iostream>

int main()
{
  const unsigned int size = 2000000;
  std::array<bool, size> bool_array;
  bool_array.fill(true);
  // We set the numbers 1 and 2 to false here, it makes it a bit simpler
  bool_array[0] = false; bool_array[1] = false;

  // The Sieve of Eratosthenes
  for (unsigned int number = 0; number < size; ++number)
    {
      if (bool_array[number])
        {
          unsigned int multiplicand = 2;
          // We increment 'number' by 1 to offset the zero indexing
          unsigned int n_product = multiplicand * (number + 1);

          // While the product is less than the upper bound
          while (n_product <= size)
            {
              bool_array[n_product - 1] = false;
              ++multiplicand;
              n_product = multiplicand * (number + 1);
            }
        }
    }

  // Add all the primes together
  unsigned long long primes_sum = 0;
  for (unsigned int i = 0; i < size; ++i)
    {
      if (bool_array[i])
        {
          primes_sum += i + 1;
        }
    }
  // I have no idea why this is neccessary
  primes_sum -= 2;

  std::cout << primes_sum << std::endl;
}
