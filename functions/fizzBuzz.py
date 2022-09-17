#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:46:16 2022

@author: ilirsheraj
"""
# For this exercise, you'll write a function that returns the next answer, in the game of fizz buzz.
# It's a simple game, usually played with 2 or more people.
# You start counting, in turn. That's easy enough, but there's a complication.
# If the number is divisible by 3, you say "fizz" instead.
# If it's divisible by 5, you say "buzz".
# And if it's divisible by both 3 and 5, you say "fizz buzz".
# The function must be called fizz_buzz
# Your fizz_buzz function should return the correct word ("fizz", "buzz" or "fizz buzz"), or the number if it's not divisible by either 3 or 5.
# The function will always return a string. When you return the number, therefore, you should convert it to a string first.
# Remember to annotate your function, and include a Docstring.
# Include a for loop, to test your function for values from 1 to 100, inclusive.

def fizz_buzz(num: int) -> str:
    """
    The function takes in an integer and if it is divisible by 3, function returns "fizz"
    If the integer is divisible by 5, it returns "buzz"
    And if it is divisible by both 3 and 5, it returns "fizz buzz"
    Else, it returns the number in string format
    """
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


input("Paly Fizz Buzz. Press ENTER to start")
print()
next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    # players_answer = correct_answer
    players_answer = input("Your Go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well Done, you reached {}".format(next_number))