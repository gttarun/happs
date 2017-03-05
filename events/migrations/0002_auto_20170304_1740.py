# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userevents',
            name='invitees',
            field=models.ManyToManyField(default=None, to='forms.invitees'),
        ),
    ]
