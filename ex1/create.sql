create table team(
	team varchar(100) primary key,
	NOC char(3)
);

create table athlete(
	id integer primary key,
	name varchar(100),
	sex char(1) check (sex='F' or sex='M'),
	age integer check (age > 0),
	height real check (height > 0),
	weight real check (weight > 0)
);

create table participation(
	games varchar(100),
	year integer check (year > 0),
	season varchar(100),
	city varchar(100),
	sport varchar(100),
	event varchar(100),
	id integer,
	team varchar(100),
	foreign key (id) references athlete(id),
	foreign key(team) references team(team),
	primary key(event, games, id, team)
);

create table medal(
	medal varchar(100) primary key 
);

create table won(
	id integer,
	team varchar(100),
	games varchar(100),
	event varchar(100),
	medal varchar(100),
	foreign key(medal) references medal(medal),
	foreign key(event, games, id, team) references participation(event, games, id, team),
	primary key(event, games, id, team, medal)
);