# import Http Response from django
from django.http import HttpResponse
from django.shortcuts import render
# get datetime
import datetime

# create a function


def home_view(request):

    return render(request, "index.html")


def event_view(request):

    return render(request, "event.html")
