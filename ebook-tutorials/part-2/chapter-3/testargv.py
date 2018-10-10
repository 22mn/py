import sys
#print(sys.argv)

"collect command-line options in a dictionary"

def getopts(argv):
	opts = {}
	while argv:
		if argv[0][0] == "-":
			opts[argv[0]] = argv[1]
			argv = argv[2:]
			print("If: ", argv)
		else:
			argv = argv[1:]
			print("Else: ", argv)
	return opts

if __name__ == '__main__':
	from sys import argv
	print(argv)
	myargs = getopts(argv)
	print(myargs)