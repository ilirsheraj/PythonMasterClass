#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 22:07:28 2022

@author: ilirsheraj
"""
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:
    print("\tGuessing in the range of {} to {}".format(low,high))
    guess = low + (high - low)//2
    high_low = input("My guess is {}. Should i guess higher or lower? "
                     "Enter h or l, or c if my guess was correct ".
                     format(guess)).casefold()
    
    if high_low == "h":
        # Guess higher: Low end of the range becomes 1 greater than the guess
        # pass
        low = guess + 1
        
    elif high_low == "l":
        # High end of the range becomes one less than the guess
        # pass
        high = guess - 1
        
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    
    guesses += 1
    