#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:45:43 2022

@author: ilirsheraj
"""
# Store the file as variable
input_filename = "country_info.txt"

# Open the file
with open(input_filename) as country_file:
    for row in country_file:
        data = row.strip("\n").split("|")
        print(data)