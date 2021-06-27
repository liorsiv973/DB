SELECT DISTINCT b1.Name, b1.Author, b1.Year 
FROM bestsellers b1, bestsellers b2
WHERE b1.Name = b2.Name AND (b1.Author <> b2.Author OR b1.Genre <> b2.Genre OR b1.Rating <> b2.Rating 
OR b1.Price <> b2.Price OR b1.Reviews <> b2.Reviews)

ORDER BY Name, Year ASC;
