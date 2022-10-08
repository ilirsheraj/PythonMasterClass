# Here we will build a Kettle class: It's going to model an electric Kettle
class Kettle(object):

	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False


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
