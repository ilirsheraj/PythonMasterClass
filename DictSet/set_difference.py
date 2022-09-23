#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:26:12 2022

@author: ilirsheraj
"""
from primers_and_squares import squares_generator, primes_generator

evens = set(range(0,50,2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

# Generate some more sets
primes = set(primes_generator(100))
print(primes)

squares = set(squares_generator(100))
print(squares)
print()


print(odds.difference(primes))
print(odds - primes)
print(primes - odds)