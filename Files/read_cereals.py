#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:03:34 2022

@author: ilirsheraj
"""
import csv

csv_filename = "cereal_grains.csv"

# with open(csv_filename, "r", encoding= "utf-8", newline='') as cereals:
#     data = csv.reader(cereals)
#     for rows in data:
#         print(rows) # Numerical values read as strings

# Fix numeric issue
with open(csv_filename, "r", encoding= "utf-8", newline='') as cereals:
    data = csv.reader(cereals, quoting = csv.QUOTE_NONNUMERIC) # Returns floats, not integers
    for rows in data:
        print(rows)
        
