# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20170304_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='token',
            new_name='authentication_token',
        ),
    ]
