// Counts the duplicates from the users input

#include <iostream>

int main()
{
    int current_value = 0;
    int value = 0;

    if (std::cin >> current_value) {
	int count = 1;
	while (std::cin >> value) {
	    if (value == current_value)
		++count;
	    else {
		std::cout << current_value << " occurs " << count << " times " << std::endl;
		current_value = value;
		count = 1;
	    }
	}
	std::cout << current_value << " occurs " << count << " times " << std::endl;
    }
    return 0;
}
