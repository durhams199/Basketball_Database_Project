create table players
    (playerID       int(10),
     first_name     varchar(20) not null,
     last_name      varchar(20) not null,
     DOB            date(),
     height         varchar(6),
     weight         int(3),
     position       varchar(14),
     teamName       varchar(30),
     primary key (playerID)
     foreign key (teamName) references team(teamName)
       );

