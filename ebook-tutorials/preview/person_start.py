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
		return "<%s => %s>" %(self.__class__.__name__, self.name)

if __name__ == '__main__':
	bob = Person("Bob Smith", 22, 40000, "software")
	sue = Person("Sue Jones", 21, 45000, "hardware")
	print(bob)
	print(sue)

	print(sue.lastName())
	print(bob.giveRaise(0.1))
	print(bob)