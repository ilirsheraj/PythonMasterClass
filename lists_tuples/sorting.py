#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:37:27 2022

@author: ilirsheraj
"""
pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)
print()

# get all unique letters
new_letters = []
for i in letters:
    if i in new_letters:
        continue
    else:
        new_letters.append(i)
print(new_letters)

print()

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
print(numbers)
# We get a different list
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

# Assign it to a variable: returns None!
another_sorted_numbers = numbers.sort()
print(numbers)
print(another_sorted_numbers)
print()

# Pass a literal to sorted
missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)