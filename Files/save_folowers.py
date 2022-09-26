#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 00:42:36 2022

@author: ilirsheraj
"""
# We will save this list on a new file
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
    ]

plants_filename = "flowers_print.txt"

with open(plants_filename, "w") as plants:
    for plant in data:
        print(plant, file = plants)
        
new_list = []

with open(plants_filename) as plants:
    for plant in plants:
        new_list.append(plant.rstrip())

print(new_list)