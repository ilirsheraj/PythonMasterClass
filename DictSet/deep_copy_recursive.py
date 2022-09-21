#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:20:50 2022

@author: ilirsheraj
"""
from quiz2 import deep_copy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]]
    }

copy_1 = copy.deepcopy(original)
copy_2 = deep_copy(original)

print(original)
print(copy_1)
print(copy_2)
print()

# First, perform simple copy without mutating the inner list
original["Tim"].append("Australia")
original["J-P"].append("UK")
print(original)
print(copy_1)
print(copy_2)
print()


# Append a new job to the inner list
original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")
# The above two lines ar ethe same as
# original["J-P"][1].append("Courier")
print(original)
print(copy_1)
print(copy_2)
print()
