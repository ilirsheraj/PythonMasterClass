class Song:
	"""
	Class to represent a song

	Attributes:
		title (str): The title of the song
		artist (Artist): The artist objects representing the song creator
		duration (int): The duration of the song in seconds. Could be zero
	"""

	def __init__(self, title, artist, duration=0):
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
		tracks (List[Song]): A list of songs on the album

	Methods:
		add_song: used to build a new song to the album's track list
	"""

	def __init__(self, name, year, artist=None):
		self.year = year
		self.name = name
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

	def add_albums(self, album):
		"""
		Add a new album to the list

		Args: album (Album): Album object to add to the list.
			If the album is already present, it will not be added again
			(although this is yet to be implemented)
		"""
		self.albums.append(album)


# Create a function to load the data
def load_data():
	new_artist = None
	new_album = None
	artist_list = []
	with open("albums.txt", "r") as albums:
		for line in albums:
			# data row should consist of (artist, album, year, song)
			artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
			year_field = int(year_field)
			print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

			if new_artist is None:
				new_artist = Artist(artist_field)
			elif new_artist.name != artist_field:
				# We have just read details of a new artist
				# Store the current album in the current artists collection then create a new artist object
				new_artist.add_albums(new_album)
				artist_list.append(new_artist)
				new_artist = Artist(artist_field)
				new_album = None

			if new_album is None:
				new_album = Album(artist_field, album_field, year_field)
			elif new_album.name != album_field:
				# We have just read a new album from the current artist
				# Store the current album in the artists collection and then create a new album object
				new_artist.add_albums(new_album)
				new_album = Album(album_field, year_field, new_artist)

			# Create a new song object and add it to the current albums collection
			new_song = Song(song_field, new_artist)
			new_album.add_song(new_song)

		# After reading the last line of the text file, we are going to have an artist and album that
		# haven't been stored, and we will process them now
		if new_artist is not None:
			if new_album is not None:
				new_artist.add_albums(new_album)
			artist_list.append(new_artist)

	return artist_list


# Define a function
def create_checkfile(artist_list):
	"""
	Create a check file from the object data for comparison with the original file
	"""
	with open("checkfile.txt", "w") as checkfile:
		for new_artist in artist_list:
			for new_album in new_artist.albums:
				for new_song in new_album.tracks:
					print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)


if __name__ == '__main__':
	artists = load_data()
	print("There are {} artists".format(len(artists)))

	create_checkfile(artists)
