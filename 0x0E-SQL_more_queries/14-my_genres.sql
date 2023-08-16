-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT gen.`name`
       FROM `tv_genres` AS gen
       	    INNER JOIN `tv_show_genres` AS show
	    ON gen.`id` = show.`genre_id`

	    INNER JOIN `tv_shows` AS tv
	    ON tv.`id` = show.`show_id`
	    WHERE tv.`title` = 'Dexter'
       ORDER BY gen.`name`;
