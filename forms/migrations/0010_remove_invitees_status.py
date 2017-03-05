# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_auto_20170304_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitees',
            name='status',
        ),
    ]
