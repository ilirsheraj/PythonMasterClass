#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 02:12:27 2022

@author: ilirsheraj
"""
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
    ]

for name, artist, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}, Songs {}"
          .format(name, artist, year, songs))
print()

album = albums[3]
print(album)
print()

songs = album[3]
print(songs)
print()

song = songs[2]
print(song)
print(song[1])
print()

# Do everything at once
mayhem = albums[3][3][2][1]
print(mayhem)
print("*"*50)

print(albums[3])
print()
print(albums[3][3])
print()
print(albums[3][3][2])
print()
print(albums[3][3][2][1])
print()

# Quiz
# Use nested indexing to print the following items from our albums structure.
# The title of the song "The Way I Choose" from the "Bad Company" album.
print(albums[1][3][5][1])
print()
# The year that the album "Nightflight" was released.
print(albums[2][2])
print()
# The track number of the song "Kentish Town Waltz" from the Imelda May album "More Mayhem".
print(albums[3][3][3][0])
print()
# The tuple representing the song "Keeping a Rendezvous" from the Budgie album "Nightflight".
print(albums[2][3][1])