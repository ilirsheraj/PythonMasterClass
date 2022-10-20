-- Long commands used in SQLITE3
SELECT artists.name, albums.name, songs.track, songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
ORDER BY artists.name, albums.name, songs.track;


-- Select a specific album
SELECT artists.name, albums.name, songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE albums.name = "Doolittle"
ORDER BY artists.name, albums.name, songs.track;

-- Partial Matching: 
SELECT artists.name, albums.name, songs.track, songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE songs.title LIKE "%doctor%"
ORDER BY artists.name, albums.name, songs.track;

SELECT artists.name, albums.name, songs.track, songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
WHERE artists.name LIKE "%jefferson%"
ORDER BY artists.name, albums.name, songs.track;

-- Create a View of the Table
CREATE VIEW artist_list AS
SELECT artists.name, albums.name, songs.track, songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
ORDER BY artists.name, albums.name, songs.track;
.schema
SELECT * FROM artist_list;

-- To close the view use the following command
DROP VIEW artist_list;

-- Housekeeping
DELETE FROM songs WHERE track < 50;
SELECT * FROM songs;
SELECT * FROM artist_list;
SELECT * FROM songs WHERE track <> 71;
SELECT COUNT(*) FROM songs;
SELECT COUNT(*) FROM albums;
SELECT COUNT(*) FROM artists;

