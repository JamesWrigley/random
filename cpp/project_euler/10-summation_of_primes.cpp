// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <vector>
#include <iostream>
#include <algorithm>

int main()
{
  std::vector<unsigned int> number_list(9999);
  std::iota(number_list.begin(), number_list.end(), 2); // Populate the vector

  unsigned int erasion_count = 0;

  for (unsigned int n = 0; n <= sqrt(number_list.size()); ++n)
    {
      unsigned int n_product = 0;

      // While the product is less than the greatest element of number_list
      while (n_product < number_list.back())
        {
          for (unsigned int multiplicand = 2; multiplicand < number_list.back(); ++multiplicand)
            {
              n_product = number_list[n] * multiplicand;
              // Get rid of all occurences of n_product in number_list
              // This also seems to be the bottleneck
              number_list.erase(std::remove(number_list.begin(), number_list.end(), n_product), number_list.end());
              ++erasion_count;
            }
        }
    }

  unsigned int primes_sum = 0;
  for (unsigned int prime : number_list)
    {
      primes_sum += prime;
    }
  std::cout << primes_sum << std::endl;
  std::cout << "Number of calls to std::erase: " << erasion_count << std::endl;
}
