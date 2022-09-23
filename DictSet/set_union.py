#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 01:59:31 2022

@author: ilirsheraj
"""
# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

# # Union of the sets
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)
# print()

# # Order doesnt matter
# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)
# print()

# # Use or logical operator
# all_animals_3 = wild_animals | farm_animals
# print(all_animals_3)


from prescription_data import adverse_interactions

meds_to_watch = set()
# for interaction in adverse_interactions:
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction
# print(sorted(meds_to_watch))

meds_to_watch.update(*adverse_interactions)
print(meds_to_watch)
print(*sorted(meds_to_watch), sep = "\n")