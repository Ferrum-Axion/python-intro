import os
import sys

def get_number_of_lines(filepath):
    counter=0
    with open(filepath) as file:
        for f in file:
            print(f)
            counter +=1
    return counter