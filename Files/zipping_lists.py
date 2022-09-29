#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 01:17:10 2022

@author: ilirsheraj
"""
import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ["album", "artist", "year"]

# List of tuples
for row in albums:
    zip_object = zip(keys, row)
    print(zip_object)
    for thing in zip(keys, row):
        print("\t", thing)
        
print()

for row in albums:
    zip_object = zip(keys, row)
    albums_dict = dict(zip_object)
    print(albums_dict)
    
print()


filename = "albums.csv"
with open(filename, 'w', encoding= 'utf-8', newline= '') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames= keys)
    writer.writeheader()
    for row in albums:
        zip_object = zip(keys, row)
        albums_dict = dict(zip_object)
        print(albums_dict)
        writer.writerow(albums_dict)