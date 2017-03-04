from __future__ import unicode_literals

from django.db import models
import events.models
import media.models

class UserModel(models.Model):
	name = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=255)
	birthday = models.DateField(auto_now=False, auto_now_add=False)
	# age
	status = models.TextField(null=True, blank=True)
	# past_events
	future_events = models.ManyToManyField(events.models.UserEvents)
	username = models.CharField(max_length=255)
	user_id = models.BigIntegerField()
	authentication_token = models.CharField(max_length=255)
	profile_picture = models.CharField(max_length=255)
	pictures = models.ManyToManyField(media.models.Picture)
	#friends = models.ManyToManyField(self)
	# settings

	def __str__(self):
		return self.username
