from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from .models import UserEvents
from django.http import HttpResponse
from .serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend

def index(request):
    return HttpResponse("Hello world!")

def event(request, pk):
    queryset = UserEvents.objects.get(pk)
    serializer = EventSerializer
    return Response(serializer.data)

def search(request):
    queryset_list = User.objects.all() 
    query = self.request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(event_name__icontains=query),
                Q(date__icontains=query),
                Q(start_time__icontains=query),
                Q(end_time__icontains=query),
                Q(anonymity__icontains=query),
                Q(invitees__icontains=query),
                Q(description__icontains=query),
                )
    return queryset_list

# Create your views here.
class EventsViewSet(viewsets.ModelViewSet):
    queryset = UserEvents.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('event_name', 
            'address', 
            'date', 
            'start_time', 
            'end_time', 
            'anonymity', 
            'invitees', 
            #'attendees', 
            #'host', 
            'description',)

    @detail_route(methods=['post'])
    def addEvent(self, request):
        serializer = EventSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEventsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return UserEvents.objects.get(pk=pk)
        except UserEvents.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_event = self.get_object(pk)
        serializer = EventSerializer(user_event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user_event = self.get_object(pk)
        serializer = EventSerializer(user_event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_event = self.get_object(pk)
        user_event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

