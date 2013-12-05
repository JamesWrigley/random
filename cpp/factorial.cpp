// The factorial function

#include <iostream>

int main()
{
    int sum = 0;
    int val = 0;
    std::cout << "Enter a number to be factorialized: ";
    std::cin >> val >> std::endl;
    // Keep executing till the user inputted number is reached
    while (val <= 10) {
	sum += val;
	++val;
    }

    std::cout << "Sum of 1 to 10 inclusive is " << sum << std::endl;

    return 0;
}
