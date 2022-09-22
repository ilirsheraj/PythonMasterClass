#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:20:42 2022

@author: ilirsheraj
"""
farm_animals = {"cow", "sheep", "hen", "goat", "horse"}
print(farm_animals)
print(type(farm_animals))
print()

for animal in farm_animals:
    print(animal)
print()

print("Indexing a Sequence")
animals_list = ["cow", "sheep", "hen", "goat", "horse"]
goat = animals_list[3]
print(goat)
print()

# print("INdexing a set is not possible")
# goat = farm_animals[3]
# print(goat)
# # 'set' object is not subscriptable

more_animals = {"sheep", "goat", "cow", "horse", "hen"}
if more_animals == farm_animals:
    print("The sets are equal")
else:
    print("The sets are different")