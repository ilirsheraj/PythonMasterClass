# # Create a function
# def addNumbers(a, b, c=1):
# 	return a + b + c
#
# print(addNumbers(8,9))
# print(addNumbers(8, 9, 4))


# Create a polymorphic class with methods
class UK():
	def capital_city(self):
		print("London is the Capital of the UK")

	def language(self):
		print("English is the primary language")


class Spain():
	def capital_city(self):
		print("Madrid is the Capital of the Spain")

	def language(self):
		print("Spanish is the primary language")


def europe(eu):
	eu.capital_city()


# Create instances for both classes
queen = UK()
# queen.capital_city()

zara = Spain()
# zara.capital_city()

# This is cool, it will print the statements of methods above
europe(queen)
europe(zara)

# # Run in a for loop to access the methods inside the classes
# for country in (queen, zara):
# 	country.capital_city()
# 	country.language()
