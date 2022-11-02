# Use empty list (False)
entries = []

# print("all: {}".format(all(entries)))
# print("any: {}".format(any(entries)))

if entries:
	print("all: {}".format(all(entries)))
else:
	print(False)
print("any: {}".format(any(entries)))

results = bool(entries) and all(entries)
print(results)
