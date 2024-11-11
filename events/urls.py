# events/urls.py
from django.urls import path
from .views import EventList, EventDetail, RegisterForEvent, UserRegistrations

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),               # List all events or create a new event
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),   # Retrieve, update, or delete a specific event
    path('events/<int:event_id>/register/', RegisterForEvent.as_view(), name='event-register'),  # Register for an event
    path('my-registrations/', UserRegistrations.as_view(), name='user-registrations'),  # View user's registrations
]

# In events/urls.py for API views
from django.urls import path
from .views import EventList, EventDetail, RegisterForEvent, UserRegistrations

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('events/<int:event_id>/register/', RegisterForEvent.as_view(), name='event-register'),
    path('my-registrations/', UserRegistrations.as_view(), name='user-registrations'),
]
from django.urls import path
from . import views

urlpatterns = [
    # Corrected path for class-based view
    path('event/<int:event_id>/', views.EventDetail.as_view(), name='event_detail'),
]
