#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 00:57:13 2022

@author: ilirsheraj
"""
import json

languages = [
    ("ABC", 1987),
    ("Algol 68", 1968),
    ("APL", 1962),
    ("C", 1973),
    ("Haskell", 1990),
    ("Lisp", 1958),
    ("Modula-2", 1977),
    ("Perl", 1987),
    ]

with open("test2.json", "w", encoding= "utf-8") as testfile:
    json.dump(languages, testfile)
    
# Read it back again
# Returns a list of lists again because of the way json stores the data
# json does not support tupples
with open("test2.json", "r", encoding= "utf-8") as testfile:
    data = json.load(testfile)

print(data)