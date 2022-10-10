# Import the item class
from item import Item


class Phone(Item):

	def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
		# call the superfunction to have access to all attributes
		super().__init__(
			name, price, quantity
		)

		# Run validations to the received arguments and print a message when conditions are not fulfilled
		assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than or equal to zero"
		self.broken_phones = broken_phones