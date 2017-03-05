# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0010_remove_invitees_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitees',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='invitees',
            name='username',
        ),
        migrations.AddField(
            model_name='invitees',
            name='username',
            field=models.ForeignKey(default=None, to='forms.User'),
        ),
    ]
