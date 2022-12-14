# Here we will build a Kettle class: It's going to model an electric Kettle
class Kettle(object):

	# power_source will be shared by all instances, it's a class attribute
	power_source = "Electricity"

	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False

	def switch_on(self):
		self.on = True


# Create the first instance
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

# Set a new price for kenwood
kenwood.price = 12.75
print(kenwood.price)
print()

# Create a second instance of kettle
hamilton = Kettle("Hamilton", 14.55)
print(hamilton.make)
print(hamilton.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print()
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# This is another way of calling the class definition initially
Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()
print("-"*30)

# Classes are dynamic and can be edited.
# Create a new attribute for kenwood but not for hamilton and see the difference
kenwood.power = 1.5
print(kenwood.power)
# hamilton.power will give error because it does not have any such attribute
# print(hamilton.power)
print()

# Change power source for class, and it will be inherited by all instances
print("Switch to atomic power")
Kettle.power_source = "Atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "Gas"
print(kenwood.power_source)
# Hamilton will not be affected because of its definition in class
print(hamilton.power_source)
print()

print("Dictionary of namespaces of the classes and instances can be accessed by: ")
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
