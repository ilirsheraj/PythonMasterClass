#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 00:26:26 2022

@author: ilirsheraj
"""
age = 24
print("My age is " + str(age) + " years")
print()

# replacement fields and .format()
print("My age is {0} years".format(age))
print()

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print()

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))
print()

# Fields can be used more than once and index determines their order
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
print()

# Use tripple quotes
print("""Jan: {2}
      Feb: {0} 
      Mar: {2} 
      Apr: {1} 
      May: {2} 
      Jun: {1} 
      Jul: {2} 
      Sep: {1} 
      Oct: {2} 
      Nov: {1} 
      Dec: {2}""".format(28,30,31))
      
