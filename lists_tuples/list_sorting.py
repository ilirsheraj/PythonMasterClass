#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:25:33 2022

@author: ilirsheraj
"""
# create two lists for even and odd numbers respectively
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Combine them into a single list
even.extend(odd)
print(even)
print()
another_even = even
print(another_even)
print()
# This mutates the list
even.sort()
print(even)
print()
even.sort(reverse=True)
print(even)
print(another_even)

print(id(even))
print(id(another_even))