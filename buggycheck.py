
import os
import sys

def checkscriptbugged(filepath):
        with open(filepath) as file:            # open the file and close it after
            for f in file:                      # go via each line   
                f_lower = f.lower()              # no case sensitive
                if "warn" in f_lower or "error" in f_lower:
                   return True
        return False
