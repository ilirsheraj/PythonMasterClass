#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 00:47:20 2022

@author: ilirsheraj
"""
import json

languages = [
    ["ABC", 1987],
    ["Algol 68", 1968],
    ["APL", 1962],
    ["C", 1973],
    ["Haskell", 1990],
    ["Lisp", 1958],
    ["Modula-2", 1977],
    ["Perl", 1987],
    ]

# Write the list into a file using json.dump()
with open("test.json", "w", encoding="utf-8") as testfile:
    json.dump(languages, testfile)
    
# Read it back again
# We read it back as a list
with open("test.json", "r", encoding= "utf-8") as json_file:
    data = json.load(json_file)
print(data)
print(data[2])