# sys module functions and usages
import sys

# a list of command line argvs
sys.argv

# return list of path from PYTHONPATH(Enviromental Variables)
sys.path

# add new path to PYTHONPATH
sys.path.append(r"newpath")

# pre-loaded modules returns a dictionary 
# {"mod-name":"mod-path info",..:..,}
sys.modules

# get absolute executable path
sys.executable

# exception details when exception trigger
# return a tuple of (ErrorType, ErrorMessage, Traceback-Info)
sys.exc_info()

# customize display
x = 33
def my_display(x):
	print("My x value: ",x)

sys.displayhook = my_display
# call x from interactive
