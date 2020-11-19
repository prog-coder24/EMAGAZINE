
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


@login_required(login_url='/login/')
def updateEvent_view(request, pk):

    event = Event.objects.get(pk=pk)
    return render(request, "emag_admin/updateEvent.html", {"event": event})


@login_required(login_url='/login/')
def updateEvent(request, pk):

    event = Event.objects.get(pk=pk)

    if request.method == 'POST':

        event.event_title = request.POST.get('title')
        event.event_description = request.POST.get('editor')
        event.event_menu = request.POST.get('menu')
        event.event_tags = request.POST.get('tags')
        event.event_banner = request.FILES.get('banner', event.event_banner)
        event.event_data = request.FILES.get('data', event.event_data)
        event.organised_by = request.POST.get('organised_by', None)
        event.sponsored_by = request.POST.get('sponsored_by', None)
        event.event_date = request.POST.get('event_date', None)
        event.uploaded_at = request.POST.get('uploaded_at')
        event.save()

    return redirect(etab_view)


@login_required(login_url='/login/')
def deleteEvent_view(request, pk):

    Event.objects.get(pk=pk).delete()
    etab = Event.objects.all()
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


@login_required(login_url='/login/')
def project_form(request):

    uname = User.objects.all()
    return render(request, "emag_admin/addProj.html", {"uname": uname})


@login_required(login_url='/login/')
def add_project(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('editor')
        tags = request.POST.get('tags')
        banner = request.FILES.get('banner')
        data = request.FILES.get('data', None)
        dept_name = request.POST.get('dept_name', None)
        uploaded_at = request.POST.get('uploaded_at')

        Project.objects.create(user_id=request.user, project_title=title, project_description=description, project_tags=tags,
                               project_banner=banner, project_data=data, dept_name=dept_name, uploaded_at=uploaded_at)

        return redirect(ptab_view)


@login_required(login_url='/login/')
def deleteProj(request, pk):

    Project.objects.get(pk=pk).delete()
    ptab = Project.objects.all()
    return redirect(ptab_view)


@login_required(login_url='/login/')
def updateProject_view(request, pk):

    project = Project.objects.get(pk=pk)
    return render(request, "emag_admin/updateProject.html", {"project": project})


@login_required(login_url='/login/')
def updateProject(request, pk):

    project = Project.objects.get(pk=pk)

    if request.method == 'POST':

        project.project_title = request.POST.get('title')
        project.project_description = request.POST.get('editor')
        project.project_tags = request.POST.get('tags')
        project.project_banner = request.FILES.get(
            'banner', project.project_banner)
        project.project_data = request.FILES.get('data', project.project_data)
        project.dept_name = request.POST.get('dept_name', None)
        project.uploaded_at = request.POST.get('uploaded_at')
        project.save()

    return redirect(ptab_view)


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


@login_required(login_url='/login/')
def ach_form(request):

    uname = User.objects.all()
    return render(request, "emag_admin/addAch.html", {"uname": uname})


@login_required(login_url='/login/')
def add_Ach(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('editor')
        tags = request.POST.get('tags')
        banner = request.FILES.get('banner')
        data = request.FILES.get('data', None)
        field = request.POST.get('field', None)
        uploaded_at = request.POST.get('uploaded_at')

        Achievement.objects.create(user_id=request.user, achievement_title=title, achievement_description=description,
                                   achievement_tags=tags, achievement_banner=banner, achievement_data=data, achievement_field=field, uploaded_at=uploaded_at)

        return redirect(atab_view)


@login_required(login_url='/login/')
def deleteAch(request, pk):

    Achievement.objects.get(pk=pk).delete()
    return redirect(atab_view)


@login_required(login_url='/login/')
def updateAch_view(request, pk):

    ach = Achievement.objects.get(pk=pk)
    return render(request, "emag_admin/updateAch.html", {"ach": ach})


@login_required(login_url='/login/')
def updateAch(request, pk):

    ach = Achievement.objects.get(pk=pk)

    if request.method == 'POST':

        ach.achievement_title = request.POST.get('title')
        ach.achievement_description = request.POST.get('editor')
        ach.achievement_tags = request.POST.get('tags')
        ach.achievement_banner = request.FILES.get(
            'banner', ach.achievement_banner)
        ach.achievement_data = request.FILES.get('data', ach.achievement_data)
        ach.achievement_field = request.POST.get('field', None)
        ach.uploaded_at = request.POST.get('uploaded_at')
        ach.save()

    return redirect(atab_view)


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


def ptab_view(request):

    ptab = Project.objects.all()
    return render(request, "emag_admin/ptab.html", {"ptab": ptab})


def atab_view(request):

    atab = Achievement.objects.all()
    return render(request, "emag_admin/atab.html", {"atab": atab})


def add_subscriber(request):

    if request.method == 'POST':
        email_address = request.POST.get('email', None)
        if email_address is not None:
            _, __isCreated = Subscriber.objects.get_or_create(
                email_address=email_address)
            if not __isCreated:
                return render(request, "home.html", {"warning": "You are already a subscriber, Thanks :)"})
            else:
                return render(request, "home.html", {"success": "You are now a subscriber, Thanks :)"})
    return redirect(home_view)


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
