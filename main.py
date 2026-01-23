import os
import sys

log_file = sys.argv[1]
file_path = os.path.join('logs', log_file)
print(file_path)

def count_lines(file_path):
    count = 0
    with open(file_path) as f:
        for line in f:
            count += 1
    return count

lines = count_lines(file_path)
print("Number of lines:", lines)

def filter_logs(file_path):
    log_types = {'error': 0, 'info': 0, 'warn': 0}
    with open(file_path) as f:
        for line in f:
            line = line.lower()
            if 'error' in line:
                log_types['error'] += 1
            elif 'info' in line:
                log_types['info'] += 1
            elif 'warn' in line:
                log_types['warn'] += 1
    return log_types

log_types = filter_logs(file_path)
print("Log types:", log_types)

def char_count(file_path):
    count = 0
    with open(file_path) as f:
        for line in f:
            line_char = len(line)
            count += line_char
    return count

char_count = char_count(file_path)
print("Character count:", char_count)

def collect_log_levels(file_path):
    levels = []
    with open(file_path) as f:
        for line in f:
            line = line.lower()
            if 'error' in line:
                levels.append('error')
            elif 'info' in line:
                levels.append('info')
            elif 'warn' in line:
                levels.append('warn')
            elif 'fatal' in line:
                levels.append('fatal')
            elif 'crit' in line:
                levels.append('crit')
    return set(levels)

log_levels = collect_log_levels(file_path)
print("Log levels found:", log_levels)

def check_buggy(log_levels):
    if "error" in log_levels or "warn" in log_levels:
        return True
    else:
        return False
    
is_buggy = check_buggy(log_levels)
print("Is the log buggy?", is_buggy)