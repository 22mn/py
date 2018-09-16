# decorator samples
import functools

def my_decorator(func):
	def wrapper():
		print("first stage")
		func()
		print("second stage")
	return wrapper

# hola = my_decorator(hola)
@my_decorator
def hola():
	print("Hola Amigo")


def hunger(func):

	# keeps identity of caller function
	# without this caller lost its identity 
	# and its become wrapper's
	@functools.wraps(func)	
	
	def wrapper(*args,**kwargs):
		"""Wrapper function Docs"""
		print("i am so hungry")
		print(func(*args,**kwargs))
		return "i am full"
	return wrapper

@hunger
def eat(*args):
	"""Eat function Docs"""
	return "Hello, %s" %(" ".join(str(i) for i in args))

print(eat("apple","ramen"))