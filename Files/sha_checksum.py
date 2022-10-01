#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 18:48:56 2022

@author: ilirsheraj
"""
import hashlib

published_hash = '854bf444933e37f5824ae7bfc1e98d5bce2ebe4160d46b5edf346a89358e99da'

filename = 'colorama-0.4.5-py2.py3-none-any.whl'

with open(filename, 'rb') as downloaded_file:
    contents = downloaded_file.read()
    
file_hash = hashlib.sha3_256(contents).hexdigest()
print(file_hash)
print()

if file_hash != published_hash:
    print(f'The file {filename} has been modified')
else:
    print(f'file {filename} hash is correct')