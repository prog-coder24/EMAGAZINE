from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    dept_name = models.CharField(max_length=255, null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name


class Project(models.Model):
    user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, related_name='projects')
    project_title = models.CharField(
        max_length=755, null=False, blank=False, unique=True)
    project_description = models.TextField(null=False, blank=False)
    project_tags = models.CharField(max_length=400, null=True, blank=True)
    project_data = models.FileField(null=True, blank=True)
    project_banner = models.ImageField(null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_title


class Achievement(models.Model):
    user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, related_name='achievements')
    achievement_title = models.CharField(
        max_length=755, null=False, blank=False, unique=True)
    achievement_field = models.CharField(
        null=False, blank=False, max_length=400)
    achievement_data = models.FileField(null=True, blank=True)
    achievement_banner = models.ImageField(null=True, blank=True)
    achievement_tags = models.CharField(max_length=400, null=True, blank=True)
    achievement_description = models.TextField(null=False, blank=False)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.achievement_title


EVENT_CHOICES = (
    ("Fests", "Fests"),
    ("Workshops", "Workshops"),
    ("Activities", "Activities")
)


class Event(models.Model):
    user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, related_name='events')
    event_title = models.CharField(
        max_length=755, null=False, blank=False, unique=True)
    event_category = models.CharField(
        null=False, blank=False, max_length=400, choices=EVENT_CHOICES)
    event_tags = models.CharField(max_length=400, null=True, blank=True)
    organised_by = models.CharField(max_length=1000, null=True, blank=True)
    sponsored_by = models.CharField(max_length=1000, null=True, blank=True)
    event_data = models.FileField(null=True, blank=True)
    event_banner = models.ImageField(null=True, blank=True)
    event_description = models.TextField(null=False, blank=False)
    event_date = models.DateField(null=False, blank=False)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.event_title
