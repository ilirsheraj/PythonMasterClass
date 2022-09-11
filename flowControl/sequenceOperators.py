#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 20:20:03 2022

@author: ilirsheraj
"""
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

# The same thing is produced by
print("he's " "probably " "pining " "for the " "fjords")
print()

# String mulltiplication
print("Hello " * 5)

print("Hello " * (5+4))

print("Hello " * 5 + "4")
print()

# Check if a string is a substring of another string
today = "friday"
print("day" in today) # True
print("fri" in today) # True
print("thur" in today) # False
print("parrot" in "fjord") # False