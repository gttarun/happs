from django.db import models
# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255, primary_key=True)
	user_id = models.BigIntegerField()
	authentication_token = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class invitees(models.Model):
	username = models.ForeignKey('User', on_delete=models.CASCADE, default=None,)
	#event = models.ForeignKey('events.UserEvents', on_delete=models.CASCADE, default=None,)
	response = models.BooleanField(default=True)

	def __str__(self):
		return self.username

	