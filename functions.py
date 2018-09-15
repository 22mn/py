# function samples

def func(*args,**kwargs):
	for i in args:
		print(i)
	for j in kwargs:
		print(j)

_list = [1,2,3]
_dict = {"a":4,"b":5}

#func(1,2,3,a=4,b=5)
#func(*_list,**_dict)