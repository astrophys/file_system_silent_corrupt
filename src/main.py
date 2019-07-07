###############################################################################
#   Author : Ali Snedden
#   Date   : 3/9/19
#
#   Purpose: 
#
#   Notes : 
#
#
#
###############################################################################
import time
import numpy as np
import sys
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
                     "    /path/to/dir: Path of dir to compare\n"
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
    elif(len(sys.argv) != 5):
        print_help(ExitCode=1)
        
    
    

    


if __name__ == "__main__":
    main()

