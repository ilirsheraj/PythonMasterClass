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
		self.name = name
		self.price = price
		self.quantity = quantity

		# Actions to execute
		Item.all.append(self)

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

	def __repr__(self):
		return f"Item('{self.name}', {self.price}, {self.quantity})"


Item.instantiate_from_csv()
print(Item.all)



# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 70)


# print(Item.all)


# for instance in Item.all:
# 	print(instance.name)

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

# print(item1.calculate_total_prince())
# print(item2.calculate_total_prince())
# print(Item.pay_rate) # class level
# print(item1.pay_rate)
# print(item2.pay_rate)

# # See all attributes
# print(Item.__dict__) # class level
# print(item1.__dict__) # instance level
#
# item1.apply_discount()
# print(item1.price)
#
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)
