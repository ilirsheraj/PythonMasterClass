#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 00:20:03 2022

@author: ilirsheraj
"""
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Nested list (list within a list)
numbers = [even, odd]
print(numbers)
print()

for number_list in numbers:
    print(number_list)
    for value in number_list:
        print(value)