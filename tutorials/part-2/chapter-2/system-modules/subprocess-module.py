# subprocess module functions and usages

import subprocess

# roughly like os.system()
subprocess.call("python start.py")

# built-in shell cmd
subprocess.call('cmd /C "type start.py"')

# alternative for built-ins
#subprocess.call("type start.py", shell=True)

# run the command to completion and receive its standard output
pipe = subprocess.Popen("python start.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output and error(if occur)
output, error = pipe.communicate()
# exit status
pipe.returncode