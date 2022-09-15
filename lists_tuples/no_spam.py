#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 01:48:22 2022

@author: ilirsheraj
"""
menu = [
        ["egg", "bacon"], 
        ["egg", "sausage", "bacon"], 
        ["egg", "spam"], 
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"]
        ]

# Write code to print out all the meals in the list but with spam removed
# Approach 1 (My version)
for lists in menu:
    if "spam" not in lists:
        print(lists)
    else:
        print([s for s in lists if s != "spam"])
print()

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)
print()

# A different approach
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()
print()