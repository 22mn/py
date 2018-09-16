from decorators import do_twice,timer,debug


@do_twice
def eat(*args):
	"""Eat function Docs"""
	print(args)
	return "Hello, %s" %(" ".join(str(i) for i in args))

#print(eat("apple","ramen"))

@timer
def run_timer(times):
	for i in range(times):
		sum([i**2 for i in range(1000)])

#run_timer(100)

@debug
def make_greeting(name, age=None):
	if age is None:
		return f"Hola {name}"
	else:
		return f"{name} is {age} years old!"

make_greeting("mgj")