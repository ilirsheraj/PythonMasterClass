#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 02:49:48 2022

@author: ilirsheraj
"""
# Your task for this coding exercise is to find out which prepositions have been used in the quote:
# "Education is not the learning of facts but the training of the mind to think – Albert Einstein"
# There are two steps you'll need to perform:
# 1 - Split text to create a list of words.
# 2 - Create an intersection of the set of words with the prepositions set that we've provided in the exercise code.
# In order for the on-line checker to validate your solution, it's essential that you use the name preps_used for the intersection that you create.

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

text_split = set(text.split())
preps_used = prepositions.intersection(text_split)
print(preps_used)

preps_used2 = prepositions & text_split
print(preps_used2)
