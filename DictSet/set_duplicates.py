#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 23:13:18 2022

@author: ilirsheraj
"""
# Lets create a list and remove duplicate values from it
data = ["blue", "red", "blue", "green", "red", "blue", "white"]
print(data)
print()

# Create a set from a list to remove duplicates
unique_data = set(data)
print(unique_data)
print()

# Create a sorted list
unique_data = sorted(set(data))
print(unique_data)
print()

# To keep original data's order, we can use dictionary and turn it into list
unique_data = list(dict.fromkeys(data))
print(unique_data)