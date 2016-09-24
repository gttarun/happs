from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserEvents
from django.http import HttpResponse
from .serializers import EventSerializer

def index(request):
	return HttpResponse("Hello world!")

@api_view(['GET', 'PUT'])
def event(request, pk):
	try:
		queryset = Snippet.objects.get(pk=pk)
	except queryset.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		queryset = UserEvents.objects.get(pk)
		serializer = EventSerializer
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = EventSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class EventsViewSet(viewsets.ModelViewSet):
	queryset = UserEvents.objects.all()
	serializer_class = EventSerializer
