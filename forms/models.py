from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=255, blank="True", default="")
	username = models.CharField(max_length=255, blank="True", default="")
	user_id = models.BigIntegerField()
	authentication_token = models.CharField(max_length=255, blank="True", default="")

	def __str__(self):
		return self.username

