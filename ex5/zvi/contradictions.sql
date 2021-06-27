select A1.Name as Name, A1.Author as Author, A1.Year as Year from
    bestsellers A1 join bestsellers A2
    on A1.Name = A2.Name
    where A1.Author != A2.Author

UNION

select A1.Name as Name, A1.Author as Author, A1.Year as Year from
    bestsellers A1 join bestsellers A2
    on A1.Name = A2.Name and A1.Year = A2.Year
    where A1.UserRating != A2.UserRating

UNION

select A1.Name as Name, A1.Author as Author, A1.Year as Year from
    bestsellers A1 join bestsellers A2
    on A1.Name = A2.Name and A1.Year = A2.Year
    where A1.Reviews != A2.Reviews

UNION

select A1.Name as Name, A1.Author as Author, A1.Year as Year from
    bestsellers A1 join bestsellers A2
    on A1.Name = A2.Name and A1.Year = A2.Year
    where A1.Price != A2.Price

UNION

select A1.Name as Name, A1.Author as Author, A1.Year as Year from
    bestsellers A1 join bestsellers A2
    on A1.Name = A2.Name
    where A1.Genre != A2.Genre

order by Name,Year










