# Write some code asking the user to enter two integer and divide the first by the second
# The program shouldn't crash
import sys


def getint(prompt):
	while True:
		try:
			number = int(input(prompt))
			return number
		except ValueError:
			print("You entered an invalid number, please enter an integer")
		except EOFError:
			# It terminates the program when pressing ctrl + D
			sys.exit(1)


first_number = getint("Please enter the first number: ")
second_number = getint("Please enter the second number: ")


try:
	print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
	print("You cannot divide by zero")
	# we can temrinate here as well, although its not necessary
	sys.exit(2)
