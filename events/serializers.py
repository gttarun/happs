from .models import UserEvents
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserEvents
        fields = ('id', 'event_name', 'time', 'longitude', 'latitude')