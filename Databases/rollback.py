class Account(object):

	def __init__(self, name: str, opening_balance: int = 0):
		self.name = name
		self._balance = opening_balance
		print("Account created for {}. ".format(self.name), end='')
		self.show_balance()  # define below

	def deposit(self, amount: int) -> float:
		if amount > 0.0:
			self._balance += amount
			print("{:2f} deposited".format(amount / 100))
		return self._balance / 100

	def withdraw(self, amount: int) -> float:
		if 0 < amount <= self._balance:
			self._balance -= amount
			print("{:2f} withdrawn".format(amount / 100))
			return amount / 100
		else:
			print("The amount must be greater than zero and no more than your account balance")
			return 0.0

	def show_balance(self):
		print("Balance on account {} is {}".format(self.name, self._balance / 100))


if __name__ == "__main__":
	john = Account("John")
	john.deposit(1010)
	john.deposit(10)
	john.deposit(10)
	john.withdraw(30)
	john.withdraw(0)
	john.show_balance()
