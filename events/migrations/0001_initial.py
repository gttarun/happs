# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('anonymity', models.BooleanField()),
                ('invitees', models.TextField()),
                ('attendees', models.TextField()),
                ('host', models.CharField(max_length=255)),
                ('host_username', models.CharField(max_length=255)),
                ('host_email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
    ]
