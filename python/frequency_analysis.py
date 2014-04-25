#! /usr/bin/python3
import string

def freq_analysis(message):
    freq_list = []

    if len(message) == 0:
        print("You must enter more than one letter!")
        quit()

    for letter in string.ascii_lowercase:
        freq_list.append(message.count(letter) / len(message))

    print(freq_list)

if __name__ == "__main__":
    freq_analysis(input("Enter message: "))
