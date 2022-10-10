import csv


class Item:
	# Add a class attribute
	pay_rate = 0.8  # The pay rate after 20% discount
	all = []  # Create an empty list to store the items

	def __init__(self, name: str, price: float, quantity=0):

		# Run validations to the received arguments and print a message when conditions are not fulfilled
		assert price >= 0, f"Price {price} is not greater than or equal to zero"
		assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
		# print(f"An instance created from {name}")
		self.__name = name
		self.price = price
		self.quantity = quantity

		# Actions to execute
		Item.all.append(self)

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		self.__name = value

	def calculate_total_prince(self):
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate

	# Use decorators to change the behavior of the function
	@classmethod
	def instantiate_from_csv(cls):
		with open("demo.csv", "r") as f:
			reader = csv.DictReader(f)
			items = list(reader)

		for item in items:
			Item(
				name=item.get('name'),
				price=float(item.get('price')),
				quantity=float(item.get('quantity'))
			)

	@staticmethod
	def is_integer(num):
		# We will count out the floats that are .0
		# For example, 5.0, 10.0
		if isinstance(num, float):
			# Count out the floats that are .0
			return num.is_integer()
		elif isinstance(num, int):
			return True
		else:
			return False

	def __repr__(self):
		return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

