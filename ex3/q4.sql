SELECT COUNT(actorId) AS num
FROM(
		SELECT actorId
		FROM Actors
		EXCEPT
		SELECT actorId
		FROM (
				SELECT movieId
				FROM PlaysIn
				GROUP BY movieId
				HAVING COUNT(actorId) <6) AS SIXACT NATURAL JOIN playsIn		
	) T;