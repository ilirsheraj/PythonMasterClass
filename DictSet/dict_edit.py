#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 00:14:45 2022

@author: ilirsheraj
"""
vehicles = {
    "dream": "Honda 250T",
    "roadster": "BMW R1100",
    "er5": "Kawasaki ER5",
    "can-am": "Bomardier Can-Am 250",
    "virago": "Yamaha XV250",
    "tenere": "Yamaha XT650",
    "jimny": "Suzuki Jimny 1.5",
    "fiesta": "Ford Fiesta Ghia 1.4",
    "roadster": "Triumph Street Triple", # duplicate key: replaces the first one
    }


# Add items to the dictionary
vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

for key, value in vehicles.items():
    print(key, value, sep = ": ")
print()
# CHange values in a dictionary
vehicles["virago"] = "Yamaha XV535"

for key, value in vehicles.items():
    print(key, value, sep = ": ")
print()

del vehicles["starfighter"]
for key, value in vehicles.items():
    print(key, value, sep = ": ")

# Trying to delete e key that doesnt exist crashes the program
# del vehicles["f1"]

# Ther is another way to do things
# Use pop to check whether the key exist by adding None, if it doesnt exist, it doesnt crash
vehicles.pop("f1", None)
result = vehicles.pop("f1", None)
print(result)
print()

# Provide a string
result = vehicles.pop("f1", "You wish! Sell the Larjet and you might afford a racing car")
print(result)
print()

# Use pop with keys that exist
plane = vehicles.pop("learjet")
print(plane)
print()

bike = vehicles.pop("tenere", "not present")
print(bike)