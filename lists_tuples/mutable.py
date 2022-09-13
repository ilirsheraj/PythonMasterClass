#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 02:11:43 2022

@author: ilirsheraj
"""
shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["coookies"]
print(shopping_list)

# No change
print(another_list)
print(id(shopping_list))
print(id(another_list))

# chain assignment
a = b = c = d = e = f = another_list

# There still only one list
print(a)
print("Adding cream")
b.append("cream")
print(c)
print(d)
print(another_list)