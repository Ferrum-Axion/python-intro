import os
from collections import defaultdict

def count_lines(file_path):
    with open(file_path, 'r') as f:
        return sum(1 for _ in f)


def count_log_levels(file_path):
    counts = {'INFO': 0, 'WARN': 0, 'ERROR': 0}
    with open(file_path, 'r') as f:
        for line in f:
            for level in counts:
                if level in line:
                    counts[level] += 1
    return counts


def count_characters(file_path):
    with open(file_path, 'r') as f:
        return sum(len(line) for line in f)


def get_log_levels(file_path):
    levels = set()
    with open(file_path, 'r') as f:
        for line in f:
            for level in ['INFO', 'WARN', 'ERROR', 'DEBUG']:
                if level in line:
                    levels.add(level)
    return levels


def is_buggy(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if 'WARN' in line or 'ERROR' in line:
                return True
    return False


def list_log_files(logs_dir='logs'):
    log_files = []
    if os.path.isdir(logs_dir):
        for file in os.listdir(logs_dir):
            if file.endswith('.log'):
                log_files.append(os.path.join(logs_dir, file))
    return log_files


def classify_logs(logs_dir='logs'):
    healthy_logs = []
    buggy_logs = []
    for log_file in list_log_files(logs_dir):
        if is_buggy(log_file):
            buggy_logs.append(log_file)
        else:
            healthy_logs.append(log_file)
    return {'healthy_logs': healthy_logs, 'buggy_logs': buggy_logs}


def error_count_per_file(logs_dir='logs'):
    error_counts = {}
    for log_file in list_log_files(logs_dir):
        counts = count_log_levels(log_file)
        error_counts[os.path.basename(log_file)] = counts['ERROR']
    return error_counts


def get_all_log_levels(logs_dir='logs'):
    all_levels = set()
    for log_file in list_log_files(logs_dir):
        all_levels.update(get_log_levels(log_file))
    return all_levels


def generate_summary(logs_dir='logs', output_file='summary.txt'):
    classification = classify_logs(logs_dir)
    all_levels = get_all_log_levels(logs_dir)
    
    with open(output_file, 'w') as f:
        f.write(f"Total log files: {len(list_log_files(logs_dir))}\n")
        f.write(f"Buggy log files: {len(classification['buggy_logs'])}\n")
        if classification['buggy_logs']:
            f.write(f"Buggy log file names: {', '.join(os.path.basename(f) for f in classification['buggy_logs'])}\n")
        f.write(f"All log levels found: {', '.join(sorted(all_levels))}\n")

# Test all the functions

if __name__ == "__main__":
    logs_directory = 'logs'
    summary_file = 'summary.txt'
    
    print("listing log files:")
    print(list_log_files(logs_directory))
    
    print("\nclassifying logs:")
    classification = classify_logs(logs_directory)
    print(classification)
    
    print("\nerror counts per file:")
    print(error_count_per_file(logs_directory))
    
    print("\nall log levels found:")
    print(get_all_log_levels(logs_directory))
    
    print("\nsummary")
    generate_summary(logs_directory, summary_file)