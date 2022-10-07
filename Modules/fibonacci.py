# def fib(n):
# 	"""
# 	Calculates the fibonacci number of n
# 	F(n) = F(n-1) + F(n-2)
# 	"""
# 	if n < 2:
# 		return n
# 	else:
# 		return fib(n-1) + fib(n-2)
#
#
# for i in range(36):
# 	print(i, fib(i))

def fibonacci(n):
	"""
	Calculates the fibonacci number of n
	Way faster method than the previous recursive function
	"""
	if n == 0:
		result = 0
	elif n == 1:
		result = 1
	else:
		n_minus1 = 1
		n_minus2 = 0
		for i in range(1, n):
			result = n_minus2 + n_minus1
			n_minus2 = n_minus1
			n_minus1 = result
	return result


for i in range(45):
	print(i, fibonacci(i))
