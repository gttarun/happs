# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_auto_20170304_1749'),
        ('events', '0002_auto_20170304_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userevents',
            name='invitees',
        ),
        migrations.AddField(
            model_name='userevents',
            name='invitees',
            field=models.ForeignKey(default=None, to='forms.User'),
        ),
    ]
