// Add all the numbers in the stream of 0 to a number (10 in this case)

#include <iostream>

int main()
{
    int sum = 0;
    int val = 50;
    // Keep executing till the val is at number
    while (val <= 100) {
	sum += val;
	++val;
    }

    std::cout << "Sum of 50 to 100 inclusive is " << sum << std::endl;

    return 0;
}
