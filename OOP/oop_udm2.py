class Instructors:
	companyName = "Bluelime"

	def __init__(self, course, duration):
		self.course = course
		self.duration = duration

	def printinfo(self):
		print("My Company name is ", Instructors.companyName)


# Instantiate the class
elearning = Instructors("Python or Beginners", 80)
bls = Instructors("Django for Beginners", 50)

# Change the value of bls attribute and check it using print
bls.course = "HTML"

# Delete an attribute; It will give an error if you wanna play it
del bls.duration

# Use a method from the class on an instance of the class
bls.printinfo()

# Accessing attributes from an instance of the class
print(elearning.course)
print(elearning.duration)
print(bls.course)
print(bls.duration)
