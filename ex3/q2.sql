SELECT movieid, title
FROM actors NATURAL JOIN movies NATURAL JOIN playsIn
GROUP BY movieid
HAVING AVG(movies.year- actors.byear) >= 70
ORDER BY movieid;
