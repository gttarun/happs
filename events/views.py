from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from .models import UserEvents
from django.http import HttpResponse
from .serializers import EventSerializer

def index(request):
	return HttpResponse("Hello world!")

def event(request, pk):
	queryset = UserEvents.objects.get(pk)
	serializer = EventSerializer
	return Response(serializer.data)

# Create your views here.
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

