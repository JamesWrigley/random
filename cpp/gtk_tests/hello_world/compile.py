#! /usr/bin/python3
# A small script to compile my GTKMM tests while I figure out a proper Makefile

import os
import sys

def main(args):
    if len(args) == 1:
        print("You must pass a source file")
    else:
        print("g++ " + args[1] + " -o " + args[1][:-4] + " `pkg-config gtkmm-3.0 --cflags --libs`")
        os.system("g++ " + args[1] + " -o " + args[1][:-4] + " `pkg-config gtkmm-3.0 --cflags --libs`")

if __name__ == "__main__":
    main(sys.argv)
