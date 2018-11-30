create table conference (
    confName        varchar(10),
    noTeams         int(2),
    primary key (confName)
);


create table team (
    teamID         int(11),
    teamName       varchar(30),
    city           varchar(20),
--    ownerID        int(10),
    confName       varchar(10),
    primary key (teamID),
--    foreign key (ownerID) references owner(ownerID),
    foreign key (confName) references conference(confName)
);

create table player (
    playerID       int(11),
    first_name     varchar(20),
    last_name      varchar(20),
    DOB            date,
    height         varchar(6),
    weight         int(3),
    position       varchar(14),
    teamID         int(11),
    primary key (playerID),
    foreign key (teamID) references team(teamID)
);

create table owner (
    ownerID         int(10) not null,
    first_name      varchar(20),
    last_name       varchar(20),
    teamID          int(11),
    primary key (ownerID),
    foreign key (teamID) references team(teamID)
);

create table record (
    teamID          int(11),
    wins            int(2),
    losses          int(2),
    ties            int(2), 
    primary key (teamID),
    foreign key (teamID) references team(teamID)
);

create table conferenceRecord (
    teamID          int(11),
    confName      varchar(10),
    wins            int(2),
    losses          int(2),
    ties            int(2), 
    primary key (teamID),
    foreign key (teamID) references team(teamID),
    foreign key (confName) references conference(confName)
);

create table game (
    gameID          int(11),
    team1ID         int(11),
    team2ID         int(11),
    team1Points     int(3),
    team2Points     int(3),
    gameDate       date,
    primary key (gameID),
    foreign key (team1ID) references team(teamID),
    foreign key (team2ID) references team(teamID)
);

create table performance (
    gameID          int(11),
    teamID          int(11),
    playerID        int(11),
    minutes         int(2),
    fgMade          int(2),
    fgAttempted     int(2),
    3ptsMade        int(2),
    3ptsAttempted   int(2),
    rebounds        int(2),
    assists         int(2),
    personalFouls   int(1),
    steals          int(2),
    turnovers       int(2),
    blocks          int(2),
    blocksAgainst   int(2),
    points          int(3),
    primary key (gameID, playerID),
    foreign key (gameID) references game(gameID),
    foreign key (teamID) references team(teamID),
    foreign key (playerID) references player(playerID)
);

create table injuries (
    injuryID        int(11),
    gameID         int(11),
    playerID        int(11),
    diagnosis       varchar(30),
    status          varchar(20),
    primary key (injuryID),
    foreign key (gameID) references game(gameID),
    foreign key (playerID) references player(playerID)
);


             

