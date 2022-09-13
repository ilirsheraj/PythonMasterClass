#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 01:45:21 2022

@author: ilirsheraj
"""
# Iterable: Anything you can iterate over __iter__ or __getitem__, indexing starts from zero
# Not all iterables are sequences, dictionary is such an example

computer_parts = ["computer", 
                  "monitor", 
                  "keyboard", 
                  "mouse", 
                  "mouse mat"
                  ]

for part in computer_parts:
    print(part)
print()
print(computer_parts[2])
print()

print(computer_parts[0:3])
print()
print(computer_parts[-1])