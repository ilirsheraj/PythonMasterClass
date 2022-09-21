#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:06:45 2022

@author: ilirsheraj
"""
# Write a function to create a deep copy of a dictionary

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
    }


def deep_copy(dictn: dict) -> dict:
    """
    The functions takes a dictinary as an input and returns a deep copy
    """
    new_dict = {}
    
    for member, char in dictn.items():
        new_char = char.copy()
        new_dict[member] = new_char
    
    return new_dict


# d = deep_copy(animals)
# print(d)


# # Test the function
# d["teddy"].append("sweet")
# print(d)
# print()
# print(animals)
# print()

# animals["elephant"].append("Africa")
# print(animals)
# print(d)