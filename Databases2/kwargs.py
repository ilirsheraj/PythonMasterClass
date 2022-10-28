# def print_backwards(*args, file=None):
# 	"""
# 	Reverses the order of letters and words in a tuple
# 	Writes the results in a file
# 	"""
# 	for word in args[::-1]:
# 		print(word[::-1], end=' ', file=file)


# def print_backwards(*args, **kwargs):
# 	print(kwargs)
# 	"""
# 	Reverses the order of letters and words in a tuple
# 	Writes the results in a file
# 	"""
# 	for word in args[::-1]:
# 		print(word[::-1], end=' ', **kwargs)
#
#
# with open("backwards.txt", "w") as backwards:
# 	print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards, end='\n')


# # When the same argument is passed twice, two solutions
# # 1
# def print_backwards(*args, end=' ', **kwargs):
# 	print(kwargs)
# 	"""
# 	Reverses the order of letters and words in a tuple
# 	Writes the results in a file
# 	"""
# 	for word in args[::-1]:
# 		print(word[::-1], end=' ', **kwargs)
#
#
# with open("backwards.txt", "w") as backwards:
# 	print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards, end='\n')


# Second approach
# When the same argument is passed twice, two solutions
# 1
# def print_backwards(*args, end=' ', **kwargs):
# 	"""
# 	Reverses the order of letters and words in a tuple
# 	Writes the results in a file
# 	"""
# 	print(kwargs)
# 	kwargs.pop('end', None)
# 	for word in args[::-1]:
# 		print(word[::-1], end=' ', **kwargs)


def print_backwards(*args, **kwargs):
	"""
	Reverses the order of letters and words in a tuple
	Writes the results in a file
	"""
	end_character = kwargs.pop('end', '\n')
	sep_character = kwargs.pop('sep', ' ')
	# for word in args[::-1]:
	for word in args[:0:-1]:  # change the range
		print(word[::-1], end=sep_character, **kwargs)
	# print(end=end_character)
	print(args[0][::-1], end=end_character, **kwargs)  # print the first word separately


with open("backwards.txt", "w") as backwards:
	print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
	print("Another String")
print("-" * 30)

print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)
