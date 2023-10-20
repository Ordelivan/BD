create table theatre_type(
    id integer PRIMARY KEY autoincrement,
    name varchar(16) 
);

create table theatre(
    id integer PRIMARY KEY autoincrement,
    locationid integer,
    name varchar(16),
    typeid integer,
    foreign key(locationid) referenced location(id),
    foreign key(typeid) referenced type(id)
);

create table location(
    id integer primary key autoincrement,
    adress varchar(16),
    countryid integer,
    foreign key(countryid) referenced country(id)
);

create table country(
    id integer primary key autoincrement,
    name varchar(16)
    );

create table performance(
    id integer primary key autoincrement,
    name varchar(16),
    performance_date date,
    personalid integer,
    theatreid integer, 
    genreid integer,
    foreign key(personalid) referenced personal(id),
    foreign key(theatreid) referenced theatre(id),
    foreign key(genreid) referenced genre(id)
);

create table genre(
    id integer PRIMARY KEY autoincrement,
    name varchar(16)
);

create table personal(
    id integer PRIMARY KEY autoincrement,
    login varchar(16),
    password varchar(16),
    jobid integer,
    foreign key(jobid) referenced jobs(id)
);

create table jobs(
    id integer PRIMARY KEY autoincrement,
    name varchar(16),
);

create table User(
    id integer PRIMARY KEY autoincrement,
    login varchar(16),
    password varchar(16)
);

create table tickets(
    id integer PRIMARY KEY autoincrement,
    userid integer,
    performanceid integer,
    foreign key(userid) referenced User(id)
);