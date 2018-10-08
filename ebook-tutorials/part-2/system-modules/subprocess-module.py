# subprocess module functions and usages

import subprocess

# roughly like os.system()
subprocess.call("python start.py")

# built-in shell cmd
subprocess.call('cmd /C "type start.py"')

# alternative for built-ins
subprocess.call("type start.py", shell=True)
