import random


# class Enemy: This is the same as the line below with object in it, no difference
class Enemy(object):

	def __init__(self, name="Enemy", hit_points=0, lives=1):
		self.name = name
		self.hit_points = hit_points
		self.lives = lives
		self.alive = True

	def take_damage(self, damage):
		remaining_points = self.hit_points - damage
		if remaining_points >= 0:
			self.hit_points = remaining_points
			print("I took {} points damage and have {} left".format(damage, self.hit_points))
		else:
			self.lives -= 1
			if self.lives > 0:
				print("{0.name} lost a life".format(self))
			else:
				print("{0.name} is dead".format(self))
				self.alive = False

	def __str__(self):
		return "Name: {0.name}, Lives: {0.lives}, Hit Points: {0.hit_points}".format(self)


# Define a new enemy class called trolls
class Troll(Enemy):

	def __init__(self, name):
		# Enemy.__init__(self, name=name, lives=1, hit_points=23)
		# super(Troll, self).__init__(name=name, lives=1, hit_points=23)
		# THe line above and below do the same thing, so no need to specify them
		super().__init__(name=name, lives=1, hit_points=23)

	def grunt(self):
		print("Me {0.name}. {0.name} stomp you".format(self))


# Create a vampire subclass
# Vampyre has 3 lives and take 12 hit points of damage
class Vampyre(Enemy):
	def __init__(self, name):
		super().__init__(name=name, lives=3, hit_points=12)

	def dodges(self):
		if random.randint(1, 3) == 3:
			print("***** {0.name} dodges *****".format(self))
		else:
			return False

	def take_damage(self, damage):
		if not self.dodges():
			super().take_damage(damage=damage)
