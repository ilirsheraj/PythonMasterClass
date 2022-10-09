class Song:
	"""
	Class to represent a song

	Attributes:
		title (str): The title of the song
		artist (Artist): The artist objects representing the song creator
		duration (int): The duration of the song in seconds. Could be zero
	"""

	def __int__(self, title, artist, duration=0):
		"""
		Song init method

		Args:
			title (str): Initializes the title attribute.
			artist (Artist): An Artist object representing the song's creator.
			duration (Optional [int]): Initial value for the `duration` attribute.
				Will default to zero if not specified
		"""
		self.title = title
		self.artist = artist
		self.duration = duration


class Album:
	"""
	Class to represent an Album using its track list

	Attributes:
		name (str): The name of the Album
		year (int): The year the album was released
		artist: (Artist): The artist responsible for the album
			If not specified, the artist will default to an artist with the name
			`Various Artists`
		tracks (List[Song]): A list of songs in the album

	Methods:
		add_song: used to build a new song to the album's track list
	"""

	def __init__(self, name, year, artist=None):
		self.name = name
		self.year = year
		if artist is None:
			self.artist = Artist("Various Artists")
		else:
			self.artist = artist
		self.tracks = []

	def add_song(self, song, position=None):
		"""
		Adds a song to the track list

		Args:
			song (Song): a song to add
			position (Optional[int]): If specified, the song will be added to that position
				in the track list - inserting it between other songs if necessary.
				Otherwise, the song will be added to the end of the list
		"""
		if position is None:
			self.tracks.append(song)
		else:
			self.tracks.insert(position, song)


class Artist:
	"""
	A basic class to store artist details

	Attributes:
		name (str): The name of the artist
		albums (List[Album]): A list of the album by this artist
			The list includes only those albums in this collection, it is
			not an exhaustible list of the artist's published albums

	Methods:
		add_album: Use to add a new album to the artist's album list
	"""

	def __init__(self, name):
		self.name = name
		self.albums = []

	def add_album(self, album):
		"""
		Add a new album to the list

		Args: album (Album): Album object to add to the list.
			If the album is already present, it will not be added again
			(although this is yet to be implemented)
		"""
		self.albums.append(album)
