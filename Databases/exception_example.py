# x = 8 = 5  # Syntax Error
x = 8 - 5
# y = x / 0  # division by zero


# recursion error
def factorial(n):
	"""Calculates n recursively"""
	if n <= 1:
		return 1
	else:
		print(n / 0)
		return n * factorial(n-1)


# print(factorial(1000))  # recursion error

# try:
# 	print(factorial(1000))
# except RecursionError:
# 	print("This program cannot calculate factorials that large")
# except ZeroDivisionError:
# 	print("What are you doing dividing by zero?")
#
# print("The program is terminating")

# Handle more than one exception in a single except clause
try:
	print(factorial(1000))
except (RecursionError, ZeroDivisionError):
# except (RecursionError, OverflowError):
	print("This program cannot calculate factorials that large")

print("The program is terminating")
