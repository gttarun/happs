from __future__ import unicode_literals
from django.db import models
from forms.models import User
from forms.models import invitees

# Create your models here.
class UserEvents(models.Model):
    event_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    anonymity = models.BooleanField()
    #invitees, attendees, host need to be linked
    invitees = models.ForeignKey('forms.User', on_delete=models.CASCADE, default = None,)
    # attendees = models.ManyToManyField(
    #     'forms.User',
    #     related_name = "for_attendees",
    #     default = None,)
    # host = models.ForeignKey(
    #     'forms.User',
    #     related_name = "for_host",
    #     on_delete=models.CASCADE,
    #     default = None,)
    description = models.TextField()

    def __str__(self):
        return self.event_name

# class Invitation(models.Model):
#     users = models.ForeignKey('forms.User', on_delete=models.CASCADE)
#     event = models.ForeignKey(UserEvents, on_delete=models.CASCADE)