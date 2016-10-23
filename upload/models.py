from __future__ import unicode_literals
from django.db import models

def upload_to(instance, filename):
	return 'static/images/{}'.format(filename)

class FileUpload(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	datafile = models.ImageField(('image'), blank=True, null=True, upload_to=upload_to)
