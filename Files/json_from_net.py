#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 01:56:15 2022

@author: ilirsheraj
"""
import json

# Library for opening URLs
import urllib.request

json_data_source = "https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/ytd/12/1880-2021/data.json"

with urllib.request.urlopen(json_data_source) as json_stream:
    data = json.load(json_stream) #.decode("utf-8")
#    anomalies = json.load(data)
    
print(data["description"])
print()

for year, value in data["data"].items():
    year, value = int(year), float(value)
    print(f"{year} ... {value:6.2f}")
    
print("*"*30)
# citation does not exist, so lets remove it
#print(data["citation"])