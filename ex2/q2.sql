SELECT distinct movieID, title
FROM actors NATURAL JOIN movies NATURAL JOIN playsIn
WHERE year = dyear and (genre = 'Documentary' or genre = 'Drama')
ORDER BY movieId, title;