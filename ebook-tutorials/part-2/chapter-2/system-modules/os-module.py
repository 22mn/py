# os module functions and usages

import os

path = r"start.py"

# returns a dictionary including environmental variables paths
os.environ

# spawns a new child process on Unix-like systems
#os.fork

# communicates between programs
os.pipe

# starts new programs
os.execlp

# starts new programs with lower-level
os.spawnv

# opens a low-level descriptor-based file
os.open

# creates a new named pipe
#os.mkfifo

# fetches low-level file information
os.start

# built-in shell cmd
os.popen("dir /B *.py")

# to run program, excepted a string command line 
# or "type start.py"
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

# creates a new directory
os.mkdir

# deletes a file by its pathname
os.remove

# entire directory tree
os.walk

# change current directory
#os.chdir(r"directory")

# absolute path, empty string means the cwd
# "." relative path, ".." backward directory
os.path.abspath(""), os.path.abspath(".")

# open a file with default program
os.popen(path)
os.startfile(path)

# Execute an executable path with arguments, replacing current process.
#os.execv(r"filepath", (args))

