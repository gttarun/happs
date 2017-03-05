# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20170217_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='authentication_token',
            new_name='token',
        ),
    ]
