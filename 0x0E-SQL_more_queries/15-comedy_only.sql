-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.

-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement

SELECT tv.`title`
  FROM `tv_shows` AS tv
       INNER JOIN `tv_show_genres` AS show
       ON tv.`id` = show.`show_id`

       INNER JOIN `tv_genres` AS gen
       ON gen.`id` = show.`genre_id`
       WHERE gen.`name` = "Comedy"
 ORDER BY tv.`title`;
