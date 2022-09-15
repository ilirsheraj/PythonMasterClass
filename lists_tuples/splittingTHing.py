#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 02:35:32 2022

@author: ilirsheraj
"""
panagram = "The quick brown fox jumps over the lazy dog"
words = panagram.split()
print(words)
print()

panagram = """"The quick brown 
fox jumps\tover 
the lazy dog"""
print(panagram)
words = panagram.split()
print(words)
print()

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ["9", " ",
                  "2", "2", "3", " ",
                  "3", "7", "2", " ",
                  "0", "3", "6", " ",
                  "8", "5", "4", " ",
                  "7", "7", "5", " ",
                  "8", "0", "7"
                  ]
print(generated_list)
print()
values1 = "".join(generated_list)
print(values1)
values = "".join(generated_list).split()
print(values)

# Create integer list: replace values in place
for index in range(len(values)):
    values[index] = int(values[index])
print(values)
print()

# Create a new list
integer_values = []
for value in values:
    integer_values.append(int(value))
print(integer_values)
print()

# Use list comprehension
print([int(i) for i in values])
print()
print("-"*40)

# Exercise
# For this exercise, you have to write a python program which prompts the user to enter three integers separated by ",".
# The user input is of the form: a,b,c, where a, b and c are numbers.
# Your program should calculate and display the result of the calculation: a + b - c

numbers = input("Please enter three numbers: ")
numbers = numbers.split(",")
result = int(numbers[0]) + int(numbers[1]) - int(numbers[2])
print(result)