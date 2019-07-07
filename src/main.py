###############################################################################
#   Author : Ali Snedden
#   Date   : 3/9/19
#   License: MIT
#
#   Purpose: 
#       This code is intended monitor changes in files hash sums (i.e. corruption)
#       when the modify time hasn't been changed.
#
#   Notes : 
#       1. Walking directory : https://stackoverflow.com/a/3964691/4021436
#       2. Access, Create and Modify Times in OSX are complex
#          a) Using os.stat() is _not_ platform independent, and the python standard
#             doesn't explicitly describe behavior for OSX (see ST_CTIME in 
#             https://docs.python.org/3.6/library/stat.html)          
#          b) Possible way to get (in Python) :
#             i ) Birthtime : https://stackoverflow.com/a/947239/4021436
#             ii)  
#          b) Preferred method would be using OSX's system tools :
#             https://stackoverflow.com/a/34123230/4021436, however I worry that this may
#             be expensive from a runtime POV.
#       3. CL ways of getting Access, Create and Modify times on OSX
#          a) Access, Modify, Change : stat -x somefile
#             i) Change time is permission change
#          b) Creat, Modify          : GetFileInfo somefile
#       4. Evidently copying a file (cp file1 file2) inherits the modification
#          time of file1 as the creation time of file2
#       
###############################################################################
import time
import numpy as np
import sys
import os
import platform
from error import exit_with_error

def print_help(ExitCode):
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
    """
    sys.stderr.write("./src/main.py /path/to/dir\n"
                     "    /absolute/path/to/dir: Absolute Path of dir to compare\n"
                     "\nTo run locally, with all correctly installed packages run\n"
                     "     source ~/.local/virtualenvs/python3.6/bin/activate\n")
    sys.exit(ExitCode)



def main():
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
    """
    if(sys.version_info[0] < 3):
        exit_with_error("ERROR!!! Runs with python3, NOT {}\n".format(sys.argv[0]))
    if(len(sys.argv) == 2 and ("--h" in sys.argv[1] or "-h" in sys.argv[1])):
        print_help(ExitCode=0)
    elif(len(sys.argv) != 2):
        print_help(ExitCode=1)
    path=sys.argv[1]    # Path to search
        
    # Master loop
    for root, dirL, fileL in os.walk(path):
        for f in fileL:
            if(platform.system() == "Darwin"):
                print(os.path.join(root, f))
            else:
                exit_with_error("ERROR!!! {} is an unsupported platform".format(
                                platform.system()))
    

    


if __name__ == "__main__":
    main()

