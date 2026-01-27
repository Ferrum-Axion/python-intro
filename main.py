import os

def number1(log):
    try:
        with open(log) as logpath1:
            return len(logpath1.readlines())
    except:
        print("this file doesn't exist")

        
def number2(log):
        result = {"count": 0}
        count = 0

        # Attempt to open the file and handle potential errors
        try:
            with open(log) as logpath2:
                # Read through each line in the file and count specific keywords
                for line in logpath2:
                    if "ERROR" in line or "INFO" in line or "WARN" in line:
                        count += 1
                result["count"] = count
        except FileNotFoundError:
            print(f"Error: The file {log} was not found.")
        return result

def number3(log):
    try:
        with open(log) as logpath3:
            # Read the whole file and count all characters
            return len(logpath3.read())
    except FileNotFoundError:
        print(f"Error: The file {log} was not found.")
        return 0


def number4(log):
    levels_found = set()
    
    try:
        with open(log) as logpath4:
            for line in logpath4:
                if "INFO" in line:
                    levels_found.add("INFO")
                if "WARN" in line:
                    levels_found.add("WARN")
                if "ERROR" in line:
                    levels_found.add("ERROR")
    except FileNotFoundError:
        print(f"Error: The file {log} was not found.")

    return levels_found


def number5(log):
    try:
        with open(log) as logpath5:
            for line in logpath5:
                if "WARN" in line or "ERROR" in line:
                    return True
    except FileNotFoundError:
        print(f"Error: The file {log} was not found.")
        return False

    return False

