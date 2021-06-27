create table team(
	team varchar(100) primary key,
	NOC char(3)
);

create table athlete(
	id integer primary key,
	name varchar(100),
	age integer check (age > 0),
	sex char(1) check (sex='F' or sex='M'),
	weight real check (weight > 0),
	height real check (height > 0)
);

creat table participation(
	event varchar(100),
	games varchar(100),
	sport varchar(100),
	city varchar(100),
	year integer (check year > 0),
	season varchar(100) check (season = "Summer" or season = "Winter"),
	id integer,
	team varchar(100),
	foreign key (id) references athlete(id),
	foreign key(team) references team(team),
	primary key(event, games, id, team)
);

create table medal(
	medal varchar(100) primary key check (medal = "Gold" or medal = "Bronze" or medal = "Silver" or medal is null)
);

create won(
	medal varchar(100) check (medal = "Gold" or medal = "Bronze" or medal = "Silver" or medal is null),
	id integer,
	team varchar(100),
	event varchar(100),
	games varchar(100),
	foreign key (id) references athlete(id),
	foreign key(team) references team(team),
	foreign key(medal) references medal(medal),
	foreign key(event) references participation(event),
	foreign key(games) references participation(games),
	primary key(event, games, id, team, medal)
);