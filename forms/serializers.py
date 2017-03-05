from rest_framework import serializers
from .models import User, invitees

class InviteeSerializer(serializers.ModelSerializer):
	class Meta:
		model = invitees
		fields = ('username', 'response',)

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'username', 'user_id', 'authentication_token')
