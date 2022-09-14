#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 01:59:52 2022

@author: ilirsheraj
"""
data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]

min_valid = 100
max_valid = 200

# print(len(data))
# print(data)
# print()
# for index in range(len(data) - 1, -1, -1):
# #    print(index)
#     if data[index] < min_valid or data[index] > max_valid:
# #        print(index, data)
#         del data[index]
# print(data)

# Another more efficient way because of enumerate
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)