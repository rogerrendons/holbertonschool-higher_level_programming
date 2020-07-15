-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genres.name, tv_show_genres.genre_id WHERE tv_show_genres.genre_id = tv_genres.id;
