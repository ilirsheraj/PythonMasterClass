class Duck(object):

	def walk(self):
		print("waddle, waddle, waddle")

	def swim(self):
		print("Come on it, the water's lovely")

	def quack(self):
		print("Quack quack")


class Penguin(object):

	def walk(self):
		print("waddle, waddle, waddle")

	def swim(self):
		print("Come on it, but it's a bit chilly this far South")

	def quack(self):
		print("Are you 'avin' a larf? I'm a penguin")


def test_duck(duck):
	duck.walk()
	duck.swim()
	duck.quack()


if __name__ == "__main__":
	donald = Duck()
	test_duck(donald)

	percy = Penguin()
	test_duck(percy)