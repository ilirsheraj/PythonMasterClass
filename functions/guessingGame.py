#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 21:18:39 2022

@author: ilirsheraj
"""
# Get the computer to geenrate a random number between 1 to 10
# import random


# def get_integer(prompt):
#     while True:
#         temp = input(prompt)
#         if temp.isnumeric():
#             return int(temp)
# #        else:
#         print("{} is not a valid number".format(temp))

# highest = 1000
# answer = random.randint(1, highest)
# # print(answer) # TODO: Remove after testing
# guess = 0 # Initialize to any number that doesnt equal the valid answer
# print("Please guess a number between 1 and {}: ".format(highest))

# while guess != answer:
#     guess = get_integer(": ")
    
#     if guess == 0:
#         break
    
#     if guess == answer:
#         print("Well done, you guessed it")
#         break
#     else:
#         if guess > answer:
#             print("Please guess lower")
#         else:
#             print("Please guess higher")

# Quiz
# In this coding exercise, you have to write a function named sum_eo with the following parameters:
# n: a positive number
# t: a str
# If t has the value 'e', the function should return the sum of all even natural numbers less than n.
# Else if t has the value 'o', the function should return the sum of all odd natural numbers less than n.
# For any other values of t return -1.

def sum_eo(n, t):
    """
    n: a positive number
    t: a str
    If t has the value 'e', the function should return the sum of all even natural numbers less than n.
    Else if t has the value 'o', the function should return the sum of all odd natural numbers less than n.
    For any other values of t return -1.
    """
    if t == "e":
        return sum(range(2, n, 2))
    elif t == "o":
        return sum(range(1, n, 2))
    else:
        return -1
    
print(sum_eo(10, "e"))
print(sum_eo(10, "o"))
print(sum_eo(10, "eab"))
print(sum_eo(0, "e"))
