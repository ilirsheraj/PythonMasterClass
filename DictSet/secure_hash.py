#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 01:03:43 2022

@author: ilirsheraj
"""
import hashlib

# print(sorted(hashlib.algorithms_guaranteed))
# print()
# print(sorted(hashlib.algorithms_available))

python_program = """for i in range(10):
    print(i)"""
    
print(python_program)

# for b in python_program.encode("utf8"):
#     print(b, chr(b))
    
original_hash = hashlib.sha256(python_program.encode("utf8"))
print(f"SHA256: {original_hash.hexdigest()}")

python_program += "print(code change)"
print(python_program)
print()

new_hash = hashlib.sha256(python_program.encode("utf8"))
print(f"SHA256: {new_hash.hexdigest()}")
print()

# Get program to check hashes for us
if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code has not been changed")
else:
    print("The code has been modified")
