def python_food():
	width = 80
	text = "Spam and Eggs"
	left_margin = (width - len(text)) // 2
	print(" " * left_margin, text)


# Call the function
# Since function has no return, it returns None
print(python_food())


def centre_text(text):
	text = str(text)
	left_margin = (80 - len(text)) // 2
	print(" " * left_margin, text)


centre_text("Spam and Eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")
