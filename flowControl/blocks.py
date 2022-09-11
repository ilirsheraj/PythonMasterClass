#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 01:29:54 2022

@author: ilirsheraj
"""

for i in range(1,13):
    print("No. {} square is {} and cubed is {:4}".format(i, i**2, i**3))
    print("-"*40)
    
print("*"*40)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {} years".format(18-age))

# print()
# # Another way of doing the same thing
# if age < 18:
#     print("Please come back in {} years".format(18-age))
# else:
#     print("You are old enough to vote")
#     print("Please put an X in the box")

# Let's use elif
if age < 18:
    print("Please come back in {} years".format(18-age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")