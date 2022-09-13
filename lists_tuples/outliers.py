#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 00:50:36 2022

@author: ilirsheraj
"""
# Create a list
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
print(data)
print()

# # delete from the beginning
# del data[0:2]
# print(data)
# print()

# # Delete from the end
# del data[14:]
# print(data)

## delete automatically to avoid indexing mistakes
## keep data from [100 to 200]
## change the index, you'll miss what you are trying to get because of index skipping
# min_valid = 100
# max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)

# Safely remove the data from ordered list
# Assume we cannot copy the list
min_valid = 100
max_valid = 200

# Process the low values from the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)
print()

# Process the high value data
# start = 0
# for index, value in enumerate(data):
#     if value >= max_valid:
#         start = index
#         break

# print(start)
# del data[start:]
# print(data)

# Another way (more efficient, backward iteration)
start = 0
for index in range(len(data) -1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item to keep
        # Set start to the position of the first
        # item to delete, which is 1 after the index
        start = index + 1
        break
    
print(start)
del data[start:]
print(data)