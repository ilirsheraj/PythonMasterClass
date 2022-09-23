#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:53:17 2022

@author: ilirsheraj
"""
morning = {"Java", "C", "Ruby", "Lisp", "C#"}
afternoon = {"Python", "C#", "Java", "C", "Ruby"}

possible_courses = morning^afternoon
print(possible_courses)
print()

morning = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon = ["Python", "C#", "Java", "C", "Ruby"]

possible_courses = set(morning) ^ set(afternoon)
print(possible_courses)
print()

# With method we dont need to convert list into set
possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)