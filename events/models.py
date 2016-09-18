from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserEvents(models.Model):
	event_name = models.CharField(max_length=255)
	time = models.DateTimeField()
	longitude = models.FloatField()
	latitude = models.FloatField()

	def __str__(self):
		return self.event_name
