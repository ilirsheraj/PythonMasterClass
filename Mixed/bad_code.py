area = 0


def area_of_square(length: float):
	global area
	area = length * length


area_of_square(30)
print(f"The area is {area}")
