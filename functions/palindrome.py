#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 21:23:32 2022

@author: ilirsheraj
"""
def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()

# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
    

# Create a new function called palindrome_sentence that ignores spaces, punctuation etc
# Some examples of palindrome sentences
## Was it a car, or a cat, i saw?
## Do geese see god?
## Desnes not far, Rafton sensed

# # My Version
# def palindrome_sentece(string):
#     sentence = []
#     for char in string.casefold():
#         if char not in " .,!?":
#             sentence.append(char)
#     return sentence[::-1] == sentence

# sen = input("Please enter a sentence to check: ")
# if palindrome_sentece(sen):
#     print("'{}' is a palindrome".format(sen))
# else:
#     print("'{}' is not a palindrome".format(sen))
    

# # Tim's version
# def palindrome_sentece(sentence):
#     string = ""
#     for char in sentence.casefold():
#         if char.isalnum():
#             string += char
#     print(string)        
#     return string[::-1] == string

# sen = input("Please enter a sentence to check: ")
# if palindrome_sentece(sen):
#     print("'{}' is a palindrome".format(sen))
# else:
#     print("'{}' is not a palindrome".format(sen))
    
# Let's have a function calling another function
def palindrome_sentece(sentence):
    string = ""
    for char in sentence.casefold():
        if char.isalnum():
            string += char
    print(string)        
    return is_palindrome(string)

sen = input("Please enter a sentence to check: ")
if palindrome_sentece(sen):
    print("'{}' is a palindrome".format(sen))
else:
    print("'{}' is not a palindrome".format(sen))