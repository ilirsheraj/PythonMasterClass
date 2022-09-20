#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 01:30:26 2022

@author: ilirsheraj
"""
d = {
     0: "zero",
     1: "one",
     2: "two",
     3: "three",
     4: "four",
     5: "five",
     6: "six",
     7: "seven",
     8: "eight",
     9: "nine",
     }

pantry_items = ["chicken", "spam", "egg", "bread", "lemon"]

# # Create a dictionary with keys without any value
# new_dict = dict.fromkeys(pantry_items)
# print(new_dict)

# # Make all values zero
# new_dict = dict.fromkeys(pantry_items,0)
# print(new_dict)

# keys = d.keys()
# print(keys)
# print()

# # Print dictionary keys
# for item in d:
#     print(item)
# print()

# # Make it more explicit
# for item in d.keys():
#     print(item)
# print()

# # remaining methods
# d2 = {
#       7: "lucky seven",
#       10: "ten",
#       3: "this is the new three",
#       }

# d.update(d2)
# for key, value in d.items():
#     print(key, value)
# print()

# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

# Values methods
v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)
print()

keys = list(d.keys())
values = list(v)

if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")
print()


# More efficient alternative
for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")
print()


# This also works for duplicated values
d = {
     0: "zero",
     1: "one",
     2: "two",
     3: "three",
     4: "four",
     5: "five",
     6: "six",
     7: "seven",
     8: "eight",
     9: "nine",
     "iv": "four",
     }

for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")