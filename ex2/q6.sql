SELECT distinct movieId, title
FROM movies M1 NATURAL JOIN playsin P1 NATURAL JOIN actors
WHERE 60 + byear < any (SELECT distinct byear FROM movies M2 NATURAL JOIN playsin NATURAL JOIN actors
WHERE M1.movieId = M2.movieId)
ORDER BY movieId, title;






