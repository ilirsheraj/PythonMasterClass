#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 23:50:49 2022

@author: ilirsheraj
"""
import csv

# Do the same for country dictionary
input_filename = "country_info.txt"

dialect = csv.excel
dialect.delimiter = '|'

# custom_dialect = csv.Dialect(delimiter = '|')

# Initiate an empty dictionary
countries = {}
with open(input_filename,encoding="utf-8", newline="") as country_file:
    # Get the columns headings from first line of the file
    headings = country_file.readline().strip("\n").split(dialect.delimiter)
    print(headings)
    for index, heading in enumerate(headings):
        heading[index] = heading.casefold()
        
    dict_reader = csv.DictReader(country_file, dialect = dialect, fieldnames = headings)
    
    for row in dict_reader:
        countries[row["Country"].casefold()] = row
        countries[row["CC"].casefold()] = row
        
# Get the name of a country from a user and display its capital city
while True:
    name = input("Please enter the name or code of a country or type 'quit' to exit: ")
    country_key = name.casefold()
    
    if country_key in countries:
        country_data = countries[country_key]
        if country_data["Capital"] == "":
            print(f"{name} has no capital city")
        else:
#            print("The capital of {} is {}".format(name.capitalize(), country_data["capital"]))
            print(f"The capital of {name} is {country_data['Capital']}")
        
    elif country_key == "quit":
        break
    else:
        print("This country does not exist")