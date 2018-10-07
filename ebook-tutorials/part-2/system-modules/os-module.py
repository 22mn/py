# os module functions and usages

import os

path = r"start.py"

# returns a dictionary including environmental variables paths
os.environ

# to run program, excepted a string command line 
os.system("python start.py")

# returns process ID (a unique system-defined identifier
# for running program)
os.getpid()

# returns current directory
os.getcwd()

# os path and directory characters
os.pathsep, os.sep, os.pardir, os.curdir, os.linesep

# is directory?
os.path.isdir(path) 

# is file?
os.path.isfile(path)

# returns directory name
os.path.dirname(path)

# returns the last item from the path (usually a file)
os.path.basename(path)


# change current directory
#os.chdir(r"path")

# open a file with default program
#os.popen(r"filepath")

# Execute an executable path with arguments, replacing current process.
#os.execv(r"filepath", (args))

