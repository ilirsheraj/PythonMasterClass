#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 22:32:17 2022

@author: ilirsheraj
"""
from contents import pantry, recipes

# print(pantry)
# print()
# print(recipes)

# # Dictionary comprehension
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# print(display_dict)

# Lets do it the classical way
display_dict = {}
for index, key in enumerate(recipes):
#    print(index + 1, key)
    display_dict[str(index + 1)] = key
#    print(display_dict)
    
while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
        
    choice = input(": ")
    if choice == "0":
        break
    
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item in ingredients:
            if food_item in pantry:
                print(f"\t{food_item} OK")
            else:
                print(f"\tYou don't have a necessary ingredient: {food_item}")

    