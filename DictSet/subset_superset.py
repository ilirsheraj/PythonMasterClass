#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 22:14:06 2022

@author: ilirsheraj
"""
animals = {"Turtle",
           "Horse",
           "Robin",
           "Python",
           "Swallow",
           "Hedgehog",
           "Wren",
           "Aardvak",
           "Cat",
           }

birds = {"Robin", "Swallow", "Wren"}

print(f"birds is a subset of animals: {birds.issubset(animals)}")
print(f"animals is a superset of birds: {animals.issuperset(birds)}")
print()
print(f"birds is a superset of animals: {birds.issuperset(animals)}")
print(f"animals is a subset of birds: {animals.issubset(birds)}")
print()

print(birds <= animals)
print(birds < animals)
print("*"*30)

garden_birds = {"Swallow", "Wren", "Robin"}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)
print("*"*30)

more_birds = {"Wren", "Buggie", "Swallow"}
print(garden_birds >= more_birds)