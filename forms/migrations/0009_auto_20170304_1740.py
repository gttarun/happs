# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20170304_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='invitees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='invitees',
            name='username',
            field=models.ManyToManyField(default=None, to='forms.User'),
        ),
    ]
