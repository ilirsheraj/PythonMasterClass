class Tag(object):

	def __init__(self, name, contents):
		self.start_tag = "<{}>".format(name)
		self.end_tag = "<{}>".format(name)
		self.contents = contents

	def __str__(self):
		return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

	def display(self):
		print(self)


class DocType(Tag):
	
	def __init__(self):
		super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
		self.end_tag = ''  # DOCTYPE doesnt have any tag


class Head(Tag):

	def __init__(self):
		super().__init__("head", "")


class Body(Tag):

	def __init__(self):
		super().__init__("body", "")  # Body contents will be built up separately
		self._body_contents = []

	def add_tag(self, name, contents):
		new_tag = Tag(name, contents)
		self._body_contents.append(new_tag)

	def display(self):
		for tag in self._body_contents:
			self.contents += str(tag)

		super().display()