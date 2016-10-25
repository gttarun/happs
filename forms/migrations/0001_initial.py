# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('user_id', models.BigIntegerField()),
                ('authentication_token', models.CharField(max_length=255)),
            ],
        ),
    ]
