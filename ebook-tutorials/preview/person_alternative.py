"""
Alternative implementation of person classes, with data, behavior,
and operator overloading (not used for objects stored persistently)
"""

class Person:
	def __init__(self, name, age, pay=0, job=None):
		self.name = name
		self.age = age
		self.pay = pay
		self.job = job

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self, percent):
		self.pay *= 1+percent
		return self.pay
	
	def __str__(self):
		return "<%s => %s: %s, %s>" %(
			self.__class__.__name__, self.name ,self.job, self.pay)

class Manager(Person):
	"""
	a person with custom raise
	inherits general lastname, str
	"""
	def __init__(self, name, age, pay):
		Person.__init__(self,name, age, pay,"manager")

	def giveRaise(self, percent, bonus=0.1):
		Person.giveRaise(self, percent+bonus)

if __name__ == '__main__':
	bob = Person("Bob Smith", 22, 40000, "software")
	sue = Person("Sue Jones", 21, 35000, "hardware")
	tom = Manager("Tom Hook", 36, 50000)

	print("",bob,"\n",sue,"\n",tom)