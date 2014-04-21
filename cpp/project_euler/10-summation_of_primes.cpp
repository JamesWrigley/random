// Problem 10 from Project Euler
// http://projecteuler.net/problem=10

#include <cmath>
#include <vector>
#include <iostream>

int main()
{
  std::vector<int> number_list(2000000);
  std::iota(number_list.begin(), number_list.end(), 2);

  for (unsigned int n = 0; n <= sqrt(10); n++)
    {
      for (unsigned int p = n + 1; p <= number_list.size(); p++)
        {
          if (fmod(number_list[p], number_list[n]) != 0
        }
    }
}
