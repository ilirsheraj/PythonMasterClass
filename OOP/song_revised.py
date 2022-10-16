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
		add_song: used to add a new song to the album's track list
	"""

	def __init__(self, name, year, artist=None):
		self.name = name
		self.year = year
		if artist is None:
			self.artist = Artist("Various Artists")
		else:
			self.artist = artist
		self.tracks = []  # Start with an empty list

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


def find_object(field, object_list):
	"""
	Check `object_list` to see if an object with a `name` attribute
	equal to `field` already exists. Return it if so
	"""
	for item in object_list:
		if item.name == field:
			return item
	return None


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
				artist_list.append(new_artist)
			elif new_artist.name != artist_field:
				# We have just read details of a new artist
				# retrieve the artist object if there is one
				# otherwise create a new artist object and add itt o the artists list
				new_artist = find_object(artist_field, artist_list)
				if new_artist is None:
					new_artist = Artist(artist_field)
					artist_list.append(new_artist)
				new_album = None

			if new_album is None:
				new_album = Album(artist_field, album_field, year_field)
				new_artist.add_albums(new_album)
			elif new_album.name != album_field:
				# We have just read a new album from the current artist
				# Retrieve the album object if there is one
				# Otherwise create a bew album object and store it in the artists' collection
				new_album = find_object(album_field, new_artist.albums)
				if new_album is None:
					new_album = Album(album_field, year_field, new_artist)
					new_artist.add_albums(new_album)

			# Create a new song object and add it to the current albums collection
			new_song = Song(song_field, new_artist)
			new_album.add_song(new_song)

	return artist_list


# Define a function called create_checkfile that will take as input the artists list
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
	print("-" * 50)

	create_checkfile(artists)
