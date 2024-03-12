# Generated by Django 5.0.3 on 2024-03-12 18:23

import apps.core.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='title')),
                ('title_es', models.CharField(max_length=100, null=True, verbose_name='title')),
                ('content', models.TextField(max_length=1000, verbose_name='content')),
                ('content_en', models.TextField(max_length=1000, null=True, verbose_name='content')),
                ('content_es', models.TextField(max_length=1000, null=True, verbose_name='content')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.core.models.custom_upload_to, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
