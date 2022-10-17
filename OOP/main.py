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
#
# # Using getter conventionally
# print(tim.get_name())
# # Using a setter conventionally
# tim.set_lives(300)
