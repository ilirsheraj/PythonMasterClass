class Song:
	"""
	Class to represent a song

	Attributes:
		title (str): The title of the song
		artist (Artist): An artist object representing the song's creator
		duration (int): The duration of the dong in seconds (defaults to zero)
	"""

	def __init__(self, title, artist, duration):
		"""
		Song init method

		Args:
			title (str): Initializes the `title` attribute
			artist (Artist): Adds artist object representing the song's creator
			duration Optional([int]): Initial value of the `duration` attribute.
				It will default to zero if not specified
		"""
		self.title = title
		self.artist = artist
		self.duration = duration


# To see the docstring of the song
help(Song)
print("-" * 50)
# Print information only for the init method, not the entire class
help(Song.__init__)
print("-" * 50)
# We can also use the doctring of the class
print(Song.__doc__)
print("-" * 50)
# Another way to get the init docstring only
print(Song.__init__.__doc__)

# Another way to add documentation to the init method
# Song.__init__.__doc__ = """ Song init method
#
# 		Args:
# 			title (str): Initializes the `title` attribute
# 			artist (Artist): Adds artist object representing the song's creator
# 			duration Optional([int]): Initial value of the `duration` attribute.
# 				It will default to zero if not specified
# 		"""
# help(Song)
