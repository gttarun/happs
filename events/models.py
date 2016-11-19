from __future__ import unicode_literals
from django.db import models

def upload_to(instance, filename):
	return 'static/images/{}'.format(filename)

class UserEvents(models.Model):
	event_name = models.CharField(max_length=255)
	time = models.DateTimeField()
	longitude = models.CharField(max_length=255)
	latitude = models.CharField(max_length=255)

	def __str__(self):
		return str(self.id) + " | " + self.event_name

class FileUpload(models.Model):
	event = models.ForeignKey(UserEvents, on_delete=models.CASCADE)
	username = models.CharField(max_length=255, blank="True", default="")
	created = models.DateTimeField(auto_now_add=True)
	datafile = models.ImageField(('image'), blank=True, null=True, upload_to=upload_to)
