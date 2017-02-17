from .models import UserEvents
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:

    	users = serializers.HyperlinkedRelatedField(
        view_name='UserViewSet',
        lookup_field='username',
        many=True,
        read_only=True
    )

        model = UserEvents
        fields = ('event_name', 
			'address', 
			'date', 
			'start_time', 
			'end_time', 
			'anonymity', 
			'invitees', 
			'attendees', 
			'host', 
			'description',)