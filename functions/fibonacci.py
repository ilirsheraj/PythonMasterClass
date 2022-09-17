#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 02:29:53 2022

@author: ilirsheraj
"""
def fibonacci(n):
    """
    Return the n' th fibonacci number for positive `n`
    """
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1,0
    
    result = None
    
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
        
    return result


for i in range(36):
    print(i, fibonacci(i))