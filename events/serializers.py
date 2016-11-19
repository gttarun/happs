from .models import UserEvents, FileUpload
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserEvents
        fields = ('id', 'event_name', 'time', 'longitude', 'latitude')

class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('event', 'username', 'created', 'datafile')
        read_only_fields = ('created', 'datafile')