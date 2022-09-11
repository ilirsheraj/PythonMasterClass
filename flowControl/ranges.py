#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:21:29 2022

@author: ilirsheraj
"""
for i in range(10,16):
    print("i is now {}".format(i))
print()

for i in range(10):
    print("i is now {}".format(i))

print()
# Provide a step value
for i in range(0,10,2):
    print("i is now {}".format(i))

print()

# Backwards
for i in range(10,0,-2):
    print("i is now {}".format(i))

age = int(input("How old are you? "))

if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-"*30)

if age not in range(16,66):
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# Write a program to print all numbers between 0 to 100 that are divisible by 7
for i in range(0,100,7):
    print(i)
print()

# Another version
for i in range(0,100):
    if i%7 == 0:
        print(i)