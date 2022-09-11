#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:16:45 2022

@author: ilirsheraj
"""
# Augmented Assignment
x = 23

x += 1
print(x) # 24

x -= 4
print(x) # 20

x *= 5
print(x) # 100

x //= 4
print(x) # 25

x /= 5
print(x) # 5.0

x **= 2
print(x) # 25.0

x %= 5
print(x) # 0.0

# Concatenation and repetition
greeting = "good "
greeting += "morning "

print(greeting)

greeting *= 5
print(greeting)

# Quiz: Use a for-loop for multiplying 8*5
answer = 0
add = 5
for i in range(8):
    answer += add
print(answer)
    