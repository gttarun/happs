from .models import UserModel, EventModel
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventModel
        fields = ('id', 'name', 'time', 'longitude', 'latitude', 'user', 'datafile')
        read_only_fields = ('datafile',)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('name', 'username', 'user_id', 'authentication_token', 'datafile')
		read_only_fields = ('datafile',)
