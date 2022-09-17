#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 00:50:11 2022

@author: ilirsheraj
"""
# Write a function to calculate the sum of all numbers passed as its arguments.
# Your function should be called sum_numbers and should define a single variable argument 
# (i.e. a star argument) that will get the values to sum.
# To pass in this on-line interpreter, your function must contain a Docstring.
# The parameters and return value must be annotated. 
# Be careful here, you may want to review the lecture Function annotations and type hints, 
# or check PEP 484 to see what it says about annotating numerical arguments and return types.

def sum_numbers(*num: float) -> float:
    """
    The function takes a number of floats and/or integers and returns their sum
    """
    result = 0
    for i in num:
        result += i
    return result

print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(0))
print(sum_numbers(1,2,3,5.7, 10, 100001.1030453))