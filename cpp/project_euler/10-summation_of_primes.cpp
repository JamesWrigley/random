// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <array>
#include <iostream>

int main()
{
  const unsigned int size = 10;
  std::array<bool, size> bool_array;
  bool_array.fill(true);

  // The Sieve of Eratosthenes
  for (unsigned int number = 0; number < size; ++number)
    {
      if (bool_array[number])
        {
          unsigned int multiplicand = 2;
          // Add 2 to 'number' because the sieve is meant to start from the number 2
          // and so number will always be 2 less than the intended number
          unsigned int n_product = multiplicand * (number + 2);

          // While the product is less than the upper bound
          while (n_product <= size)
            {
              bool_array[n_product - 1] = false;
              ++multiplicand;
              n_product = multiplicand * (number + 2);
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
          std::cout << i + 2 << std::endl;
        }
    }
  --primes_sum;

  std::cout << primes_sum << std::endl;
}
