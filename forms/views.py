from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, detail_route, list_route

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	@detail_route(methods=['post'])
	def addUser(self, request):
		serializer = UserSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
