import functools,time


def do_twice(func):

	# protect func identity 
	
	@functools.wraps(func)
	def wrapper_do_twice(*args,**kwargs):
		func(*args,**kwargs)
		return func(*args,**kwargs)

	return wrapper_do_twice

def timer(func):
	"""Print the runtime of the decorated function"""
	@functools.wraps(func)
	def wrapper_timer(*args,**kwargs):
		
		start_time = time.perf_counter()
		value = func(*args,**kwargs)
		end_time = time.perf_counter()
		
		run_time = end_time - start_time

		print(f"Finished {func.__name__!r} in {run_time:.4f} seconds")
		return value

	return wrapper_timer

def debug(func):
	"""Print the function signature and return value"""
	@functools.wraps(func)
	def wrapper_debug(*args, **kwargs):
		args_repr = [repr(a) for a in args]
		kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
		signature = ", ".join(args_repr + kwargs_repr)
		print(f"Calling {func.__name__}({signature})")
		value = func(*args,**kwargs)
		print(f"{func.__name__} returned {value!r}")
		return value
	return wrapper_debug

def slow_down(_func=None,*,rate=1):
	"""Sleep given amount of seconds before calling the function"""
	
	def decorator_slow_down(func):
		@functools.wraps(func)
		def wrapper_slow_down(*args, **kwargs):
			time.sleep(rate)
			return func(*args,**kwargs)
		return wrapper_slow_down

	if _func is None:
		return decorator_slow_down
	else:
		return decorator_slow_down(_func)


def repeat(_func=None,*,num_times=2):
	def deco_repeat(func):
		#print("deco: %s"%func)
		@functools.wraps(func)
		def wrapper_repeat(*args,**kwargs):
			for i in range(num_times):
				value = func(*args, **kwargs)
			return value
		return wrapper_repeat
	if _func is None:
		#print("if: %s" %_func)
		return deco_repeat
	else:
		#print("else: %s "%_func)
		return deco_repeat(_func)


def count_calls(func):
	@functools.wraps(func)
	def wrapper_count_calls(*args,**kwargs):
		wrapper_count_calls.num_calls += 1
		print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
		return func(*args,**kwargs)
	wrapper_count_calls.num_calls = 0
	return wrapper_count_calls


def singleton(cls):
	"""Make a class a singleton class(one instance)"""
	@functools.wraps(cls)
	def wrapper_singleton(*args,**kwargs):
		if not wrapper_singleton.instance:
			wrapper_singleton.instance = cls(*args, **kwargs)
		return wrapper_singleton.instance
	wrapper_singleton.instance = None
	return wrapper_singleton


class CountCalls:
	def __init__(self,func):
		functools.update_wrapper(self,func)
		self.func = func
		self.num_calls = 0
	def __call__(self,*args,**kwargs):
		self.num_calls += 1
		print(f"Call {self.num_calls} of {self.func.__name__!r}")
		return self.func(*args,**kwargs)


class Circle:
	def __init__(self, radius):
		self._radius = radius

	@property
	def radius(self):
		"""Get value of radius"""
		return self._radius

	@radius.setter
	def radius(self,value):
		"""Set radius, raise error if negative"""
		if value >= 0:
			self._radius = value
		else:
			raise ValueError("Must be Positive Value!")
	@property
	def area(self):
		"""Calculate area inside circle"""
		return self.pi() * self._radius ** 2
	
	def cylinder_volume(self, height):
		"""Calculate volume of cylinder with circle as base"""
		return self.area * height

	@classmethod
	def unit_circle(cls):
		"""Factory method creating a circle with radius 1"""
		return cls(1)

	@staticmethod
	def pi():
		"""Value of pi 3.14159... same with math.pi"""
		return 3.14159

