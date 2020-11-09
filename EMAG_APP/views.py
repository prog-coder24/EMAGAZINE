
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


@login_required(login_url='/login/')
def event_form_view(request):

    uname = User.objects.all()
    return render(request, "emag_admin/addEvent.html", {"uname": uname})


@login_required(login_url='/login/')
def add_event_view(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('editor')
        menu = request.POST.get('menu')
        tags = request.POST.get('tags')
        banner = request.FILES.get('banner')
        data = request.FILES.get('data', None)
        organised_by = request.POST.get('organised_by', None)
        sponsored_by = request.POST.get('sponsored_by', None)
        event_date = request.POST.get('event_date', None)
        uploaded_at = request.POST.get('uploaded_at')

        Event.objects.create(user_id=request.user, event_title=title, event_description=description, event_category=menu, event_tags=tags,
                             event_banner=banner, event_data=data, organised_by=organised_by, sponsored_by=sponsored_by, event_date=event_date, uploaded_at=uploaded_at)

        return redirect(etab_view)


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


def option_view(request):
    return render(request, "emag_admin/option.html")


def etab_view(request):

    etab = Event.objects.all()
    return render(request, "emag_admin/etab.html", {"etab": etab})


def authenticate_view(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(option_view)
        else:
            return render(request, "emag_admin/login.html", {"error": "Invalid Credentials"})

    return render(request, "emag_admin/login.html")
