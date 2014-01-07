// Simple program that adds 2 user-inputted numbers

#include <iostream>

int main()
{
    std::cout << "Enter two numbers:" << std::endl;
    int v1 = 0;
    int v2 = 0;
    std::cin >> v1 >> v2;
    std::cout << std::endl << "The sum of " << std::endl 
	      << v1 << std::endl 
	      << "and" << std::endl 
	      << v2 << std::endl 
	      << "is " << v1 + v2 << std::endl;

    return 0;
}
