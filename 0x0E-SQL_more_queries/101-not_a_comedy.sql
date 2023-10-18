-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT
    DISTINCT
        tv_shows.title
FROM tv_shows
JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name NOT IN(
    SELECT tv_genres.name
    FROM tv_genres
    JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
    JOIN tv_shows
        ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Comedy'
)
ORDER BY
    tv_shows.title,
    tv_genres.name
;