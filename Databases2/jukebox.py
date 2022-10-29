import sqlite3
import tkinter


conn = sqlite3.connect("music.sqlite")


class Scrollbox(tkinter.Listbox):

	def __init__(self, window, **kwargs):
		super().__init__(window, **kwargs)

		self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

	def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
		super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan,
					 columnspan=columnspan, **kwargs)
		self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
		self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

	def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
		super().__init__(window, **kwargs)

		self.cursor = connection.cursor()
		self.table = table
		self.field = field

		self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
		if sort_order:
			self.sql_sort = " ORDER BY " + ','.join(sort_order)
		else:
			self.sql_sort = " ORDER BY " + self.field

	def clear(self):
		self.delete(0, tkinter.END)

	def requery(self):
		print(self.sql_select + self.sql_sort)  # TODO delete this line
		self.cursor.execute(self.sql_select + self.sql_sort)

		# clear the listbox contents before reloading
		self.clear()
		for value in self.cursor:
			self.insert(tkinter.END, value[0])


def get_albums(event):
	lb = event.widget
	index = lb.curselection()[0]
	artist_name = lb.get(index),  # This is a tuple

	# Get the artist ID from the database row
	artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
	alist = []
	for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist =? ORDER BY albums.name", artist_id):
		alist.append(row[0])
	albumLV.set(tuple(alist))
	songLV.set(("Chose and album",))


def get_songs(event):
	lb = event.widget
	index = int(lb.curselection()[0])
	album_name = lb.get(index),

	# Get the artist ID from the database row
	album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
	alist = []
	for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", album_id):
		alist.append(x[0])
	songLV.set(tuple(alist))


mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry("1024x768")

# ==== Column Configuration ====
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)  # spacer column on the right

# ==== Row Configuration ====
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ==== Labels ====
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ==== Artists Listbox ====
artistList = DataListBox(mainWindow, conn, "artists", "name")
artistList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30,0))
artistList.config(border=2, relief="sunken")

# for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
# 	artistList.insert(tkinter.END, artist[0])
artistList.requery()
artistList.bind('<<ListboxSelect>>', get_albums)

# artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
# artistScroll.grid(row=1, column=0, sticky="nse", rowspan=2)
# artistList['yscrollcommand'] = artistScroll.set

# ==== Album Listbox ====
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an Artist",))
albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
albumList.requery()
albumList.grid(row=1, column=1, sticky="nsew", padx=(30,0))
albumList.config(border=2, relief="sunken")

albumList.bind('<<ListboxSelect>>', get_songs)

# albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
# albumScroll.grid(row=1, column=1, sticky="nse", rowspan=2)
# albumList['yscrollcommand'] = albumScroll.set

# ==== Song Listbox ====
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose and Album",))
songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
songList.requery()
songList.grid(row=1, column=2, sticky="nsew", padx=(30,0))
songList.config(border=2, relief="sunken")

# ==== Main Loop ====
testList = range(0, 100)
albumLV.set(tuple(testList))
mainWindow.mainloop()
print("Closing the Database Connection")
conn.close()
