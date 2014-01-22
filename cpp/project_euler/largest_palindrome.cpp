// Problem 3 from Project Euler
// http://projecteuler.net/problem=3

#include <algorithm>
#include <iostream>

int reverse_number (int number)
{
  std::string int_as_str = std::to_string(number);
  std::reverse(int_as_str.begin(), int_as_str.end());
  int reversed_number = std::stoi(int_as_str);
  return reversed_number;
}

int main()
{
  int largest_palindrome;
  int max_number = 1000;
  int min_number = 100;

  for (int n1 = min_number; n1 < max_number; n1++)
    {
      //      std::cout << "Got to n1 for " << n1 << std::endl;
      for (int n2 = min_number; n2 < n1; n2++)
        {
          //          std::cout << "Got to n2 for " << n2 << std::endl;
          int product = n1 * n2;
          if (reverse_number(product) == product)
            {
              if (largest_palindrome < product)
                {
                  largest_palindrome = product;
                }
              std::cout << largest_palindrome << std::endl;
            }
        }
    }
  std::cout << largest_palindrome << std::endl;
}
