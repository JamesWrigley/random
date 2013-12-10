#! /usr/bin/python3

# A program that uses the os.walk module to 'walk' through files and folders in
# and including the CWD. Currently can search and delete.

import sys
import os
import re

# Windows compatability
if sys.platform == 'linux':
    slash = "/"
else:
    slash = "\\"

def search_base(keyword_list):

    # Checking for empty keyword input from the user
    if len(keyword_list) == 0:
        print("You must enter a keyword!")
        initiate()

    # Initializes a list that will store the file paths of files to be deleted
    file_match_list = []
    regex_match = re.compile('|'.join(keyword_list), flags=re.I)
#    regex_match = re.compile(re.escape('|'.join(keyword_list)), flags=re.I)

    # Search in and under CWD for files with all keyword in their name, then
    # append to file_match_list
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if regex_match.search(file):
                file_match_list.append(os.path.join(root, file))

    return file_match_list


def search(keyword_list):

    if search_base(keyword_list) == []:
        print("No matches found")
    else:
        for i in search_base(keyword_list): print(i)

def delete_files(keyword_list):

    search_base(keyword_list)

    # Prompts user to confirm delete as long as matches have been found
    if file_match_list == []:
        print("No matches found")
    else:
        print(file_match_list)
        if input("Are you sure you wish to delete these " + str(len(file_match_list)) + " files? [y/N]: ") in "yY":
            print("Coward! " * len(file_match_list))
#            for file in file_match_list:
#                os.remove(file)
        else:
            print("Coward! " * len(file_match_list))




if __name__ == '__main__':

    def initiate():
        option = input("Press 1 if you want to search, 2 if you want to search and delete: ")

        if option == "1":
            keyword_list = str.split(input("Enter a keyword (or two): "))
            search(keyword_list)
        elif option == "2":
            keyword_list = str.split(input("Enter a keyword (or two): "))
            delete_files(keyword_list)
        else:
            print("You must select an option")
            initiate()
    initiate()
