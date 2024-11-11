from django.db import models
from django.contrib.auth.models import User  # Importing once is sufficient
from .models import Event  # If this file is in the same directory

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    capacity = models.IntegerField()
    available_slots = models.IntegerField()

    def __str__(self):
        return self.name


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Link to the Event model
    registered_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the registration was created

    def __str__(self):
        return f"{self.user.username} registered for {self.event.name}"
