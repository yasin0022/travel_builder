from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    # If you need additional fields, you can add them here. For example:
    full_address = models.TextField()

    def __str__(self):
        return self.username


class Destination(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    description = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='itineraries')
    name = models.CharField(max_length=255, null=False)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='itineraries')
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"

class Activity(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    estimated_cost = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
