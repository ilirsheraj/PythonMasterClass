class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def print_name(self):
		print(self.firstname, self.lastname)


florist = Person("Jane", "Flowers")
florist.print_name()
