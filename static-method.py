import datetime
class Employee:

	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, _string):
		first,last,pay = _string.split("-")
		return cls(first,last,int(pay))

	#@staticmethod
	def is_workday(day):
		return day.weekday()==5 or day.weekday() ==6 

emp1 = Employee("mg","jean",100000)
emp2 = Employee("vi","vi",200000)

d = datetime.date(2018,9,15)
print(Employee.is_workday(d))