CREATE INDEX ON playsIn({character})

EXPLAIN ANALYZE
SELECT actorId
FROM playsIn
WHERE character LIKE 'Sheriff'

