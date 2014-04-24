// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <vector>
#include <iostream>
#include <unordered_map>

int main()
{
  std::unordered_map<unsigned int, bool> number_map;
  unsigned int size = 2000000;
  // Populate the map
  for (unsigned int iter = 2; iter <= size; ++iter)
    {
      number_map[iter] = true;
    }

  // The Sieve of Eratosthenes
  for (auto keyValue : number_map)
    {
      if (keyValue.second)
        {
          unsigned int multiplicand = 2;
          unsigned int n_product = multiplicand * keyValue.first;

          // While the product is less than the greatest element of number_map
          while (n_product <= size)
            {
              number_map[n_product] = false;
              ++multiplicand;
              n_product = multiplicand * keyValue.first;
            }
        }
    }

  // Add all the primes together
  unsigned long long primes_sum = 0;
  for (auto keyValue : number_map)
    {
      if (keyValue.second)
        {
          primes_sum += keyValue.first;
        }
    }
  std::cout << primes_sum << std::endl;
}
