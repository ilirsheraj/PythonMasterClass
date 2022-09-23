#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 02:41:53 2022

@author: ilirsheraj
"""
# # Use intersection to find which patient is in more than one set
# trial_1 = {"Bob", "Charley", "Georgia", "John"}
# trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}


# check_set = trial_1.intersection(trial_2)
# print(check_set)

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(intersection)

# Do the same using method
mounts = farm_animals.intersection(wild_animals, potential_rides)
print(mounts)