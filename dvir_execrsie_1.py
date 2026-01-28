import os
import sys
#1
def number_of_lines(filepath):
    l = 0
    with open (filepath) as f:
        for line in f:
         l += 1
    return l
#2
def get_number_of_log_items_by_type(filepath):
    log_item_types = {
        "INFO": 0, 
        "ERROR": 0, 
        "WARN": 0,
    }
    with open(filepath) as file:
        for l in file:
            if "INFO" in file:
                log_item_types["INFO"] += 1
            if "ERROR" in file:
                log_item_types["ERROR"] += 1
            if "WARN" in file:
                log_item_types["WARN"] += 1
    return log_item_types
#3
def get_number_of_characters(filepath):
    counter = 0
    with open(filepath) as file:
        for l in file:
            counter += len(l)
    return counter
#4
def get_unique_levels(filepath):
    unique_levels = set()
    options = ["INFO", "WARN", "ERROR", "DEBUG", "CRITICAL"]
    with open(filepath, 'r') as file:
        for line in file:
            for level in options:
                if level in line:
                    unique_levels.add(level)
    return list(unique_levels)
#5
def is_bugy(filepath):
    with open(filepath) as file:
        for l in file:
            if "ERROR" in l or "WARN" in l or "FATAL" in l:
             return True
        return False
#6



