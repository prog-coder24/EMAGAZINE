# Generated by Django 3.1.2 on 2020-10-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMAG_APP', '0008_auto_20201008_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_banner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
