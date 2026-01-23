Working on a single log file

1 - Write a function that receives a path to a log file and returns the total number of lines in the file.

2 - Write a function that counts how many log lines contain INFO, WARN, and ERROR and returns the results as a dictionary.

3 - Write a function that calculates and returns the total number of characters in the log file.

4- Write a function that collects all log levels that appear in the file and returns them without duplicates.

5- Write a function that checks whether a log file is buggy (contains WARN or ERROR) and returns True or False.

Working on the entire logs/ directory

6 - Write a function that iterates over all log files in the logs directory and returns a list of their paths.

7 - Write a function that uses the functions from analyze_log.py to classify log files into healthy_logs and buggy_logs.

8 - Write a function that builds a dictionary where each log file name is mapped to the number of ERROR lines it contains.

9 - Write a function that collects all log levels that appear across all log files and returns the unique set of levels.

10 - Write a function that generates a summary.txt file containing the total number of log files, the number and names of buggy log files, and all log levels found across the logs.