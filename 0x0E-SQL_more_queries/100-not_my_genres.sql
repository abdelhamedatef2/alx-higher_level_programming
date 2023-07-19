-- list genre not genre of dexter
-- list genere not genre of dexter
SELECT tv_genres.name FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
AND tv_show_genres.show_id = (
	SELECT id FROM tv_shows
	WHERE title = 'Dexter')
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_genres.name ASC;
