#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:38:09 2022

@author: ilirsheraj
"""
parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")