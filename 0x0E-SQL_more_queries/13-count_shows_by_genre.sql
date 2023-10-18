-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT 
    name,
    COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
    ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;