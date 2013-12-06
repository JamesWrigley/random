// Add all the numbers in the stream of 0 to a number (10 in this case)

#include <iostream>

int sum = 0;

int main()
{
    for (int val = 50; val <= 100; ++val)
	sum += val;

    std::cout << "Sum of 50 to 100 inclusive is " << sum << std::endl;

    return 0;
}
