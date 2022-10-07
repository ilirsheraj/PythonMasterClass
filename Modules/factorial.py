# Create a function to calculate factorials
# def fact(n):
# 	"""
# 	Calculate n! iteratively
# 	"""
# 	result = 1
# 	if n == 0 or n == 1:
# 		result = 1
# 	elif n > 1:
# 		for f in range(2, n+1):
# 			result *= f
# 	return result
#
#
# for i in range(130):
# 	print(i, fact(i))


# Let's define a recursive function
def fact_rec(n):
	"""
	Calculate n! recursively
	"""
	if n <= 1:
		return 1
	else:
		return n * fact_rec(n-1)


for i in range(130):
	print(i, fact_rec(i))
