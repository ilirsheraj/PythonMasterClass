#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 01:12:00 2022

@author: ilirsheraj
"""
# Define some functions
def removeprefix(string: str, prefix: str) -> str:
    """
    Removes the prefix form a string if it starts that way
    """
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]
    
def removesuffix(string: str, suffix: str) -> str:
    """
    Removes the suffix from a string
    
    suffix="" should not call string[:-0]
    """
    if suffix and string.endswith(suffix): # suffix="" should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]


# We will read only the first line
filename = "Jabberwocky.txt"
with open(filename) as poem:
    first = poem.readline().rstrip()
    
print(first)
print()

# # Let's strip the apostrophe
# # strip() strips from both ends of the string
# chars = "'"
# no_appostrophe = first.strip(chars)
# print(no_appostrophe)
# print()

# # We will rmeove `'Twas` but the last `s` will go as well
# # It keeps removing until no matching character from the target is found
# chars = "'Twas"
# no_appostrophe = first.strip(chars)
# print(no_appostrophe)
# print()


# # Now removes `'Twas` from left and `ves` from right because there is no `o` at the end
# chars = "'Twasebv"
# no_appostrophe = first.strip(chars)
# print(no_appostrophe)
# print()


# # One more example
# # Now removes `'Twas b` from left because of space, and `ves` from right because there is no `o` at the end
# chars = "' Twasebv"
# no_appostrophe = first.strip(chars)
# print(no_appostrophe)

# Use a for loop to make it more clear
print(first)
chars = "' Twasebv"
for character in first:
    if character in chars:
        print(f"removing {character}")
    else:
        break

print("*"*30)

chars = "' Twasebv"
for character in first[::-1]: # Process backwards
    if character in chars:
        print(f"removing {character}")
    else:
        break

print("*"*30)
# # Remove Prefix and Suffix
twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix("toves")
print(toves_removed)
print()
print("*"*30)

# Remove using functions
twas_removed = removeprefix(first, "'Twas")
print(twas_removed)
toves_removed = removesuffix(first, "toves")
print(toves_removed)