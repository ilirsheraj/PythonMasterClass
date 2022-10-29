import sys

big_range = range(10000)
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

def my_range(n: int):
	"""
	Define a function to mimic range() function of python
	"""
	print("my_range starts")
	start = 0
	while start < n:
		print("my_range is returning {}".format(start))
		yield start
		start += 1


_ = input("line 18")
big_range = my_range(5)
_ = input("line 20")

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# Create a list containing all the values in big_range
big_list = []

_ = input("line 27")
for val in big_range:
	_ = input("line 29 - inside loop")
	big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
