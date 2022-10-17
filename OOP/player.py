class Player(object):

	def __init__(self, name):
		self.name = name
		self._lives = 3
		self.level = 1
		self.score = 0

	def _get_lives(self):
		return self._lives

	def _set_lives(self, lives):
		if lives >= 0:
			self._lives = lives
		else:
			print("Lives cannot be negative")
			self._lives = 0

	lives = property(_get_lives, _set_lives)

	def __str__(self):
		""" A function to print out the values of the attributes """
		return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
