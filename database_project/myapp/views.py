from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from myapp.models import *
from myapp.forms import HomeForm

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
