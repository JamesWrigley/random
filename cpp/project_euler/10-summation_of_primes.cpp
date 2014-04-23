// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <iostream>
#include <algorithm>
#include <unordered_map>

int main()
{
  std::unordered_map<unsigned int, bool> number_map;
  unsigned int size = 100;
  unsigned int iter = 2;
  while (iter <= size)
    {
      //      number_map[iter] = true;
      number_map.emplace(iter, true);
      ++iter;
    }

  // The Sieve of Eratosthenes (WIP)
  for (auto keyValue : number_map)
    {
      if (keyValue.second)
        {
          unsigned int n_product = 0;

          // While the product is less than the greatest element of number_map
          for (unsigned int multiplicand = 2; n_product < size; ++multiplicand)
            {
              n_product = keyValue.first * multiplicand;
              number_map[n_product] = false;
            }
        }
    }

  unsigned int primes_sum = 0;
  // for (auto keyValue : number_map)
  //   {
  //     std::cout << keyValue.first << std::endl;
  //   }
  //  std::cout << primes_sum << std::endl;
}
