// Problem 9 from Project Euler
// http://projecteuler.net/problem=9

#include <array>
#include <numeric>
#include <iostream>

int main()
{
  std::array<int, 1000> range;
  std::iota(range.begin(), range.end(), 1);

  std::cout << range[999] << std::endl;
}
