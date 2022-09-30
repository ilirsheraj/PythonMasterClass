#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 01:47:17 2022

@author: ilirsheraj
"""
equation = bytes((207, 128, 114, 194, 178))
print(equation) # Default Representation
print()
print(type(equation))
print(len(equation)) # The number of values
equation2 = b'\xcf\x80r\xc2\xb2'
print(equation2)
print()

# retreive the original numbers
for b in equation2:
    print(b, end=', ')
print()

print(equation2.decode('utf-8'))