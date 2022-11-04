-- lista all genres from hbtn_0d_tvshows and displays the nujmber of shows linked to them

SELECT tv_genres.name as genre, COUNT(*) as number_of_shows
FROM tv_genres
    INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY COUNT(*) DESC;