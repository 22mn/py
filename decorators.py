# decorator samples

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
	def wrapper(*args,**kwargs):
		print("i am so hungry")
		return func(*args,**kwargs)
	return wrapper

@hunger
def eat(*args):
	return "Hello, %s" %(" ".join(str(i) for i in args))

print(eat("apple","ramen"))