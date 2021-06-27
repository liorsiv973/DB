SELECT actorId, name
FROM actors 
WHERE actorId in (SELECT actorId FROM actors NATURAL JOIN movies NATURAL 					JOIN playsIn 
					GROUP BY actorId
					HAVING AVG(rating) = (SELECT max(a) FROM (SELECT AVG(rating) AS A FROM movies NATURAL JOIN playsIn
										GROUP BY actorId) RATE ))
ORDER BY actorId;
