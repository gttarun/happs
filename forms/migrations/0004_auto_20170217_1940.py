# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20161023_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='authentication_token',
            field=models.CharField(default=b"Enter User's Authentication Token", max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=b"Enter User's Name", max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.BigIntegerField(default=b"Enter User's User ID"),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=b"Enter User's Username", max_length=255),
        ),
    ]
