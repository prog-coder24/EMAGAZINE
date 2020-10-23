# import Http Response from django
from django.http import HttpResponse
from django.shortcuts import render
# get datetime
import datetime
from .models import *

# create a function


def home_view(request):
    return render(request, "home.html")

def menu_view(request):
    return render(request, "menu/menu.html")


def event_view(request):
    return render(request, "event/event.html")

def project_view(request):
    return render(request, "project/project.html")

def achievement_view(request):
    return render(request, "achievement/achievement.html")


