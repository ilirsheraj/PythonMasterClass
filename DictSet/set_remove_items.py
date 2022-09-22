#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 23:28:45 2022

@author: ilirsheraj
"""
# Create a set of integers
small_ints = set(range(21))
print(small_ints)
print()

# # Clear the set
# small_ints.clear()
# print(small_ints)

# Delete individual items
small_ints.discard(10)
small_ints.remove(11)
print(small_ints)
print()


# If item doesnt exist, there is no error
small_ints.discard(99)
print(small_ints)

# # Key error
# small_ints.remove(99)
# print(small_ints)


# If we want to remove a bunch of items
# Using discard, even if the item we want to remove is not in the set, no error will occur
# We want to make sure its not there
restricted_items = {",", ":", "..."}
packing_set = {"a", "cdf", ":", ".", ":", "'", "ascdsf"}
print(packing_set)

for item in restricted_items:
    packing_set.discard(item)
print(packing_set)