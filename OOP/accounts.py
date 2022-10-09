class Account:
	"""
	Simple account class with balance
	"""

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		print("Account created for " + self.name)

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			self.show_balance()

	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
		else:
			print("The amount you are trying to withdraw is greater than your account balance!")
		self.show_balance()

	def show_balance(self):
		print("Balance is {}".format(self.balance))


if __name__ == '__main__':
	tim = Account("Tim", 0)
	tim.show_balance()

	tim.deposit(1000)
	# tim.show_balance()
	tim.withdraw(500)
	# tim.show_balance()
	tim.withdraw(2000)
