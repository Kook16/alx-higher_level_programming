-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv.title, gen.name
 FROM tv_shows AS tv
       LEFT JOIN tv_show_genres AS show
       ON tv.id = show.show_id
       LEFT JOIN tv_genres AS gen
       ON show.genre_id = gen.id
 ORDER BY tv.title, gen.name;
