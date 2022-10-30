import os
import fnmatch
import id3reader_p3 as id3reader


# def find_music(start, extension):
# 	for path, directories, files in os.walk(start):
# 		for file in fnmatch.filter(files, "*.{}".format(extension)):
# 			yield os.path.join(path, file)
#
#
# for f in find_music("music", "emp3"):
# 	print(f)


# # Use Absolute Path
# def find_music(start, extension):
# 	for path, directories, files in os.walk(start):
# 		for file in fnmatch.filter(files, "*.{}".format(extension)):
# 			absolute_path = os.path.abspath(path)  # create absolute path
# 			yield os.path.join(absolute_path, file)
#
#
# for f in find_music("music", "emp3"):
# 	print(f)


def find_music(start, extension):
	for path, directories, files in os.walk(start):
		for file in fnmatch.filter(files, "*.{}".format(extension)):
			absolute_path = os.path.abspath(path)  # create absolute path
			yield os.path.join(absolute_path, file)


# Create a generator with a for loop
my_music_files = find_music("music", "emp3")

# Create an empty list to store problematic file names
error_list = []

for f in my_music_files:
	try:
		id3 = id3reader.Reader(f)
		print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
			id3.get_value("performer"),
			id3.get_value("album"),
			id3.get_value("track"),
			id3.get_value("title")
		))
	except:
		error_list.append(f)

for error_file in error_list:
	print(error_file)
