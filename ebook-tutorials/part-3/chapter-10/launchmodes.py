
# rewrite launchmodes.py

import sys, os
pyfile = (sys.platform[:3] == "win" and "python.exe") or "python"
pypath = sys.executable

def fixWindowsPath(cmdline):
	splitline = cmdline.lstrip().split(" ")
	fixedpath = os.path.normpath(splitline[0])
	return " ".join([fixedpath] + splitline[1:])

class LaunchMode:
	def __init__(self, label, command):
		self.what = label
		self.where = command

	def __call__(self):
		self.announce(self.what)
		self.run(self.where)

	def announce(self, text):
		print(text)

	def run(self, cmdline):
		assert False, "run must bd defined"

class System(LaunchMode):
	"""
	run Python script named in shell command line
	caveat: may block caller, unless & added on Unix
	"""

	def run(self, cmdline):
		cmdline = fixWindowsPath(cmdline)
		os.system("%s %s", (pypath, cmdline))

class Popen(LaunchMode):

	def run(self, cmdline):
		cmdline = fixWindowsPath(cmdline)
		os.popen(pypath + " " + cmdline)

class Start(LaunchMode):
	def run(self, cmdline):
		assert sys.platform[:3] == "win"
		cmdline = fixWindowsPath(cmdline)
		os.startfile(cmdline)

class Spawn(LaunchMode):
	def run(self, cmdline):
		os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))

class StartArgs(LaunchMode):
	def run(self, cmdline):
		assert sys.platform[:3] == "win"
		os.system("start "+ cmdline)

class Top_Level(LaunchMode):
	def run(self, cmdline):
		assert False, "Sorry - mode not yet implementd"

PortableLauncher = Spawn


if __name__ == '__main__':
	file= "hola.txt"
	launcher = PortableLauncher(file, file)
	launcher()
	