#! /usr/bin/python3
# http://www.pasteall.org/51082/python


import string

def shift_n_letters(letter, steps):
    letter_index = 0

    if (string.ascii_lowercase.index(letter) + steps) <= 26:
        letter_index = string.ascii_lowercase.index(letter) + steps
        print(string.ascii_lowercase[letter_index])
    else:
        letter_index = (string.ascii_lowercase.index(letter) + steps) % 26
        print(string.ascii_lowercase[letter_index])

if __name__ == "__main__":
    user_input = list(input("Enter a letter and a number of steps: ").split())
    if len(user_input) == 2:
        shift_n_letters(user_input[0], int(user_input[1]))
    else:
        print("Wrong number of arguments!")
