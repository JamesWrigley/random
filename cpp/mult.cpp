// Takes 2 numbers from the user and multiplies them

#include <iostream>

int main()
{
    int v1 = 0;
    int v2 = 0;

    std::cout << "Enter two numbers to be multiplied: ";
    std::cin >> v1 >> v2;
    std::cout << v1 << " multiplied by " << v2 << " is " << v1 * v2 << std::endl;

    return 0;
}
