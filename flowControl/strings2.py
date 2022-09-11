#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:48:42 2022

@author: ilirsheraj
"""
number = "9,223;372:036 854,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
print(separators)

# Use separators to split up individual values
values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])