
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import *
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def home_view(request):
    return render(request, "home.html")


def menu_view(request):
    return render(request, "menu/menu.html")


def event_view(request):

    events = Event.objects.all()
    return render(request, "event/event.html", {"events": events})


def displayevent_view(request, pk):

    try:
        event = Event.objects.get(pk=pk)
        return render(request, "event/displayevent.html", {"event": event})

    except Event.DoesNotExist:
        return render(request, "home.html")

    return None


def project_view(request):

    projects = Project.objects.all()
    return render(request, "project/project.html", {"projects": projects})


def displayproj_view(request, pk):

    try:
        project = Project.objects.get(pk=pk)
        return render(request, "project/displayproj.html", {"project": project})

    except Project.DoesNotExist:
        return render(request, "home.html")

    return None


def achievement_view(request):

    achievements = Achievement.objects.all()
    return render(request, "achievement/achievement.html", {"achievements": achievements})


def displayach_view(request, pk):

    try:
        achievement = Achievement.objects.get(pk=pk)
        return render(request, "achievement/displayach.html", {"achievement": achievement})

    except Achievement.DoesNotExist:
        return render(request, "home.html")

    return None


def login_view(request):
    return render(request, "emag_admin/login.html")


def logout_view(request):

    logout(request)
    return redirect(login_view)


def authenticate_view(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(event_form_view)
        else:
            return render(request, "emag_admin/login.html", {"error": "Invalid Credentials"})

    return render(request, "emag_admin/login.html")
