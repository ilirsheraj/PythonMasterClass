def average(*args):
	"""
	It takes a tuple as input and returns the average of the numbers given
	"""
	print(type(args))
	print("args is {}".format(args))
	print("*args is:", *args)
	mean = 0
	for arg in args:
		mean += arg
	return mean / len(args)


print(average(1, 2, 3, 4))
print()


def build_tuple(*args):
	return args


message = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message))
print(message)
