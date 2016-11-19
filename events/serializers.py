from .models import UserEvents, FileUpload
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserEvents
        fields = ('id', 'event_name', 'created_by', 'time', 'longitude', 'latitude')

class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('event', 'created_by', 'created', 'datafile')
        read_only_fields = ('created', 'datafile')