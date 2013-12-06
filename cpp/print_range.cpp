// Prints all the numbers between the 2 user inputted integers

#include <iostream>

int val1 = 0;
int val2 = 0;

int main()
{
    std::cout << "Enter 2 numbers, the second larger than the first: ";
    for (std::cin >> val1 >> val2; val2 >= val1; ++val1) {
	std::cout << val1 << std::endl;
    }
}
