# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Conference(models.Model):
    confname = models.CharField(db_column='confName', primary_key=True, max_length=10)  # Field name made lowercase.
    noteams = models.IntegerField(db_column='noTeams', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conference'


class Conferencerecord(models.Model):
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamID', primary_key=True)  # Field name made lowercase.
    confname = models.ForeignKey(Conference, models.DO_NOTHING, db_column='confName', blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conferencerecord'

class Game(models.Model):
    gameid = models.IntegerField(db_column='gameID', primary_key=True)  # Field name made lowercase.
    team1id = models.ForeignKey('Team', models.DO_NOTHING, db_column='team1ID', blank=True, null=True)  # Field name made lowercase.
    team2id = models.CharField(db_column='teamName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    team1points = models.IntegerField(db_column='team1Points', blank=True, null=True)  # Field name made lowercase.
    team2points = models.IntegerField(db_column='team2Points', blank=True, null=True)  # Field name made lowercase.
    gamedate = models.DateField(db_column='gameDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game'


class Injuries(models.Model):
    injuryid = models.IntegerField(db_column='injuryID', primary_key=True)  # Field name made lowercase.
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='gameID', blank=True, null=True)  # Field name made lowercase.
    playerid = models.ForeignKey('Player', models.DO_NOTHING, db_column='playerID', blank=True, null=True)  # Field name made lowercase.
    diagnosis = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injuries'


class Owner(models.Model):
    ownerid = models.IntegerField(db_column='ownerID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'owner'


class Performance(models.Model):
    gameid = models.ForeignKey(Game, models.DO_NOTHING, db_column='gameID', primary_key=True)  # Field name made lowercase.
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    playerid = models.ForeignKey('Player', models.DO_NOTHING, db_column='playerID')  # Field name made lowercase.
    minutes = models.IntegerField(blank=True, null=True)
    fgmade = models.IntegerField(db_column='fgMade', blank=True, null=True)  # Field name made lowercase.
    fgattempted = models.IntegerField(db_column='fgAttempted', blank=True, null=True)  # Field name made lowercase.
    number_3ptsmade = models.IntegerField(db_column='3ptsMade', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ptsattempted = models.IntegerField(db_column='3ptsAttempted', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    rebounds = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    personalfouls = models.IntegerField(db_column='personalFouls', blank=True, null=True)  # Field name made lowercase.
    steals = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    blocksagainst = models.IntegerField(db_column='blocksAgainst', blank=True, null=True)  # Field name made lowercase.
    points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance'
        unique_together = (('gameid', 'playerid'),)


class Player(models.Model):
    playerid = models.IntegerField(db_column='playerID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(max_length=6, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=14, blank=True, null=True)
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamID', blank=True, null=True)  # Field name made lowercase.
    points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class Record(models.Model):
    teamid = models.ForeignKey('Team', models.DO_NOTHING, db_column='teamID', primary_key=True)  # Field name made lowercase.
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'


class Team(models.Model):
    teamid = models.IntegerField(db_column='teamID', primary_key=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='teamName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=20, blank=True, null=True)
    confname = models.ForeignKey(Conference, models.DO_NOTHING, db_column='confName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'team'
