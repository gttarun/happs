from __future__ import unicode_literals
from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class UserEvents(models.Model):
	event_name = models.CharField(max_length=255)
	time = models.DateTimeField()
	active = models.BooleanField()
	# city = models.CharField(max_length=255)
	# location = PlainLocationField(based_fields=['city'], zoom=7)

	def __str__(self):
		return self.event_name
