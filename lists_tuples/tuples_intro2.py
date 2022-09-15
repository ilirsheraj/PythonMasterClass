#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 01:00:52 2022

@author: ilirsheraj
"""
# Album, Artist, Year it was released
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)

# Indexing the tuple
print(metallica[0])
print(metallica[1])
print(metallica[2])

# Tuples are immutable
# metallica[0] = "Master of Puppets" (error)

# convert tuple to list
metallica2 = list(metallica)
print(metallica2)
# Lists are mutable
metallica2[0] = "Master of Puppets"
print(metallica2)
