#! /usr/bin/python3

import sys
import os

if sys.platform == 'linux':
    slash = "/"
else:
    slash = "\\"

def delete_files(keyword):

    if len(keyword) == 1:
        print("You must enter a keyword!")
        quit()
    else:
        keyword = keyword[1]

    file_match_list = []

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if keyword in file:
                print(root + slash + file)
                file_match_list.append(root + slash + file)

    if file_match_list == []:
        print("No matches found")
    else:
        if input("Are you sure you wish to delete these " + str(len(file_match_list)) + " files? [y/N]: ") in "yY":
            for file in file_match_list:
                os.remove(file)
        else:
            print("Coward!" * len(file_match_list))

if __name__ == '__main__':
    delete_files(sys.argv) 
