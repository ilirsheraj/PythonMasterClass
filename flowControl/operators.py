#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 01:55:08 2022

@author: ilirsheraj
"""

a = 12
print(a)
b = 3
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b) # Produces float result
print(a // b) # Integer Division (rounded towards minus infinity)
print(a % b) # Modulo: remainder operator

print()

#for i in range(1,4):
#    print(i)
#    
#print()
#
#for i in range(1,a//b):
#    print(i) # i here is an expression (it is evaluated)
#
#print()
#
#i = 1 # i here is not expression, it is bound to the value 1
#print(i)
#i = 2
#print(i)
#i = 3
#print(i)

# Operator Precedence

print(a + b/3 - 4*12)
print()
print(a+ (b/3) - (4*12))
print()
print(((a+b)/3 - 4) *12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()
print(a / (b * a) / b)
print(a / ((b * a) / b))