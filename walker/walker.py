#! /usr/bin/python3

# A program that uses the os.walk module to 'walk' through files and folders in
# and including the CWD. Currently can search and delete.

import sys
import os

# Windows compatability
if sys.platform == 'linux':
    slash = "/"
else:
    slash = "\\"

def delete_files():

    keyword = input("Enter a keyword (or two): ")

    # Checking for empty keyword input from the user
    if len(keyword) == 1:
        print("You must enter a keyword!")
        quit()

    # Initializes a list that will store the file paths of files to be deleted
    file_match_list = []

    # Search in and under CWD for files with all keyword in their name, then
    # append to file_match_list
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if keyword[0] in file and keyword[1] in file:
                print(root + slash + file)
                file_match_list.append(root + slash + file)

    # Prompts user to confirm delete as long as matches have been found
    if file_match_list == []:
        print("No matches found")
    else:
        if input("Are you sure you wish to delete these " + str(len(file_match_list)) + " files? [y/N]: ") in "yY":
            print("Coward! " * len(file_match_list))
#            for file in file_match_list:
#                os.remove(file)
        else:
            print("Coward! " * len(file_match_list))


def search():

    keyword = input("Enter a keyword (or two): ")

    # Checking for empty keyword input from the user
    if len(keyword) == 1:
        print("You must enter a keyword!")
        quit()

    # Search in and under CWD for files with all keyword in their name, then
    # append to file_match_list
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if keyword[0] in file and keyword[1] in file:
                print(root + slash + file)


if __name__ == '__main__':

    option = input("Press 1 if you want to search, 2 if you want to search and delete: ")
    if option == "1":
        search()
    else:
        delete_files()
