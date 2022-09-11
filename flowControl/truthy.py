#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:29:18 2022

@author: ilirsheraj
"""
if 0: # 0 is evaluated to false
    print("True")
else:
    print("False")


name = input("Please enter your name: ")
if name:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name")
             