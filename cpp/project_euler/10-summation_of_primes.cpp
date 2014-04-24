// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <vector>
#include <iostream>
#include <unordered_map>

int main()
{
  std::unordered_map<unsigned long long, bool> number_map;
  unsigned long long size = 2000000;
  unsigned long long iter = 2;
  // Populate the map
  while (iter <= size)
    {
      number_map[iter] = true;
      ++iter;
    }

  // The Sieve of Eratosthenes
  for (auto keyValue : number_map)
    {
      if (keyValue.second)
        {
          unsigned long long multiplicand = 2;
          unsigned long long n_product = multiplicand * keyValue.first;

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
