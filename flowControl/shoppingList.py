#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:32:55 2022

@author: ilirsheraj
"""
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# Use continue to do the same!
for item in shopping_list:
    if item == "spam":
        continue
    # Careful with identation here!
    print("Buy " + item)
print()

for item in shopping_list:
    if item == "spam":
        break
    # Careful with identation here!
    print("Buy " + item)