from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    dept_name = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Project(models.Model):
    project_title = models.CharField(
        max_length=755, null=False, blank=False, unique=True)
    project_description = models.TextField(null=False, blank=False)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_title


class Achievement(models.Model):
    achievement_title = models.CharField(
        max_length=755, null=False, blank=False, unique=True)
    achievement_field = models.CharField(
        null=False, blank=False, max_length=400)

    achievement_description = models.TextField(null=False, blank=False)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.achievement_title


class Event(models.Model):
    event_title = models.CharField(
        max_length=755, null=False, blank=False, unique=True)
    event_category = models.CharField(null=False, blank=False, max_length=400)
    event_description = models.TextField(null=False, blank=False)
    event_date = models.DateField(null=False, blank=False)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.event_title
