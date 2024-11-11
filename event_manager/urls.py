from django.contrib import admin
from django.urls import path, include
from .views import home  # Import the home view from views.py

urlpatterns = [
    path('', home, name='home'),  # Route for the root URL
    path('admin/', admin.site.urls),
    path('api/', include('events.urls')),
]
