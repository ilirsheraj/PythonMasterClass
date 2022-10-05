# Add the option of multiple arguments using `*parameter`
# Not efficient, just for practice
def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
	text = ""
	for arg in args:
		text += str(arg) + sep
	left_margin = (80 - len(text)) // 2
	print(" " * left_margin, text, end=end, file=file, flush=flush)


centre_text("first", "second", 3, 4, "spam", sep=":")
