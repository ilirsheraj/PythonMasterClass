#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:12:58 2022

@author: ilirsheraj
"""
import csv

input_filename = "country_info.txt"

# with open(input_filename, encoding= "utf-8", newline= "") as countries_data:
#     country_reader = csv.reader(countries_data, delimiter = "|")
#     for row in country_reader:
#         print(row)

# Work out the separaters automatically
with open(input_filename, encoding= "utf-8", newline= "") as countries_data:
    # Make it more efficient with 2-3 lines only, no need to read the entire file
    sample = ""
    for line in range(3):
        sample += countries_data.read() # Reads entire content, reaching the end of it
    country_dialect = csv.Sniffer().sniff(sample) # Sniffer finds out data delimiter
    country_dialect.skipinitialspace = True # Remove space on the left
    countries_data.seek(0) # Start at position 0
    country_reader = csv.reader(countries_data, dialect = country_dialect)
    for row in country_reader:
        print(row)
        
print("*"*80)
print()

attributes = ["delimiter",
              "doublequote",
              "escapechar",
              "lineterminator",
              "quotechar",
              "quoting",
              "skipinitialspace",
              ]

for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")