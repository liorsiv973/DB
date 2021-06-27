SELECT distinct name, character
FROM actors NATURAL JOIN playsIn
WHERE character LIKE 'George%'
ORDER BY name, character;