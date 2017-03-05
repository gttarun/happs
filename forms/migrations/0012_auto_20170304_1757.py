# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_auto_20170304_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitees',
            name='status',
            field=models.BooleanField(),
        ),
    ]
