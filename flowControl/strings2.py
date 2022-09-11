#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 02:27:27 2022

@author: ilirsheraj
"""
# Strings are one of the python's sequence data types

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3]) # Prints "w" because of zero indexing
print()

# Mini-Challenge
## Add some code to the program so that it prints out "we win" with each character on a separate line

for i in [3,4,9,3,6,8]:
	print(parrot[i])
print()	
# Indexing Backward in a Sequence
print(parrot[-1])
print(parrot[-14])
print()

# Do the same (we win) but by using negative indexing
for i in [-11, -1, -5, -11, -8,-6]:
	print(parrot[i])
print()	
# String Slicing
print(parrot[0:6])
print()
print(parrot[3:5])
print()
print(parrot[0:9])
print()
# Automatically from zero
print(parrot[:9])
print()
# Automatically to the end
print(parrot[10:])
print()
# Print everything
print(parrot[:])
print()
print(parrot[:6])
print(parrot[6:])
print()
print(parrot[:6] + parrot[6:])
print()

# Use negatives
print(parrot[-4:2]) # prints nothing because you cant go backward
print()
print(parrot[-4:-2])
print(parrot[-4:12])
print()
print(parrot[-14:-6] + parrot[-6:])

# Slice using steps
print(parrot[0:6:2]) #New
print()
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])
print()
number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

# Use separators to split up individual values
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

