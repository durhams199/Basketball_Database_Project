#myapp/urls.py
from django.urls import path

from .views import *
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('team/', TeamPageView.as_view(), name='team'),
    path('game/', GamePageView.as_view(), name='game'),
    path('owner/', OwnerPageView.as_view(), name='owner'),
    path('conferencerecord/', ConferenceRecordPageView.as_view(), name='conferencerecord'),
    path('record/', RecordPageView.as_view(), name='record'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('player/', PlayerPageView.as_view(), name='player'),
]