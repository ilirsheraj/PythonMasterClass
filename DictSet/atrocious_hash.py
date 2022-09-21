#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 00:04:10 2022

@author: ilirsheraj
"""
# In this module we will write a bad hashing function just to understand the concept

data = [
        ("orange", "a sweet, orange, citrus fruit"),
        ("apple", "good for making cider"),
        ("lemon", "a sour, yellow citrus fruit"),
        ("grape", "a small, sweet fruit growing in branches"),
        ("melon", "sweet and juicy"),
        ]

# # To get an integer from each letter using ord() built-in function
# # Every character is represented by a unique number
# print(ord("a"))
# print(ord("b"))
# print(ord("z"))

# # Let's run the hashing function
def simple_hash(s: str) -> int:
    """
    A ridiculously simple hashing function
    """
    basic_hash = ord(s[0])
    return basic_hash % 10


# for key, value in data:
#     h = simple_hash(key)
#     print(key, h)


# # Let's call the python built-in hash function and see whats happesn
# for key, value in data:
#     h = hash(key)
#     print(key, h)



def get(k: str) -> str:
    """
    Return the value of a key, or None if the key does not exist
    """
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


# We will create two lists
keys = [""] *10
values = keys.copy()    
    
for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key,h)
    keys[h] = key
    values[h] = value
    
print(keys)
print(values)
print()

value = get("lemon")
print(value)
print()
print(get("grape"))
print()
print(get("tomato"))
print()
print(get("bannana"))