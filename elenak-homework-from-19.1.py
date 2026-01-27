import os

# 1: Total number of lines (Line 3)
def count_total_lines(filepath):
    with open(filepath, 'r') as file:
        return len(file.readlines())

# 2: Count INFO, WARN, and ERROR
def count_log_levels(filepath):
    counts = {"INFO": 0, "WARN": 0, "ERROR": 0}
    with open(filepath, 'r') as file:
        for line in file:
            for level in counts.keys():
                if level in line:
                    counts[level] += 1
    return counts

# 3: Total number of characters 
def count_total_chars(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        return len(content)

# 4: Collect unique log levels 
def get_unique_levels(filepath):
    levels = set()
    possible_levels = ["INFO", "WARN", "ERROR", "DEBUG", "CRITICAL"]
    with open(filepath, 'r') as file:
        for line in file:
            for level in possible_levels:
                if level in line:
                    levels.add(level)
    return list(levels)

# 5: Check if file is "buggy" 
def is_buggy(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
        return "WARN" in content or "ERROR" in content