-- lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, IFNULL(tv_show_genres.genre_id, 'NULL') ASC; 