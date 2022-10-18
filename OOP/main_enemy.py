from enemy import Enemy, Troll, Vampyre

# random_monster = Enemy("Basic Enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

# It inherits the default values of the superclass
# ugly_troll = Troll()
# print("Ugly troll - {}".format(ugly_troll))

# another_troll = Troll("Ug", 18, 1)
# print("Another troll - {}".format(another_troll))  #, end="")  # replace end of line with space
#
# brother = Troll("Urg", 23)
# print(brother)

# After changing in Troll subclass
ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(18)
print(another_troll)

brother = Troll("Urg")
print(brother)

# Make the trolls to grunt
ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

# monster = Enemy("Basic Enemy")
# # It wont work because Enemy has no grunt method
# monster.grunt()

vampyre1 = Vampyre("Dracula")
print(vampyre1)
vampyre1.take_damage(3)
print(vampyre1)

vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

print("-"*40)
another_troll.take_damage(30)
print(another_troll)
print("-" * 40)

while vamp.alive:
	vamp.take_damage(1)
	print(vamp)
