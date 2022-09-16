#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 02:59:07 2022

@author: ilirsheraj
"""
from nested_datas import albums

# Constants are named in capital letters (convention)
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
    print("Please choose your favorite album (Invalid choice exits)")
    for index, (title, artist, year, song) in enumerate(albums):
        print("{}: {}".format(index+1, title))
    
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break
    
    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))
    
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        
        print("Playing {}".format(title))
        
    print("="*40)