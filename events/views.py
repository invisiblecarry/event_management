from rest_framework import viewsets, filters
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer
from rest_framework.permissions import IsAuthenticated

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
