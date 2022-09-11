#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 00:51:00 2022

@author: ilirsheraj
"""
# \n starts a new line in the code
splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

# tab the output
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# Escape special characters
print('The pet shop owner said "No, No, \'e\'s uh,...he\'s resting".')
# Another way
print("The pet shop owner said \"No, No, 'e's uh,...he's resting\".")
# Use tripple quotes
print("""The pet shop owner said "No, No, 'e's uh,...he's resting".""")

# Tripple quotes for splitting on multiple lines
anotherSplitString = """This string has been
split over
several
lines"""
print(anotherSplitString)

# Escape the end of the line: Make it single line
anotherSplitString = """This string has been \
split over \
several \
lines"""
print(anotherSplitString)

# Another way: Remove the space
print("""The pet shop owner said "No, No, \
'e's uh,...he's resting".""")

# Include the backslash character
## 1 - Use two backslashes
print("C:\\Users\\timbuchalka\\notes.txt")
## 2 - Use raw string (r)
print(r"C:\Users\timbuchalka\notes.txt")