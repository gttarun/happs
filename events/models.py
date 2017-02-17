from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserEvents(models.Model):
    event_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    anonymity = models.BooleanField()
    #invitees, attendees, host need to be linked
    invitees = models.TextField()
    attendees = models.TextField()
    host = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.event_name
