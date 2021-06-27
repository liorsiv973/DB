SELECT actorId, MAX(duration), MIN(duration), AVG(duration)
FROM movies NATURAL JOIN playsIn
GROUP BY actorId
ORDER BY actorId;