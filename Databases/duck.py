class Wing(object):

	def __init__(self, ratio):
		self.ratio = ratio

	def fly(self):
		if self.ratio > 1:
			print("Wee, this is fun!")
		elif self.ratio == 1:
			print("This is hard work, but I'm flying")
		else:
			print("I think I'll just walk")


class Duck(object):

	def __init__(self):
		self._wing = Wing(1.8)

	def walk(self):
		print("Waddle, waddle, waddle")

	def swim(self):
		print("Come on it, the water's lovely!")

	def quack(self):
		print("Quack quack!")

	def fly(self):
		self._wing.fly()


class Penguin(object):

	def walk(self):
		print("Waddle, waddle, I waddle too")

	def swim(self):
		print("Come on in, but it's a bit chilly this far South")

	def quack(self):
		print("Are you 'ayin' a larf? I'm a penguin!")


class Flock(object):

	def __init__(self):
		self.flock = []

	def add_duck(self, duck: Duck) -> None:
		self.flock.append(duck)

	def migrate(self):
		for duck in self.flock:
			duck.fly()


if __name__ == "__main__":
	donald = Duck()
	donald.fly()
