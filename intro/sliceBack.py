#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 20:03:20 2022

@author: ilirsheraj
"""
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] # start value is ommited
print(backwards)
print()
backwards = letters[25::-1]
print(backwards)
print()
# Another OPtion
backwards = letters[::-1]
print(backwards)

# Challenge
## Create a slice that produces the characters qpo
print(letters[16:13:-1])
## Slice the string to produce edcba
print(letters[4::-1])
## Slice the string to produce the last 8 characters in reverse order
print(letters[:-9:-1])
print()

# Idioms
## Return the last n-characters
print(letters[-4:])
# Get the last item
print(letters[-1:])
# Get only the first item: WOrks for empty sequences as well
print(letters[:1])
# same result, but not if the string is empty
print(letters[0])

