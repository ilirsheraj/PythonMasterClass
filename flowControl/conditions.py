#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 00:58:24 2022

@author: ilirsheraj
"""
age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
#     print("Have a good day at work")

# Simplifying chained comparfions
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time!")

print("-"*30)

if age < 16 or age > 65:
    print("Enjoy your free time!")
else:
    print("Have a good day at work")