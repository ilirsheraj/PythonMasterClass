#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 01:58:41 2022

@author: ilirsheraj
"""
# Write a program to print a number of options and allow the user to select an 
# option from the list. OPtions to be numbered from 1-9, minimum 4 options

# print("Please choose your options from the list below:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo Swimming")
# print("4:\tHave Dinner")
# print("5:\tGo to bed")
# print("0:\tExit")

choice = "-"
# while True:
    
#     if choice == "0":
#         break
    
#     elif choice in "12345":
#         print("You chose {}".format(choice))
    
#     else:
#         print("Please choose your options from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo Swimming")
#         print("4:\tHave Dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")
    
#     choice = input()

while choice != "0":
    
    if choice in "12345":
        print("You chose {}".format(choice))
    
    else:
        print("Please choose your options from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave Dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
    
    choice = input()