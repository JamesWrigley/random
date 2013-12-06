#! /usr/bin/python3

import sys
import os

def delete_files(keyword):
    '''
    The find function
    '''

    if len(keyword) == 1:
        print("You must enter a keyword!")
        quit()
    else:
        keyword = keyword[1]

    file_match_list = []

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if keyword in file:
                print(root + "/" + file)
                file_match_list.append(root + "/" + file)

    if input("Are you sure you wish to delete these " + str(len(file_match_list)) + " files? [y/N]: ") in "ynYN":
        print("Now to test!")
    else:
        print
#    for file in file_match_list:
#        os.remove(file)

if __name__ == '__main__':
    delete_files(sys.argv)
