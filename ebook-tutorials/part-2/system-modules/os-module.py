# os module functions and usages

import os

# returns a dictionary including environmental variables paths
os.environ

# to run program, excepted a string command line 
os.system("python start.py")

# returns process ID (a unique system-defined identifier
# for running program)
os.getpid()

# returns current directory
os.getcwd()

# change current directory
#os.chdir(r"path")

# open a file with default program
#os.popen(r"filepath")

# Execute an executable path with arguments, replacing current process.
#os.execv(r"filepath", (args))

