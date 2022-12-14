#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:44:31 2022

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
    }


# # Index dictionaries using the key
# my_car = vehicles["fiesta"]
# print(my_car)
# print()

# commuter = vehicles["virago"]
# print(commuter)
# print()

# learner = vehicles.get("er5")
# print(learner)

# learner = vehicles.get("ER5") # Returns None
# print(learner)

for key in vehicles:
    print(key)
print()


# Iterate key + value
for key in vehicles:
    print(key, vehicles[key])
print()


# make it better
for key in vehicles:
    print("{}: {}".format(key, vehicles[key]))
print()


# Another way using sep
for key in vehicles:
    print(key, vehicles[key], sep="; ")
print()


# Make it more efficient
for key, value in vehicles.items():
    print(key, value, sep = ": ")