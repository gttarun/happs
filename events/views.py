from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import viewsets, status, permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import FileUploadSerializer
from rest_framework.response import Response
from django.utils.encoding import smart_str
from .models import FileUpload, UserEvents
from .serializers import EventSerializer
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image

def get_image(request, image_id):
	db_image = FileUpload.objects.get(pk=image_id)
	image = "../" + str(db_image.datafile)
	return render(request, 'events/show_image.html', {'image': image})

class FileUploadViewSet(ModelViewSet):
	
	queryset = FileUpload.objects.all()
	serializer_class = FileUploadSerializer
	parser_classes = (MultiPartParser, FormParser,)

	def perform_create(self, serializer):
		serializer.save(datafile=self.request.data.get('datafile'))

	def retrieve(self, request, pk, format=""):
		images = []
		db_image = FileUpload.objects.filter(username=pk)
		for each in db_image:
			images.append(str(each.datafile))
		return render(request, 'events/show_image.html', {'images': images, 'username': pk})

class EventsViewSet(viewsets.ModelViewSet):
	queryset = UserEvents.objects.all()
	serializer_class = EventSerializer

	@detail_route(methods=['post'])
	def addEvent(self, request):
		serializer = EventSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

