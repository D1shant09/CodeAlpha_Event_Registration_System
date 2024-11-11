from rest_framework import generics, permissions
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RegisterForEvent(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event = Event.objects.get(id=self.kwargs['event_id'])  # Event ID from URL
        serializer.save(user=self.request.user, event=event)

class UserRegistrations(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)


from django.shortcuts import render, get_object_or_404
from .models import Event
from django.http import HttpResponseRedirect
from django.urls import reverse

# View to display all events
def event_list(request):
    events = Event.objects.all()  # Fetch all events
    return render(request, 'event/event_list.html', {'events': events})

# View to display details of a specific event
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Fetch event by ID or return 404
    return render(request, 'event/event_detail.html', {'event': event})

# View to register for an event
def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Fetch event by ID or return 404
    if request.method == 'POST':
        # Register the user for the event
        user = request.user
        registration = Registration.objects.create(event=event, user=user)
        return HttpResponseRedirect(reverse('event_detail', args=[event.id]))
    return render(request, 'event/register_for_event.html', {'event': event})
