// Prints all the numbers down to zero from val

#include <iostream>

int val = 10;

int main()
{
    while (val >= 0) {
	std::cout << val << std::endl;
	--val;
    }
}
