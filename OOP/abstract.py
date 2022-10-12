from abc import ABC, abstractmethod


# Create the parent (base) class
class Shape(ABC):

	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def perimeter(self):
		pass


# Create a sublass that inherits from Shape
class Square(Shape):
	def __init__(self, side):
		self.__side = side

	def area(self):
		return self.__side * self.__side

	def perimeter(self):
		return 4 * self.__side


# Instantiate the class
# myShape = Shape()  # Cannot create because of abstraction
mySquare = Square(5)
print(mySquare.area())
print(mySquare.perimeter())
