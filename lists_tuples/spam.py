#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 00:22:59 2022

@author: ilirsheraj
"""
menu = [
        ["egg", "bacon"], 
        ["egg", "sausage", "bacon"], 
        ["egg", "spam"], 
        ["egg", "bacon", "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
        ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"]
        ]

# Print only the lists not containing spam
for meal in menu:
    if "spam" not in meal:
        print(meal)
        
        for item in meal:
            print(item)
    
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))