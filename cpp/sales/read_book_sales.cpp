// Reads a bunch of book sales transactions and prints them

#include <fstream>
#include <iostream>
#include "Sales_item.h"

int main(int argc, char *argv[])
{
    std::ifstream transaction_file;

    if (argc != 2)
        std::cout << "You must pass a transaction file to the program" << std::endl;
    else {
        transaction_file.open(argv[1]);
        std::string line;
        while (std::getline(transaction_file, line))
            {
                std::cout << line << std::endl;
            }
    }
}

