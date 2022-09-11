#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:04:44 2022

@author: ilirsheraj
"""
# number = input("Please enter a series of numbers, using separators you like: ")
# separators = ""

# for char in number:
#     if not char.isnumeric():
#         separators = separators + char

# print(separators)

# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])
# print(sum([int(val) for val in values]))

# Quiz
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

capital = ""

for char in quote:
    if char.isupper():
        capital = capital + char
print(capital)