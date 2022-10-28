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
artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30,0))
artistList.config(border=2, relief="sunken")

for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
	artistList.insert(tkinter.END, artist[0])

artistList.bind('<<ListboxSelect>>', get_albums)

# artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
# artistScroll.grid(row=1, column=0, sticky="nse", rowspan=2)
# artistList['yscrollcommand'] = artistScroll.set

# ==== Album Listbox ====
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an Artist",))
albumList = Scrollbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky="nsew", padx=(30,0))
albumList.config(border=2, relief="sunken")

# albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
# albumScroll.grid(row=1, column=1, sticky="nse", rowspan=2)
# albumList['yscrollcommand'] = albumScroll.set

# ==== Song Listbox ====
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose and Album",))
songList = Scrollbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky="nsew", padx=(30,0))
songList.config(border=2, relief="sunken")

# ==== Main Loop ====
testList = range(0, 100)
albumLV.set(tuple(testList))
mainWindow.mainloop()
print("Closing the Database Connection")
conn.close()
