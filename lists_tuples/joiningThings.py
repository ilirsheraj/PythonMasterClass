#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 02:28:15 2022

@author: ilirsheraj
"""
flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hyrdangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
    ]
print(flowers)
print()

# for flower in flowers:
#     print(flower)

separator = " | "
separator = ", "
output = separator.join(flowers)
print(output)
print()

print(",".join(flowers))