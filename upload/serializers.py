from rest_framework import serializers
from .models import FileUpload

class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('created', 'datafile')
        read_only_fields = ('created', 'datafile')