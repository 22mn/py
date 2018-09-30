from person_start import Person

class Manager(Person):

	def __init__(self, name, age, pay):
		Person.__init__(self,name, age, pay,"manager")

	def giveRaise(self, percent, bonus=0.1):
		self.pay *= (1+percent+bonus)
		return self.pay

if __name__ == '__main__':
	tom = Manager("Tom Hook", 42, 50000)
	print(tom)

