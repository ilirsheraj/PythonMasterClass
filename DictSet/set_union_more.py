#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 02:14:37 2022

@author: ilirsheraj
"""
scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"} # sting, arachnids, venomous
snakes = {"python", "cobra", "viper", "anaconda", "mamba"} # bite, venomous
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"} # bite, arachnids, venomous
vasps = {"yellowjacket", "hornet", "paper wasp"} # sting

sting = scorpions | vasps
print(sting)
print()

arachnids = scorpions | spiders
print(arachnids)
print()

bite = snakes | spiders
print(bite)
print()

venomous = scorpions | snakes | spiders
print(venomous)