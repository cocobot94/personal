# Generated by Django 5.0.3 on 2024-03-12 02:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
