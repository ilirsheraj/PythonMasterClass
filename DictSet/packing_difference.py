#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:30:27 2022

@author: ilirsheraj
"""
travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
    }

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
    }

print("Please choose your mode of traveling: ")
for key, value in travel_mode.items():
    print("{}: {}".format(key, value))
    

mode = "-"
while mode not in travel_mode:
    mode = input("> ")
    

# We will use set difference to avoid iteration
if mode == "2":
    # # Traveling by plane, remove restricted items
    # for restricted_item in restricted_items:
    #     items.discard(restricted_item)
    # items -= restricted_items
    items.difference_update(restricted_items)


# Print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)