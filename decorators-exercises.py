from decorators import do_twice,timer


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

run_timer(100)