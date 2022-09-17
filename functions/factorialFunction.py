#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 23:18:38 2022

@author: ilirsheraj
"""
# The factorial of a number is the product of all the values from 1 to the number, inclusive.
# Thus 4 factorial, which is written as 4!, is calculated as 1 * 2 * 3 * 4 = 24
# 5! is 1 * 2 * 3 * 4 * 5 = 120
# The convention is that 0! = 1 (not zero, as you might expect).
# Write a function called factorial, that will return the factorial of the number passed as its argument.
# You must include a Docstring, and function annotations, in your function.

def factorial(num: int) -> int:
    """
    Takes a positive integer and returns its factorial
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

for i in range(36):
    print(i, factorial(i))