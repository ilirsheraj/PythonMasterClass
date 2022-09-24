#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 23:49:13 2022

@author: ilirsheraj
"""
# Not the best way to open a file, its just for educational purposes

jabber = open("Jabberwocky.txt", "r")

# # Iterate over
# for line in jabber:
#     print(line)
    
# jabber.close()

# # To remove the new empty line: Remove the default \n
# for line in jabber:
#     print(line, end="")
    
# jabber.close()

# The other way is to strip off the line
for line in jabber:
#    print(line.strip(), end=" ")
    print(line.strip())
#    print(len(line))

# Closing is essential, especially when writing data as it may be lost
jabber.close()