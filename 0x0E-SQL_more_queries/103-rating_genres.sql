--  a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv.`title`, gen.`name`
  FROM `tv_shows` AS tv
       LEFT JOIN `tv_show_genres` AS show
       ON tv.`id` = show.`show_id`

       LEFT JOIN `tv_genres` AS gen
       ON show.`genre_id` = gen.`id`
  ORDER BY tv.`title`, gen.`name`;
