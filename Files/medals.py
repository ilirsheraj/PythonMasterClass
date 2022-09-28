#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 02:27:26 2022

@author: ilirsheraj
"""
# Import the csv module
import csv

csv_filename = "OlympicMedals_2020.csv"

# with open(csv_filename, encoding= "utf-8", newline= '') as csv_file:
#     # reader will be an object
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)

with open(csv_filename, encoding= "utf-8", newline= '') as csv_file:
    # Skip the first line contiaing column headers
    headers = csv_file.readline().strip('\n').split(',')
    print(f"Column headers: {headers}")
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)