#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:49:10 2022

@author: ilirsheraj
"""
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
#                   "mouse mat",
                   "hdmi cable",
                   "dvd drive", 
                   "camera"
                   ]

# valid_choices = [str(i) for i in range(1,len(available_parts) +1)]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
# Create an empty list
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
        
    current_choice = input()

print(computer_parts)