from rest_framework import viewsets, status, permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from .models import UserModel, EventModel
from django.http import HttpResponse
from .serializers import EventSerializer, UserSerializer
from django.shortcuts import render

def index(request):
	return HttpResponse("Hello world!")

def event(request, pk):
	queryset = UserEvents.objects.get(pk)
	serializer = EventSerializer
	return Response(serializer.data)

def get_user(request, image_id):
	db_image = UserModel.objects.get(pk=image_id)
	image = "../" + str(db_image.datafile)
	return render(request, 'upload/show_image.html', {'image': image})

def get_event(request, image_id):
	db_image = EventModel.objects.get(pk=image_id)
	image = "../" + str(db_image.datafile)
	return render(request, 'upload/show_image.html', {'image': image})

# Create your views here.
class EventsViewSet(viewsets.ModelViewSet):
	queryset = EventModel.objects.all()
	serializer_class = EventSerializer
	parser_classes = (MultiPartParser, FormParser,)
	@detail_route(methods=['post'])
	def addEvent(self, request):
		serializer = EventSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
	queryset = UserModel.objects.all()
	serializer_class = UserSerializer
	parser_classes = (MultiPartParser, FormParser,)
	@detail_route(methods=['post'])
	def addUser(self, request):
		serializer = UserSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
