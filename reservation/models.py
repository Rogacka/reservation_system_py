from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    numder = models.IntegerField()
    capacity = models.IntegerField()
    locations = models.TextField()

    def __str__(self):
        return f"Room #{self.numder} - {self.capacity}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["numder"]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user}# Booking, {self.room}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["start_time"]




# Create your models here.

