#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 02:33:56 2022

@author: ilirsheraj
"""
from content_quantities import pantry, recipes

# Create a function fo items to buy
def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Add a tuple containing `item` and `amount` to the data dictionary.
    """
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    # Use a default method
    data[item] = data.setdefault(item,0) + amount
    

# Create a dictionary
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key


# Create an empty list for items we need to buy
shopping_list = {}
# Start a while loop
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
        for food_item, required_quantity in ingredients.items():
            # Use default value with get to avoid crashing of the program
            quantity_in_pantry = pantry.get(food_item, 0) 
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)
                
for things in shopping_list.items():
    print(things)