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

	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname)
		# self.firstname = fname
		# self.lastname = lname

	def printinfo(self):
		print(self.firstname, self.lastname)


florist = Person("Jane", "Flowers")
florist.print_name()
happy_lawyers = Lawyers("Jack", "Smiley")
happy_lawyers.print_name()
happy_lawyers.printinfo()
