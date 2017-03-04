from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('name', 'first_name', 'last_name', 'username', 
			'user_id', 'authentication_token', 'city', 'state', 
			'birthday', 'status', 'future_events', 
			'profile_picture')
