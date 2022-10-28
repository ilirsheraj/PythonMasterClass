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


def build_tuple(*args):
	return args


def word_length(*args):
	char_count = 0
	for i in args:
		char_count += len(i)
	return char_count / len(args)


def print_backwards(*args):
	for i in args[::-1]:
		print(i[::-1], end=' ')


def smallest(*args):
	return min(args)


print(average(1, 2, 3, 4))
print("-" * 30)

message = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message))
print(message)
print("-" * 30)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)
print("-" * 30)

count = word_length("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print("The average word length is {}".format(count))
print("-" * 30)

lowest = smallest(9, 4, 56, 1, 5, -23, 84)
print(smallest(lowest))
print("-" * 30)

print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader")
