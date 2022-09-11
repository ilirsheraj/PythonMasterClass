#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:40:50 2022

@author: ilirsheraj
"""
# activity = input("What would you like to do today? ")

# # if "cinema" not in activity:
# #     print("But I want to go to the cinema")

# if "cinema" not in activity.casefold(): # Makes it lowercase!
#     print("But I want to go to the cinema")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 30:
    print("{}, Welcome to the Holiday".format(name))
else:
    print("{}, Your age is not appropriate for this occasion".format(name))