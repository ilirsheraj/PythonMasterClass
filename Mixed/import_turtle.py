import turtle
import math


# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()  # Otherwise the lines disappear


def square(length: int) -> None:
	"""Draws a square of length 'length"""
	for side in range(4):
		turtle.forward(length)
		turtle.right(90)


def encircled_square(length: int) -> None:
	"""Draws a square of length `length`,
	 then encloses it in a circle
	 """
	square(length)
	angle = math.radians(45)
	radius = length * math.cos(angle)
	turtle.right(135)
	turtle.circle(radius)


# for s in range(72):
# 	square(120)
# 	turtle.left(5)

encircled_square(300)
turtle.done()
