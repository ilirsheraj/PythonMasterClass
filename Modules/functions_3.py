def python_food():
	width = 80
	text = "Spam and Eggs"
	left_margin = (width - len(text)) // 2
	print(" " * left_margin, text)


# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
# 	text = ""
# 	for arg in args:
# 		text += str(arg) + sep
# 	left_margin = (80 - len(text)) // 2
# 	print(" " * left_margin, text, end=end, file=file, flush=flush)


# with open("centered", mode="w") as centered_file:
# 	centre_text("Spam and Eggs", file=centered_file)
# 	centre_text("spam, spam and eggs", file=centered_file)
# 	centre_text(12, file=centered_file)
# 	centre_text("spam, spam, spam and spam", file=centered_file)
# 	centre_text("first", "second", 3, 4, "spam", sep=":", file=centered_file)


# Use return in the function
def centre_text(*args, sep=' '):
	text = ""
	for arg in args:
		text += str(arg) + sep
	left_margin = (80 - len(text)) // 2
	return " " * left_margin + text


# s1 = centre_text("Spam and Eggs")
# print(s1)
# s2 = centre_text("spam, spam and eggs")
# print(s2)
# s3 = centre_text(12)
# print(s3)
# s4 = centre_text("spam, spam, spam and spam")
# print(s4)
# s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
# print(s5)
#
# print("=" + str(12*3))
# print(sorted(["b", "d", "c", "a"]))

with open("menu", "w") as menu:
	s1 = centre_text("Spam and Eggs")
	print(s1, file=menu)
	s2 = centre_text("spam, spam and eggs")
	print(s2, file=menu)
	print(centre_text(), file=menu)
	print(centre_text("spam, spam, spam and spam"), file=menu)
	s5 = centre_text("first", "second", 3, 4, "spam", sep=":")
	print(s5, file=menu)
