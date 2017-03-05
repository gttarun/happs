from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserEvents(models.Model):
    event_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    host = models.ForeignKey(
         'forms.User',
         related_name = "for_host",
         on_delete=models.CASCADE,
         default = None,)
    description = models.TextField()
    
    def __str__(self):
        return self.event_name

    def __unicode__(self):
        return self.event_name

class Event(models.Model):
    attendee_event = models.ForeignKey('UserEvents', on_delete=models.CASCADE)

    def __str__(self):
        return self.attendee_event