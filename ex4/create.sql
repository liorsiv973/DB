create table movies(
	movieId integer primary key, 
	title varchar(150) not null, 
	rating numeric check (rating>=0 and rating <=10), 
	year integer check (year>0), 
	duration integer check (duration>0), 
	genre varchar(50)
);
