# import Http Response from django
from django.http import HttpResponse
from django.shortcuts import render
# get datetime
import datetime
from .models import *

# create a function


def home_view(request):

    context = {"user": "Aaditya"}

    users = User.objects.get(id=1)

    return render(request, "index.html", {'users': users})


def event_view(request):

    return render(request, "event.html")
