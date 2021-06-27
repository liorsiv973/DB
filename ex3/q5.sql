WITH RECURSIVE T(a,actorid) AS
   (SELECT 0, actorId FROM actors WHERE name='Frank Bacon'
      UNION 
		SELECT a+1,P2.actorId
		FROM playsIn P1, playsIn P2, T
		WHERE a < 5 AND P1.actorId <> P2.actorId AND P1.movieId = P2.movieId AND T.actorId = P1.actorId)
SELECT DISTINCT actorId, name 
FROM T NATURAL JOIN actors
ORDER BY actorId;

