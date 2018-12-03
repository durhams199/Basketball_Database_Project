from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from myapp.models import *
from myapp.forms import HomeForm
from django.db.models import Q

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    def get(self, request):
        form = HomeForm()
        teams = Team.objects.all()
        args = {'form': form, 'teams': teams}
        return render(request, self.template_name, args)
        
class AboutPageView(TemplateView):
    template_name = 'about.html'

class GamePageView(TemplateView):
    template_name = 'Game.html'
    def get(self, request):
        form = HomeForm()
        games = Game.objects.all()
        args = {'form': form, 'games': games}
        return render(request, self.template_name, args)

class OwnerPageView(TemplateView):
    template_name = 'Owner.html'
    def get(self, request):
        form = HomeForm()
        owners = Owner.objects.all()
        args = {'form': form, 'owners': owners}
        return render(request, self.template_name, args)

class PlayerPageView(TemplateView):
    template_name = 'Player.html'
    def get(self, request):
        form = HomeForm()
        players = Player.objects.all()
        args = {'form': form, 'players': players}
        return render(request, self.template_name, args)
        
class TeamPageView(TemplateView):
    template_name = 'team.html'
    def get(self, request):
        form = HomeForm()
        teams = Team.objects.all()
        args = {'form': form, 'teams': teams}
        return render(request, self.template_name, args)

class ConferenceRecordPageView(TemplateView):
    template_name = 'ConferenceRecord.html'
    def get(self, request):
        form = HomeForm()
        conferencerecords = Conferencerecord.objects.all()
        args = {'form': form, 'conferencerecords': conferencerecords}
        return render(request, self.template_name, args)

class RecordPageView(TemplateView):
    template_name = 'Record.html'
    def get(self, request):
        form = HomeForm()
        records = Record.objects.all()
        args = {'form': form, 'records': records}
        return render(request, self.template_name, args)

