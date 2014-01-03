// The factorial program

#include <iostream>

int main()
{
    int number = 0;

    std::cout << "Enter a positive integer: ";
    std::cin >> number;

    if (number == 0)
        std::cout << "Factorial of 0 is 1" << std::endl;
    else {
        float sum = 1;
        int i = 1;
        while (i <= number) {
            sum *= i;
            ++i;
        }
        std::cout << "Factorial of " << number << " is " << sum << std::endl;
    }
    return 0;
}
