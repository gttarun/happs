# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('time', models.DateTimeField(verbose_name='auto_now_add=True')),
                ('active', models.BooleanField()),
            ],
        ),
    ]