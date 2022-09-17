#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 00:14:47 2022

@author: ilirsheraj
"""
numbers = (0, 1, 2, 3, 4, 5)

print(numbers, sep=";")
print(*numbers, sep=";")
print(0, 1, 2, 3, 4, 5, sep=";")
print()


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)
print()


test_star()
