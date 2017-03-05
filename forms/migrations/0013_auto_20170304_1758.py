# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0012_auto_20170304_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitees',
            old_name='status',
            new_name='response',
        ),
    ]
