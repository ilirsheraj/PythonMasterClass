# There are two ways of importing the player class
# ## Way 1:
# import player
#
# tim = player.Player("Tim")
# print(tim.name)
# print(tim.lives)

# way 2: Generally not recommended because there is a single class in this case
from player import Player

# Now we don't need the file name, we just call the class directly
tim = Player("Tim")
print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim)
print()

tim.lives -= 1
print(tim)
print()

tim.lives -= 1
print(tim)
print()

tim.lives -= 1
print(tim)
print()

tim.lives = 9
print(tim)
print("-"*50)

tim.level = 2
print(tim)

tim.level += 5
print(tim)

tim.level = 3
print(tim)

tim.score = 500
print(tim)
