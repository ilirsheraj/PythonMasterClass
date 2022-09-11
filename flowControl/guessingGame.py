#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 02:54:45 2022

@author: ilirsheraj
"""
answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time!")

# Let's make the code sexier

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than the answer!
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it the first time")
    
# Another way
if guess == answer:
    print("You got it the first time")
else:
    if guess > answer:
        print("Please guess lower")
    else:
        print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
