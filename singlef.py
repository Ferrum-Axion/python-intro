
import os
import sys



# check number of lines
def get_lines_sum(filepath):
    count=0
    with open(filepath) as file:    # open the file and close it after
        for f in file:              # go via each line
            count+=1                # add to counter
    return count


# check for info, warning, error in lines and count
def checkinlines(filepath):
    sumdict = {"info":0, "warn":0, "error":0}
    dictlist = list(sumdict.keys())
    with open(filepath) as file:            # open the file and close it after
        for f in file:                      # go via each line   
           f_lower = f.lower()              # no case sensitive 
           if dictlist[0] in f_lower:
               sumdict[dictlist[0]] +=1
           if dictlist[1] in f_lower:
               sumdict[dictlist[1]] +=1  
           if dictlist[2] in f_lower:
               sumdict[dictlist[2]] +=1                         
    return sumdict


def totalcharcheck(filepath):
    totalc = 0
    with open(filepath) as file:            # open the file and close it after
        for f in file:                      # go via each line 
          totalc +=len(f)
    return totalc


def checkloglevels(sumdict):
    loglevel = []
    for l in sumdict:
        if sumdict[l] > 0:
            loglevel.append(l)
    return loglevel

def checkscriptbugged(sumdict):
    if 'warn' in sumdict and sumdict['warn'] > 0:
       return True
    if 'error' in sumdict and sumdict['error'] > 0:
       return True
    return False


###   main start  ###

# get the file name (arg=1), set the path to logs/filename
file = sys.argv[1]
filepath = os.path.join("./logs", file)

# 1. send file name to function to check and return number of lines and print it
linecount = get_lines_sum(filepath)
print(f"1. Line Count in {file} is {linecount}")   

# 2. check for info, warning, error in file and return as dictionary
sumdict = checkinlines(filepath)    
print(f"2. Summary dictionary is: {sumdict}")

# 3. cacluate total numbers in log
totalchar = totalcharcheck(filepath)
print(f"3. Total characters in file is: {totalchar}")

# 4. return log level in file without duplicates
loglevels = checkloglevels(sumdict)
print(f"4. Log levels in log are: {loglevels}")

# 5. check if warning or error and if so return true/flase
bugornot = checkscriptbugged(sumdict)
if bugornot:     
   print(f"5. script is bugged")
else:
   print(f"5. script is not bugged")


