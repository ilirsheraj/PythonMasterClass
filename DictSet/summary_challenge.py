#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:46:23 2022

@author: ilirsheraj
"""
# Lets re-run the code created in section 2 to fix some bugs
# choice = "-"
# while choice != "0":
    
# #    if choice in list("12345"):
# #    We can use set() which is more efficient
#     if choice in set("12345"):
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


# Test membership
choice = "-"
while choice != "0":
    
    if choice in {"1", "2", "3", "4", "5"}:
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