def spam1():

	def spam2():

		def spam3():
			z = " even"
			z += y
			print("In spam3, locals are {}".format(locals()))
			return z

		y = " more " + x #  y must exist before spam3 is called
		y += spam3()
		print("In spam 2, locals are {}".format(locals()))
		return y

	x = "spam " #  + spam2()
	x += spam2()
	print("In spam 1, locals are {}".format(locals()))
	return x


print(spam1())
# Locals and globals are identical in module scope
print(locals())
print(globals())
