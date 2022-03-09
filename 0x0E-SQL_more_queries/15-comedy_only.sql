-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT `tv_shows`.`title` FROM `tv_shows`
JOIN `tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
JOIN `tv_genres` ON `tv_show_genres`.`genre_id` = `tv_genre`.`id`
WHERE `tv_genres`.`name` = "Dexter"
ORDER BY `tv_shows`.`title`;
