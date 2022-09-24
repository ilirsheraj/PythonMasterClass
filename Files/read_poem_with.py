#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:30:46 2022

@author: ilirsheraj
"""
# To avoid the problems with closing files and more efficient way
# File is closed automatically

# with open("Jabberwocky.txt", "r") as jabber:
#     for line in jabber:
#         print(line.rstrip())


# # readlines return a list of strings
# with open("Jabberwocky.txt", "r") as jabber:
#     lines = jabber.readlines()
    
# print(lines)
# print()
# # Read it in reverse
# print(lines[::-1])
# print()
# # print only the last line
# print(lines[-1:])
# print()

# # Print the poem in reverse order
# for line in reversed(lines):
#     print(line, end=" ")
    
    
# # The entire file is a single string
# # `r` is by default, if not given its ok
# with open("Jabberwocky.txt", "r") as jabber:
#     text = jabber.read()

# print(text)

# # All the text is reversed
# for char in reversed(text):
#     print(char, end="")


# Program will terminate when it finds the line "jubjub"
# `r` is by default, if not given its ok
with open("Jabberwocky.txt", "r") as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if "jubjub" in line.casefold():
            break

print("*"*50)

# `r` is by default, if not given its ok
with open("Jabberwocky.txt") as jabber:
    for line in jabber:
        print(line.rstrip())
        if "jubjub" in line.casefold():
            break