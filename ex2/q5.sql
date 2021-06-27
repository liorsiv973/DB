SELECT distinct P1.actorId as actorId1, P2.actorId as actorId2
FROM playsIn P1, playsIn P2
WHERE P1.movieId = P2.movieId and P1.actorId <> P2.actorId AND not exists (SELECT movieId
	FROM playsIn
	WHERE actorId = P2.actorId
EXCEPT
	SELECT movieId
	FROM playsIn
	WHERE actorId = P1.actorId
)
ORDER BY P1.actorId, P2.actorId;


