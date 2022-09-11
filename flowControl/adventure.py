#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:19:25 2022

@author: ilirsheraj
"""
availabe_exits = ["north", "south", "east", "west"]

chosen_exit = ""

# while chosen_exit not in availabe_exits:
#     chosen_exit = input("Please choose a direction: ")
    
# print("Aren't you glad you are out of there")

# while chosen_exit not in availabe_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game Over!")
#         break
    
# print("Aren't you glad you are out of there")

for i in range(0, 100, 7):
    print(i)
    if i> 0 and i%11 == 0:
        break

print()

# Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5.
for i in range(21):
    if i == 0 or (i%3 == 0 or i%5 == 0):
        continue
    print(i)