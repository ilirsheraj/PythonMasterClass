-- SQL Exercises
-- 1 - Select the titles of all the songs on the album "Forbidden"
SELECT songs.title FROM songs 
INNER JOIN albums ON songs.album = albums._id
WHERE albums.name = "Forbidden";

-- 2 - Repeat the previous query but this time display the songs in track order. You may want to include track number in the output to verufy that it worked
SELECT songs.track, songs.title FROM songs 
INNER JOIN albums ON songs.album = albums._id
WHERE albums.name = "Forbidden"
ORDER BY songs.track;

-- 3 - Display all songs for the band "Deep Purple"
SELECT songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name = "Deep Purple";

SELECT * FROM artist_list WHERE artist = "Deep Purple";

-- 4 - Rename the band Mehitabel tp "One Kitten"
UPDATE artists SET name = "One Kitten" WHERE artists.name = "Mehitabel";

-- 5 - Check that the record was correctly renamed
SELECT * FROM artists WHERE artists.name = "One Kitten";

-- 6 - Select the titles of all the songs by Aerosmith in alphabetical order. Include only the title in the output


-- 7 - Replace the column that you used in the previous answer with count(title) to get just a count of the number of songs

-- 8 - Get songs without duplicates


