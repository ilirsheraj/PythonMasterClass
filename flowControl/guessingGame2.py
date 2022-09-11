#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 21:18:39 2022

@author: ilirsheraj
"""
# Get the computer to geenrate a random number between 1 to 10
import random
highest = 10
answer = random.randint(1, highest)
# print(answer) # TODO: Remove after testing

# print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())


# if guess == answer:
#     print("You got it the first time")
# else:
#     if guess > answer:
#         print("Please guess lower")
#     else:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")

# Use a while loop to keep the program asking till oyu get it right
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0 # Initialize to any number that doesnt equal the valid answer
while guess != answer:
    guess = int(input())
    
    if guess == 0:
        break
    
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess > answer:
            print("Please guess lower")
        else:
            print("Please guess higher")
