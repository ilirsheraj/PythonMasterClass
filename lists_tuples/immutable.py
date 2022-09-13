#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 02:01:44 2022

@author: ilirsheraj
"""
# result = True

# another_result = result

# print(id(result))
# print(id(another_result))

# # The ID will change, python rebinds the result to a new value False
# result = False
# print(id(result))

result = "Correct"
another_result = result

print(id(result))
print(id(another_result))

# Again rebound, different ID
result += "ish"
print(id(result))

# This will not change, python creates a new object
print(id(another_result))