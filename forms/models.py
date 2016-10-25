from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	user_id = models.BigIntegerField()
	authentication_token = models.CharField(max_length=255)

	def __str__(self):
		return self.name

