#! /usr/bin/python3
import string

def shift_n_letters(letter, steps):
    letter_index = string.ascii_lowercase.index(letter) + 1 + steps
    print()

if __name__ == "__main__":
    user_input = list(input("Enter a letter and a number of steps: ").split())
    if len(user_input) == 2:
        shift_n_letters(user_input[0], int(user_input[1]))
    else:
        print("Wrong number of arguments!")
