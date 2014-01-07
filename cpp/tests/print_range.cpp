// Prints all the numbers between the 2 user inputted integers

#include <iostream>

int val1 = 0;
int val2 = 0;

int main()
{
    std::cout << "Enter 2 numbers, the range between them will be printed: ";
    std::cin >> val1 >> val2;

    if (val1 < val2) {
        while (val1 <= val2) {
            std::cout << val1 << std::endl;
            ++val1; }
    }
    else if (val1 > val2) {
        while (val1 >= val2) {
            std::cout << val1 << std::endl;
            --val1;
        }
    }
}

