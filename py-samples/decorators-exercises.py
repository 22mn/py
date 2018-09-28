import math,functools
from decorators import Circle
from decorators import *


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

#make_greeting("mgj")

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
	return sum(math.factorial(n) for n in range(terms))

#approximate_e(10)


@slow_down(rate=2)
def countdown(num):
	if num < 1:
		print("Lift off!")
	else:
		print(num)
		countdown(num-1)
#countdown(3)


class TimeWaster:
	@debug
	def __init__(self, max_num):
		self.max_num = max_num
	@timer
	def waste_time(self, num_times):
		for i in range(num_times):
			sum([i**2 for i in range(self.max_num)])

"""
repeat = repeat(num_times=3)
greet = repeat(greet)
"""

@repeat
def greet(name):
	print("Hello %s"%name)

@repeat(num_times=5)
def greeting(name):
	print("Hey %s"%name)

@count_calls
def hola():
	print("Hola")
@CountCalls
def hello():
	print("Hello")

@singleton
class TheOne:
	pass
@count_calls
def factorial(n):
	print("factorial has been called with n = "+str(n))
	if n == 1:
		return 1
	else:
		res = n * factorial(n-1)
		print(f"Intermediate result for {n} * factorial({n-1}) : {res}")
		return res

@functools.lru_cache(maxsize=5)
@count_calls
def fib(n):
	print("fib has been called with n = "+str(n))
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		res = fib(n-1) + fib(n-2)
		print(f"Intermediate result for fib({n}-1) + fib({n}-2) : {res}")
		return res
@cache
@count_calls
def fibo(n):
	if n <= 1:
		return n
	return fibo(n-1) + fibo(n-2)
