#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:31:18 2022

@author: ilirsheraj
"""
# # Create an empty set using set literal
# numbers = {*""}
# print(numbers, type(numbers))
# print()
# # Another way
# numbers = {*{}}
# print(numbers, type(numbers))
# print()

# # The most common way is the set() funcion
# numbers = set()
# print(numbers, type(numbers))
# print()

# numbers.add(1)
# print(numbers)

numbers = set()
while len(numbers) < 4:
    next_value = int(input("Please enter your next value: "))
    numbers.add(next_value)
print(numbers)