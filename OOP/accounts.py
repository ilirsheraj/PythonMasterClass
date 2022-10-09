import datetime
import pytz


class Account:
	"""
	Simple account class with balance
	"""

	@staticmethod
	def _current_time():
		utc_time = datetime.datetime.utcnow()
		return pytz.utc.localize(utc_time)

	def __init__(self, name, balance):
		self._name = name
		self.__balance = balance
		self._transaction_list = [(Account._current_time(), balance)]
		print("Account created for " + self._name)
		self.show_balance()

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			self.show_balance()
			self._transaction_list.append((Account._current_time(), amount))

	def withdraw(self, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			self._transaction_list.append((Account._current_time(), -amount))
		else:
			print("The amount you are trying to withdraw is greater than your account balance!")
		self.show_balance()

	def show_balance(self):
		print("Balance is {}".format(self.__balance))

	def show_transactions(self):
		for date, amount in self._transaction_list:
			if amount >= 0:
				tran_type = "deposited"
			else:
				tran_type = "withdrawn"
				amount *= -1
			print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
	tim = Account("Tim", 0)
	# tim.show_balance()

	tim.deposit(1000)
	# tim.show_balance()
	tim.withdraw(500)
	# tim.show_balance()
	tim.withdraw(2000)
	tim.show_transactions()

	# Create another account
	steph = Account("Steph", 800)
	# Messing with internal attributes here! Will change everything
	# if we rename _balance into __balance, this will not affect the balance at all
	steph.__balance = 200
	steph.deposit(100)
	steph.withdraw(200)
	steph.show_transactions()
	steph.show_balance()
	print(steph.__dict__)
	# Try to force private access with `__` This is not advisable!
	steph._Account__balance = 40
	steph.show_balance()
