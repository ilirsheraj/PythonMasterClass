#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 20:29:51 2022

@author: ilirsheraj
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 01:58:26 2022

@author: ilirsheraj
"""
lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
    }

# things = animals.copy()

# Manual copying
things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
    }

print(things["teddy"])
print(animals["teddy"])
print()

# Now things are different!
# things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("Added via 'animals'")
things["teddy"].append("Added via 'things'")

print(things["teddy"])
print(animals["teddy"])