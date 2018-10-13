"read numbers till eof and show squares"

def interact():
	print("Hello stream world")
	while True:
		try:
			reply = input("Enter a number>")
			num = int(reply)
			print("%d squared is %d" %(num,num**2))
		except EOFError:
			break

	print("Bye")

if __name__ == '__main__':
	interact()