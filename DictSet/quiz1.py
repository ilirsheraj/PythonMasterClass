#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:44:25 2022

@author: ilirsheraj
"""
# Your task for this coding exercise is to write some code to count the number 
# of times each character occurs in the given `text` string (see the starter code in exercise.py).
# You have to do this for every unique character in the given string. 
# Only count characters and digits - don't include spaces, punctuation or other symbols.
# When counting the characters, ignore case. For example, the string "Be bold" would have a count of 2 for the letter 'b'.
# Store the count in the `word_count` dictionary that has been declared for you, in the starter code.
# The key must be the character, and the value associated with this key should be the count of this particular character in the `text`.

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
 
# Your code goes here ...
for char in text.casefold():
    if char.isalnum():
        word_count[char] = word_count.setdefault(char,0) + 1


for letter, count in sorted(word_count.items()):
    print(letter, count)
print()


# Classical approach
word_count = {}
for char in text.casefold():
    if char.isalnum():
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
 
    
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)