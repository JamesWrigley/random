// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <vector>
#include <iostream>
#include <algorithm>

int main()
{
  std::vector<unsigned int> number_list(10000);
  std::iota(number_list.begin(), number_list.end(), 2);

  for (unsigned int n = 0; n <= sqrt(number_list.size()); n++)
    {
      unsigned int n_product = 0;

      // While the product is less than the greatest element of number_list
      while (n_product < number_list.back())
        {
          for (unsigned int multiplicand = 2; multiplicand < number_list.back(); ++multiplicand)
            {
              n_product = number_list[n] * multiplicand;
              // Get rid of all occurences of n_product in number_list
              number_list.erase(std::remove(number_list.begin(), number_list.end(), n_product), number_list.end());
            }
        }
    }
}
