#! /usr/bin/python3
# A WIP program to time stuff

import time

def timer(value):
    current_time = round(time.time(), 2)
    end_time = current_time + value

    while current_time <= end_time:
        time.sleep(1)
        print("Foo")
        current_time = current_time + 1
        
    print("Done")

val = float(input("Enter number: "))
timer(val)
