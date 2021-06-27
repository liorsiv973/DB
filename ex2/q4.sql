SELECT distinct actorId
FROM playsIn

EXCEPT

SELECT actorId
FROM playsIn NATURAL JOIN movies
WHERE rating <= 7 or rating is NULL

ORDER BY actorId;