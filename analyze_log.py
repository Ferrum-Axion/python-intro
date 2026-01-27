import os
import sys

file = sys.argv[1]

filepath = os.path.join("./logs", file)

def get_number_of_lines(filepath):
    counter = 0
    with open(filepath) as file:
        for l in file:
            counter += 1
    return counter

def get_number_of_chars(filepath):
    counter = 0
    with open(filepath) as file:
        for l in file:
            counter += len(l)
    return counter

def get_number_of_log_items_by_type(filepath):
    log_item_types = {
    "info": 0, 
    "error": 0, 
    "warn": 0,
    "log": 0,
    "detail": 0,
    "fatal": 0,
    "statement": 0,
    }
    with open(filepath) as file:
        for l in file:
            ll = l.lower()
            if "info" in ll:
                log_item_types["info"] += 1
            if "error" in ll:
                log_item_types["error"] += 1
            if "warn" in ll:
                log_item_types["warn"] += 1
            if "log" in ll:
                log_item_types["log"] += 1
            if "detail" in ll:
                log_item_types["detail"] += 1
            if "fatal" in ll:
                log_item_types["fatal"] += 1
            if "statement" in ll:
                log_item_types["statement"] += 1
        return log_item_types

def get_unique_log_item_type(filepath):
    types = set()
    with open(filepath) as file:
        for l in file:
            ll = l.lower()
            if "info" in ll:
                types.add("info")
            if "error" in ll:
                types.add("error")
            if "warn" in ll:
                types.add("warn")
            if "log" in ll:
                types.add("log")
            if "detail" in ll:
                types.add("detail")
            if "fatal" in ll:
                types.add("fatal")
            if "statement" in ll:
                types.add("statement")
        return types

def is_buggy_log(filepath):
    with open(filepath) as file:
        for l in file:
            ll = l.lower()
            if "error" in ll or "warn" in ll or "fatal" in ll:
                return True
        return False

if __name__ == "__main__":
    print("number of lines: " + str(get_number_of_lines(filepath)))
    print("number of log items by type: " + str(get_number_of_log_items_by_type(filepath)))
    print("number of characters: " + str(get_number_of_chars(filepath)))
    print("unique log item types: " + str(get_unique_log_item_type(filepath)))
    print("is buggy log: " + str(is_buggy_log(filepath)))


