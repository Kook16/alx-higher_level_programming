SELECT
    tv_genres.name,
    SUM(rate) AS rating
FROM
    tv_show_ratings,
    tv_shows,
    tv_genres,
    tv_show_genres
WHERE
    tv_shows.id = tv_show_ratings.show_id
    AND tv_shows.id = tv_show_genres.show_id
    AND tv_genres.id = tv_show_genres.genre_id
GROUP BY
    tv_genres.id
ORDER BY
    rating DESC,
    tv_genres.name ASC;