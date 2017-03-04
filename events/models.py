from __future__ import unicode_literals
from django.db import models

class UserModel(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255), primary_key=True
	user_id = models.BigIntegerField()
	authentication_token = models.CharField(max_length=255)

	def __str__(self):
		return self.username

class EventModel(models.Model):
	name = models.CharField(max_length=255)
	time = models.DateTimeField()
	longitude = models.CharField(max_length=255)
	latitude = models.CharField(max_length=255)
	user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

	def __str__(self):
		return self.event_name