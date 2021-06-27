create table olympics(
	id varchar,
	name varchar,
	sex varchar,
	age varchar,
	height varchar,
	weight varchar,
	team varchar,
	noc varchar,
	games varchar,
	year varchar,
	season varchar,
	city varchar,
	sport varchar,
	event varchar,
	medal varchar
);

create table athlete(
	id integer primary key,
	name varchar(100) NOT NULL,
	age integer check (age > 0),
	sex char(1) check (sex='F' or sex='M'),
	weight FLOAT check (weight > 0),
	height FLOAT check (height > 0)
);

create table team(
	team varchar(100) primary key,
	NOC char(3) 
);


create table participation(
	event varchar(100),
	games varchar(100),
	sport varchar(100),
	city varchar(100),
	year integer check (year > 0),
	season varchar(100),
	id integer,
	team varchar(100),
	foreign key (id) references athlete(id) ON DELETE CASCADE,
	foreign key(team) references team(team) ON DELETE CASCADE,
	UNIQUE(id, team, games, event)
);

create table medal(
	medal varchar(100) primary key 
);

create table won(
	id integer,
	team varchar(100),
	event varchar(100),
	games varchar(100),
	medal varchar(100),
	foreign key (id) references athlete(id) ON DELETE CASCADE,
	foreign key(team) references team(team) ON DELETE CASCADE,
	foreign key(event) references participation(event) ON DELETE CASCADE,
	foreign key(games) references participation(games) ON DELETE CASCADE,
	foreign key(medal) references medal(medal) ON DELETE CASCADE,
	UNIQUE(id, team, games, event)
);