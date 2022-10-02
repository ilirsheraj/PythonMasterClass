# # To see everything about python
# print(dir())
#
# # To see the built-in functions
# print(dir(__builtins__))
# print()
#
# # Use a for loop
# for m in dir(__builtins__):
#     print(m)

import shelve

# print(dir())
# print()
# print(dir(shelve))

# for obj in dir(shelve.Shelf):
#     if obj[0] != "_":
#         print(obj)

# # To get information about a library
# help(shelve)

# Help on individual functions
import random
help(random.randint)
