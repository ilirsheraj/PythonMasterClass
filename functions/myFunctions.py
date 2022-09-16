#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:43:34 2022

@author: ilirsheraj
"""
def multiply():
    result = 10.5*4
    return result


answer = multiply()
print(answer)
print()

# Create a function with parameters (Arguments)
def multiply(x,y):
    result = x*y
    return result


answer = multiply(10.5, 4)
print(answer)
print(multiply(6, 7))
print()

for i in range(1,5):
    two_times = multiply(2, i)
    print(two_times)