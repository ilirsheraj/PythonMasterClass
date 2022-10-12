class Cars:
	def __init__(self, speed, color):
		self.__speed = speed
		self.__color = color

	def set_speed(self, value):
		"""
		It will be used to change the value of speed parameter whenever necessary
		"""
		self.__speed = value

	def set_color(self, col):
		self.__color = col

	def get_speed(self):
		"""
		Return the value of the speed
		"""
		return self.__speed


ford = Cars(250, "green")
nissan = Cars(300, "red")
toyota = Cars(350, "blue")

print(f"Speed of Ford before change is {ford.get_speed()}")
ford.set_speed(450)
# Now we can check the new value of ford's speed
print(f"Speed of Ford after change is {ford.get_speed()}")
# Cannot change the value directly
ford.speed = 470
print(f"Speed of Ford after direct change is {ford.get_speed()}")
# Cannot change it because it is private
# print(f"The color of Ford is {ford.__color}")

# The only way to change the value is to use set_speed() or create new method for color
ford.set_color("black")
print(ford.__dict__)
