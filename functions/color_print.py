#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:14:06 2022

@author: ilirsheraj
"""
# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED, "This will be in red")

# The changes we made will stay until we cancel them
print("And so is this")
print(RESET, "And so is this")
print()

# Let's write a function to avoid manually resetting colors all the time
def colour_print(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI Sequences to change color
    
    param text: the text to print
    param effect: the effect we want. One of the constants defined
    at the start of this module
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)

colour_print("Hello, Red", RED)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)