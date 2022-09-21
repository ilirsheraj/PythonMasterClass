#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 01:58:26 2022

@author: ilirsheraj
"""
animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
    }

# things = animals
# animals["teddy"] = "toy"
# print(things["teddy"])

# # Dictionaries are the same
# print(id(things))
# print(id(animals))

# # Create separate dictionaries
# things = animals.copy()
# animals["teddy"] = "toy"
# print(things["teddy"])
# print(animals["teddy"])

# # ID's are different
# print(id(things))
# print(id(animals))

# print()

# Deep and shallow copy (now values are mutable)
animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
    }

things = animals.copy()

print(things["teddy"])
print(animals["teddy"])
print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])