#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 01:28:12 2022

@author: ilirsheraj
"""
available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive",
    }


current_choice = None # Inititalize to anything except 0 or valid choice
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
        
    else:
        print("Please add options from the list")
        for key, val in available_parts.items():
            print(f"{key}: {val}")
        print("0: to finish")
        
    current_choice = input("> ")