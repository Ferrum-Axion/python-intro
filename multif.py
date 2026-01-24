
import os
import sys

from buggycheck import checkscriptbugged

def getfilepath(foldertocheck):
    pathlist = []
    for filename in os.listdir(foldertocheck):
        path = os.path.join(foldertocheck, filename)
        pathlist.append(path)
    return pathlist


def checkbuggy(filespath):
    buggycheckdict = {}
    for filename in filespath:
        answer = checkscriptbugged(filename)
        justfilename = filename.split("/")[-1]
        buggycheckdict[justfilename] = answer
    return buggycheckdict


def errornumber(filespath):
    errornumberdict = {}
    for filename in filespath:                 # for each file in location
        with open(filename) as file:           # open the file and close it after
           count=0                         
           for f in file:                  # for each line
               f_lower = f.lower()             # no case sensitive 
               if "error" in f_lower:
                  count+=1
        justfilename = filename.split("/")[-1]
        errornumberdict[justfilename] = count
    return errornumberdict


def checkloglevels(sumdict):
    lvlarray = ["info", "warn", "error"]
    fileslvl = set()
    for filename in filespath:                 # for each file in location
        with open(filename) as file:           # open the file and close it after
           for f in file:                  # for each line
               f_lower = f.lower()             # no case sensitive 
               if "error" in f_lower:
                  fileslvl.add("error")
               if "error" in f_lower:
                  fileslvl.add("warn")  
               if "error" in f_lower:
                  fileslvl.add("info")
    return fileslvl 


def createsummaryfile(filespath, buggyornot, numberoferror):
    with open("summary.txt", "w") as f:
         f.write(f"1. Number of logs in folder: {len(filespath)} \n")
         # now to check via all the buggyornot dictionary for True values and return the keys
         truenames = []
         for key, value in buggyornot.items():
             if value is True:
                truenames.append(key) 
         f.write(f"2. Buggy log names: {truenames} \n")
         f.write(f"3. Log levels found in logs: {numberoferror} \n")
    return "done"


###   main start  ###

# get the folder name (arg=1), set the path to the folder entered
folder = sys.argv[1]
foldertocheck = os.path.join(folder)

# 6. send file name to function to check and return number of lines and print it
filespath = getfilepath(foldertocheck)
print(f"6. the files paths are: \n {filespath} \n") 

# 7. send file name to function to check and return number of lines and print it
buggyornot = checkbuggy(filespath)
print(f"7. list of buggy/not buggy files (buggy=True, not buggy=False): \n {buggyornot} \n") 

# 8. check and return each file number of error lines in it as dictionary
numberoferror = errornumber(filespath)
print(f"8. each log and number of error lines in it: \n {numberoferror} \n") 

# 9. check and return log levels sum for all files
numberoferror = checkloglevels(filespath)
print(f"9. log levels obsereved in all tests: \n {numberoferror} \n") 

# 10. create a txt file to return: number of logs, which logs are bugged, and log lvl of all logs.
createsummaryfile(filespath, buggyornot, numberoferror)
print("Summary file named summary.txt was created")