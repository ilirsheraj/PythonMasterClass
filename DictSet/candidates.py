#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 22:30:54 2022

@author: ilirsheraj
"""
required_skills = ["python", "github", "linux"]

candidates = {
    "anna": {"java", "linux", "windows", "github", "python", "full stack"},
    "bob": {"github", "linux", "python"},
    "carol": {"linux", "javascript", "html", "python", "github"},
    "daniel": {"pascal", "java", "c++", "github"},
    "ekani": {"html", "css", "github", "python", "linux"},
    "fenna": {"linux", "pascal", "java", "c", "lisp", "modula-2", "pearl", "github"},
    }

# check the skills for each candidate to decide whether to hire them
interviwees = set()
for candidate, skills in candidates.items():
#    print(candidate, skills)
    if skills.issuperset(required_skills):
        interviwees.add(candidate)
        
print(interviwees)

# Subset vs proper superset
interviwees = set()
for candidate, skills in candidates.items():
    # Proper superset
    if skills > set(required_skills):
        interviwees.add(candidate)
        
print(interviwees)
