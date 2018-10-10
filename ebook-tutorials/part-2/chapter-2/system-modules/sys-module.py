# sys module functions and usages
import sys

# return list of path from PYTHONPATH(Enviromental Variables)
sys.path

# add new path to PYTHONPATH
sys.path.append(r"newpath")

# pre-loaded modules returns a dictionary 
# {"mod-name":"mod-path info",..:..,}
sys.modules


# exception details when exception trigger
# return a tuple of (ErrorType, ErrorMessage, Traceback-Info)
sys.exc_info()

