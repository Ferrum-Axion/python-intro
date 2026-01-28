import os
import analyze_log

def get_logs_paths() -> list[str]:
    log_files = os.listdir('./logs')
    full_paths = list()
    for file in log_files:
        full_paths.append(os.path.abspath('logs/' + file))
    return full_paths

def get_buggy_logs():
    log_files = get_logs_paths()
    classifications = dict()
    for file in log_files:
        classifications[file] = 'buggy' if analyze_log.is_buggy_log(file) else 'healthy'
    return classifications

def get_number_of_errors_in_logs():
    log_files = get_logs_paths()
    errors = {}
    for file in log_files:
        errors[file] = analyze_log.get_number_of_log_items_by_type(file)['error']
    return errors

def get_unique_log_levels():
    log_files = get_logs_paths()
    levels = set()
    for file in log_files:
        l = analyze_log.get_unique_log_item_type(file)
        for i in l:
            levels.add(i)
    return levels

def get_summary():
    cl = get_buggy_logs()
    summary = {
        "total logs": len(cl),
    }
    buggy_logs = []
    for name, status in cl.items():
        if status == 'buggy':
            buggy_logs.append(name)
    summary['total buggy logs'] = len(buggy_logs)
    summary['buggy logs'] = buggy_logs
    summary['unique log levels'] = get_unique_log_levels()

    out = ""
    for key, value in summary.items():
        out += key + ": " + str(value) + "\n"

    with open('summary.txt', "w") as file:
        file.write(out)

    return out



if __name__ == '__main__':
    print("log files full paths: " + str(get_logs_paths()))
    print("log files classifications: " + str(get_buggy_logs()))
    print("number of errors in log files: " + str(get_number_of_errors_in_logs()))
    print("unique log levels: " + str(get_unique_log_levels()))
    print("summary: \n" + get_summary())