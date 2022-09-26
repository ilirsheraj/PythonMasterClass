#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 00:06:54 2022

@author: ilirsheraj
"""
# Create a dictionary with two keys
# Store the file as variable
input_filename = "country_info.txt"
# Define an empty dictionary by country name
countries = {}

# Open the file
with open(input_filename) as country_file:
    # To exclude the first line use readline
    country_file.readline()
    
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
#        print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")

        country_dict = {
            "name": country,
            "capital": capital,
            "country_code": code,
            "cc3": code3,
            "dialing_code": dialing,
            "timezone": timezone,
            "currency": currency,
            }
#        print(country_dict)

        countries[country.casefold()] = country_dict
        
        # Introduce a second key to the dictionary
        countries[code.casefold()] = country_dict
        
# Get the name of a country from a user and display its capital city
while True:
    name = input("Please enter the name or code of a country or type 'quit' to exit: ")
    country_key = name.casefold()
    
    if country_key in countries:
        country_data = countries[country_key]
        if country_data["capital"] == "":
            print(f"{name} has no capital city")
        else:
#            print("The capital of {} is {}".format(name.capitalize(), country_data["capital"]))
            print(f"The capital of {name} is {country_data['capital']}")
        
    elif country_key == "quit":
        break
    else:
        print("This country does not exist")