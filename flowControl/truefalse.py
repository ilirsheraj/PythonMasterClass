#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:09:55 2022

@author: ilirsheraj
"""
# day = "Monday"
day = "Saturday"
temperature = 30
# raining = True
raining = False

# if day == "Saturday" and temperature > 27 and not raining:
#     print("Go Swimming")
# else:
#     print("Learn Python")
    
raining = True
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print("Learn Python")
