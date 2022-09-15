#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 01:14:41 2022

@author: ilirsheraj
"""
a = b = c = d = e = f = 12
print(c)
a = b = c = d = e = f = 42
print(c)
print()

# Unpacking a tuple
x, y, z = 1, 2, 76
print(x)
print(y)
print(z)
print()

print("Unpacking a Tuple")
data = 1, 2, 76 # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)
print()
# Unpacking a list
data_list = [12, 13, 14]
p, q, r = data_list
print(p)
print(q)
print(r)
print()

# data_list = [12, 13, 14]
# # It will crash because list has 4 items
# data_list.append(15)
# p, q, r = data_list
# print(p)
# print(q)
# print(r)

# Enumerate function
# for index, character in enumerate("abcdefgh"):
#     print(index, character)
    
for t in enumerate("abcdefgh"):
    print(t)
print()

index, character = (0, "a")
print(index)
print(character)
print()

for t in enumerate("abcdefgh"):
    index, character = t
    # Unpack the tuple here
    print(index, character)
print()