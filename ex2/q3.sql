SELECT distinct actorId
FROM (
	SELECT movieId
	FROM actors NATURAL JOIN playsIn NATURAL JOIN movies
	WHERE name LIKE 'Charles Chaplin'
	) AS chaplin NATURAL JOIN playsIn

INTERSECT

SELECT actorId
FROM playsIn NATURAL JOIN movies
WHERE duration > 90

ORDER BY actorId;