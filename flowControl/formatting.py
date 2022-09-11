#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 00:41:51 2022

@author: ilirsheraj
"""
for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))
print()

# Lets format it a bit by changing the field width
for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))
print()

# Lets make it left aligned
for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))
print()

# Let's center it
for i in range(1,13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i**2, i**3))
print()

# Specify precision after decimal point
print("Pi is approximately {0:12}".format(22/7)) # 12 decimal points
print()
print("Pi is approximately {0:12f}".format(22/7)) # default 6 digits
print()
print("Pi is approximately {0:12.50f}".format(22/7)) # 12 is width, 50 is decimal precision
print()
print("Pi is approximately {0:52.50f}".format(22/7)) # bigger width
print()
print("Pi is approximately {0:62.50f}".format(22/7))
print()
print("Pi is approximately {0:72.50f}".format(22/7))
print()
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))
print()

# Width of 4 in last column
for i in range(1,13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
print()

# The f-strings
print()
name = "Tim"
greeting = "Hello "
print(greeting + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")

print(f"Pi is approximately {22/7:12.50f}")
print()
pi = 22/7
print(f"Pi is approximately {pi:12.50f}")