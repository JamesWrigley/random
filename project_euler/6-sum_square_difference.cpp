// Problem 6 from Project Euler
// http://projecteuler.net/problem=6

#include <iostream>
#include <math.h>

int main()
{
  int max_number = 100;
  int sum_of_squares = 0;
  int square_of_sum = pow(((max_number * (max_number + 1)) / 2), 2);

  for (int i = 1; i <= max_number; i++)
    {
      sum_of_squares += pow(i, 2);
      //      std::cout << sum_of_squares << std::endl;
    }

  std::cout << "The difference is " << square_of_sum - sum_of_squares << std::endl;
}
