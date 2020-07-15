-- My genres
SELECT tv_genres.name
FROM tv_show_genres
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE show_id = 8
ORDER BY tv_genres.name ASC;
