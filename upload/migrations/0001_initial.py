# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import upload.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default='', max_length=255, blank='True')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datafile', models.ImageField(upload_to=upload.models.upload_to, null=True, verbose_name='image', blank=True)),
            ],
        ),
    ]
