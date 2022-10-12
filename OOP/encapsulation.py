class Cars:
	def __init__(self, speed, color):
		self.speed = speed
		self.color = color

	def set_speed(self, value):
		"""
		It will be used to change the value of speed parameter whenever necessary
		"""
		self.speed = value

	def get_speed(self):
		"""
		Return the value of the speed
		"""
		return self.speed


ford = Cars(250, "green")
nissan = Cars(300, "red")
toyota = Cars(350, "blue")

# No encapsulation, so we can make changes
print(f"Speed of Ford before change is {ford.get_speed()}")
ford.set_speed(450)
# Now we can check the new value of ford's speed
print(f"Speed of Ford after change is {ford.get_speed()}")
# Change the value directly
ford.speed = 470
print(f"Speed of Ford after direct change is {ford.get_speed()}")
print(f"The color of Ford is {ford.color}")
