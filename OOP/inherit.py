class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def print_name(self):
		print(self.firstname, self.lastname)


class Lawyers(Person):
	"""
	def __init__(self, fname, lname) overwrites parent class
	and it uses it's own method and attributes
	"""

	def __init__(self, fname, lname, casetype):
		Person.__init__(self, fname, lname)
		"""
		Add an attribute specific to child class 
		"""
		self.casetype = casetype
		# self.firstname = fname
		# self.lastname = lname

	def printinfo(self):
		print("Hello, my name is ", self.firstname, self.lastname)


florist = Person("Jane", "Flowers")
florist.print_name()
happy_lawyers = Lawyers("Jack", "Smiley", "Criminal")
happy_lawyers.print_name()
happy_lawyers.printinfo()
print(happy_lawyers.casetype)
