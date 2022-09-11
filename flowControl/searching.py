#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:42:33 2022

@author: ilirsheraj
"""
shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# item_to_find = "spam"
# found_at = None # Something doesnt have a value

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
    
# print("Item found at position {}".format(found_at))

# Replace spam with an item not in the list
item_to_find = "albatros"
found_at = None # Something doesnt have a value

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

# A more efficient version of doing the same thing
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))