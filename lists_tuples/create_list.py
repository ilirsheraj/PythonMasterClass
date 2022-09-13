#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 00:03:02 2022

@author: ilirsheraj
"""
# list literal
empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Concatenate existing lists
numbers = even + odd
print(numbers)
print()

# Use function
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print()

# returns a list of strings
digits = sorted("432985617")
print(digits)
print()

# use list() function
digits = list("432985617")
print(digits)
print()

more_numbers = list(numbers)
print(more_numbers)
print()

print(id(numbers))
print(id(more_numbers))
print()

print(numbers is more_numbers)
print(numbers == more_numbers)
print()

more_numbers2 = numbers[:]
print(numbers is more_numbers2)
print(numbers == more_numbers2)
print()

print(id(numbers))
print(id(more_numbers2))
print()

more_numbers3 = numbers.copy()
print(numbers is more_numbers3)
print(numbers == more_numbers3)
print(id(numbers))
print(id(more_numbers3))

# For various ways of copying a list see the link below:
# https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-
# doesnt-change-unexpectedly-after-assignment/43220129#43220129