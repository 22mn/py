"""connect two programs"""

# shell command
python writer.py | reader.py


# subprocess
from subprocess import Popen, PIPE
p1 = Popen("python writer.py", stdout=PIPE)
p2 = Popen("python reader.py", stdin=p1.stdout, stdout=PIPE)
output = p2.communicate()[0]
print(output)

# os
import os
p1 = os.popen("python writer.py", "r")
p2 = os.popen("python reader.py", "w")
p2.write(p1.read())
x = p2.close()
print(x)