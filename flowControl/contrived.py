#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 01:09:41 2022

@author: ilirsheraj
"""
# numbers = [1, 45, 31, 16, 60]

# for number in numbers:
#     if number %8 ==0:
#         # reject the list
#         print("The numbers are unacceptable")
#         break
# else:
#     print("All those numbers are fine")

# low = 1
# high = 1000

# print("Please think of a number between {} and {}".format(low, high))
# input("Press ENTER to start")

# guesses = 1
# while low != high:
#     print("\tGuessing in the range of {} to {}".format(low,high))
#     guess = low + (high - low)//2
#     high_low = input("My guess is {}. Should i guess higher or lower? "
#                      "Enter h or l, or c if my guess was correct ".
#                      format(guess)).casefold()
    
#     if high_low == "h":
#         # Guess higher: Low end of the range becomes 1 greater than the guess
#         # pass
#         low = guess + 1
        
#     elif high_low == "l":
#         # High end of the range becomes one less than the guess
#         # pass
#         high = guess - 1
        
#     elif high_low == "c":
#         print("I got it in {} guesses".format(guesses))
#         break
#     else:
#         print("Please enter h, l or c")
    
#     guesses += 1

# else:
#     print("You thought of the number {}".format(low))
#     print("I got it in {} guesses".format(guesses))

availabe_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in availabe_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over!")
        break
else:
    print("Aren't you glad you are out of there")