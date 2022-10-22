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
		finally:
			print("The finally clause always executes")


first_number = getint("Please enter the first number: ")
second_number = getint("Please enter the second number: ")


try:
	print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
	print("You cannot divide by zero")
	# we can terminate here as well, although it's not necessary
	sys.exit(2)
else:
	print("Division was performed successfully")

