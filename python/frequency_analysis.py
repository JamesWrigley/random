#! /usr/bin/python3

def freq_analysis(message):
    freq_list = []
    processed_letters = []

    for letter in message:
        if letter not in processed_letters:
            freq_list.append(message.count(letter) / len(message))
            processed_letters.append(letter)

    print(freq_list)

if __name__ == "__main__":
    freq_analysis(input("Enter message: "))
