# Generated by Django 2.1.3 on 2018-12-02 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('confname', models.CharField(db_column='confName', max_length=10, primary_key=True, serialize=False)),
                ('noteams', models.IntegerField(blank=True, db_column='noTeams', null=True)),
            ],
            options={
                'db_table': 'conference',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('gameid', models.IntegerField(db_column='gameID', primary_key=True, serialize=False)),
                ('team2id', models.CharField(blank=True, db_column='teamName', max_length=30, null=True)),
                ('team1points', models.IntegerField(blank=True, db_column='team1Points', null=True)),
                ('team2points', models.IntegerField(blank=True, db_column='team2Points', null=True)),
                ('gamedate', models.DateField(blank=True, db_column='gameDate', null=True)),
            ],
            options={
                'db_table': 'game',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Injuries',
            fields=[
                ('injuryid', models.IntegerField(db_column='injuryID', primary_key=True, serialize=False)),
                ('diagnosis', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'injuries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('ownerid', models.IntegerField(db_column='ownerID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'owner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('playerid', models.IntegerField(db_column='playerID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('height', models.CharField(blank=True, max_length=6, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('position', models.CharField(blank=True, max_length=14, null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'player',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamid', models.IntegerField(db_column='teamID', primary_key=True, serialize=False)),
                ('teamname', models.CharField(blank=True, db_column='teamName', max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'team',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conferencerecord',
            fields=[
                ('teamid', models.ForeignKey(db_column='teamID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.Team')),
                ('wins', models.IntegerField(blank=True, null=True)),
                ('losses', models.IntegerField(blank=True, null=True)),
                ('ties', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'conferencerecord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('gameid', models.ForeignKey(db_column='gameID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.Game')),
                ('minutes', models.IntegerField(blank=True, null=True)),
                ('fgmade', models.IntegerField(blank=True, db_column='fgMade', null=True)),
                ('fgattempted', models.IntegerField(blank=True, db_column='fgAttempted', null=True)),
                ('number_3ptsmade', models.IntegerField(blank=True, db_column='3ptsMade', null=True)),
                ('number_3ptsattempted', models.IntegerField(blank=True, db_column='3ptsAttempted', null=True)),
                ('rebounds', models.IntegerField(blank=True, null=True)),
                ('assists', models.IntegerField(blank=True, null=True)),
                ('personalfouls', models.IntegerField(blank=True, db_column='personalFouls', null=True)),
                ('steals', models.IntegerField(blank=True, null=True)),
                ('turnovers', models.IntegerField(blank=True, null=True)),
                ('blocks', models.IntegerField(blank=True, null=True)),
                ('blocksagainst', models.IntegerField(blank=True, db_column='blocksAgainst', null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'performance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('teamid', models.ForeignKey(db_column='teamID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapp.Team')),
                ('wins', models.IntegerField(blank=True, null=True)),
                ('losses', models.IntegerField(blank=True, null=True)),
                ('ties', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'record',
                'managed': False,
            },
        ),
    ]