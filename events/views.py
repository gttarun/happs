from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .models import UserEvents
from .serializers import EventSerializer
from django.urls import reverse
from django import forms
from rest_framework import serializers

# Create your views here.
def index(request):
	return render(request, "events/index.html", context={})

def signup(request):
	return render(request, "events/profile.html", context={})

def create_event(request):
	if request.method == 'POST':
		form = forms.Form(request.POST)
		print form['event_name']
		# print form.cleaned_data['Date']
		# print form.cleaned_data['Time']
	return HttpResponseRedirect(reverse('events:profile')) # Redirect after POST

def event(request, pk):
	queryset = UserEvents.objects.get(pk)
	serializer_class = EventSerializer

# Create your views here.
class EventsViewSet(viewsets.ModelViewSet):
	queryset = UserEvents.objects.all()
	serializer_class = EventSerializer
