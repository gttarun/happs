from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .models import UserEvents
from .serializers import EventSerializer

# Create your views here.
def index(request):
	return HttpResponse("List of events!")

# Create your views here.
class EventsmapViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = UserEvents.objects.all()
    serializer_class = EventSerializer