#! /usr/bin/python3

# A program that uses the os.walk module to 'walk' through files and folders in
# and including the CWD. Currently can search and delete.

import sys
import os

def search_base(keyword_list):
    # Initializes a list that will store the file paths of files to be deleted
    file_match_list = []

    # Search in and under CWD for files with all keyword in their name, then
    # append to file_match_list
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if all(i in file for i in keyword_list):
                file_match_list.append(os.path.join(root, file))

    return file_match_list


def search(keyword_list):
    search_result = search_base(keyword_list)

    if search_result == []:
        print("No matches found")
    else:
        for i in search_result: print(i)

def delete_files(keyword_list):
    file_match_list = search_base(keyword_list)
    
    # Prompts user to confirm delete as long as matches have been found
    if file_match_list == []:
        print("No matches found")
    else:
        for i in file_match_list: print(i)
        user_choice = input("Are you sure you wish to delete these " + str(len(file_match_list)) + " files? [y/N]: ")

        if user_choice in "yY":
            for file in file_match_list:
                os.remove(file)
            print(str(len(file_match_list)) + " files deleted")
        elif user_choice in "nN":
            print("No files deleted")



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
            
