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
  ID  INTEGER  PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  sex  CHAR(1) CHECK(sex = 'F' or sex = 'M'),
  age  INTEGER,
  height FLOAT,
  weight FLOAT
);

create table teams(
  team VARCHAR(100) PRIMARY KEY,
  NOC VARCHAR(100) NOT NULL
);

create table game(
  games VARCHAR(100) PRIMARY KEY,
  year INTEGER NOT NULL,
  season VARCHAR(100) NOT NULL,
  city VARCHAR(100) NOT NULL
);

create table sports(
  sport VARCHAR(100) NOT NULL,
  event VARCHAR(100) PRIMARY KEY
);

create table medals(
  medal VARCHAR(100) PRIMARY KEY
);

create table play(
  id integer, 
  team varchar(100),
  games varchar(100),
  event varchar(100),
  FOREIGN KEY (id) REFERENCES athlete(ID) ON DELETE CASCADE,
  FOREIGN KEY (team) REFERENCES teams(team) ON DELETE CASCADE,
  FOREIGN KEY (games) REFERENCES game(games) ON DELETE CASCADE,
  FOREIGN KEY (event) REFERENCES sports(event) ON DELETE CASCADE,
  UNIQUE(id, team, games, event) 
);

create table won(
  id integer,
  team varchar(100),
  games varchar(100),
  event varchar(100),
  medal varchar(100),
  FOREIGN KEY (id) REFERENCES athlete(ID) ON DELETE CASCADE,
  FOREIGN KEY (team) REFERENCES teams(team) ON DELETE CASCADE,
  FOREIGN KEY (games) REFERENCES game(games) ON DELETE CASCADE,
  FOREIGN KEY (event) REFERENCES sports(event) ON DELETE CASCADE,
  FOREIGN KEY (medal) REFERENCES medals(medal) ON DELETE CASCADE,
  UNIQUE(id, team, games, event)
);