# Generated by Django 3.1.2 on 2020-10-08 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EMAG_APP', '0009_project_project_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='achievement',
            name='achievement_banner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='achievement',
            name='achievement_data',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='event_banner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='event_data',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_banner',
            field=models.ImageField(upload_to=''),
        ),
    ]
