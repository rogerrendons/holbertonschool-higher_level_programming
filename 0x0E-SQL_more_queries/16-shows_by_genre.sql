-- Show genres 
-- in show
SELECT tv_shows.title, tv_genres.name FROM tv_genres RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id ORDER by tv_shows.title;