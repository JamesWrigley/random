// Problem 2 from Project Euler
// http://projecteuler.net/problem=2

#include <iostream>

int main()
{
  int sum = 0;
  int n1 = 0;
  int n2 = 1;

  while (n1 + n2 < 4000000)
    {
      int n3 = n1 + n2;
      if (n3 % 2 == 0)
        {
          sum += n3;
        }
      n1 = n2;
      n2 = n3;
    }

  std::cout << "The sum of all even fibonacci numbers up to 4 million is " << sum << std::endl;
}
