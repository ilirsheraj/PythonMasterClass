#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 01:32:09 2022

@author: ilirsheraj
"""
import json

json_data_source = "temperature_anomaly.json"

with open(json_data_source, "r", encoding= "utf-8") as data:
    anomalies = json.load(data)
    
print(anomalies["description"])
print()

for year, value in anomalies["data"].items():
    year, value = int(year), float(value)
    print(f"{year} ... {value:6.2f}")
    
print("*"*80)

print(anomalies["citation"])