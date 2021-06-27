create table movies(
	movieId integer primary key, 
	title varchar(150) not null, 
	rating numeric check (rating>=0 and rating <=10), 
	year integer check (year>0), 
	duration integer check (duration>0), 
	genre varchar(50)
);

create table actors(
	actorId integer primary key, 
	name varchar(100) not null, 
	byear integer check (byear>0) , 
	dyear integer check (dyear>byear)
);

create table playsIn(
	movieId integer, 
	actorId integer, 
	character varchar(100),
	foreign key(movieId) references movies(movieId),
	foreign key(actorId) references actors(actorId),
	primary key(actorId,movieId) 	
);