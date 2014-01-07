// Sums an arbitrary number of inputs from the user

#include <iostream>
int main()
{
    int sum = 0;
    int value = 0;

    while (std::cin >> value)
    sum += value;
    std::cout << "Sum of values is: " << sum << std::endl;
    return 0;
}
