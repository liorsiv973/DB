SELECT DISTINCT b1.Name, b1.Author, b1.Year 
FROM bestsellers b1, bestsellers b2
WHERE b1.name = b2.name AND (b1.author != b2.author or b1.genre != b2.genre or (b1.year = b2.year AND b1.rating != b2.rating)OR (b1.year = b2.year AND b1.price != b2.price) OR (b1.year = b2.year AND b1.Reviews != b2.Reviews))

ORDER BY Name, Year ASC
