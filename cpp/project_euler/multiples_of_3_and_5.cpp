// Problem 1 from projecteuler.net/problems

#include <iostream>

int main()
{
  int sum = 0;

  for (unsigned int i = 0; i < 1000; i++)
    {
      if (i % 3 == 0 || i % 5 == 0)
        {
          sum += i;
        }
    }
  std::cout << "The sum of all natural numbers less than 1000 that are divisible by "
       << "3 or 5 is " << sum << std::endl;
}
