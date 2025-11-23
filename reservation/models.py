from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    numder = models.IntegerField()
    capacity = models.IntegerField()
    locations = models.TextField()
    type = models.CharField(max_length=222, null=True, blank=True)

    def __str__(self):
        return f"Номер приміщення #{self.numder} - {self.capacity}, тип приміщення#{self.type}"
    
    class Meta:
        verbose_name = "Приміщення"
        ordering = ["numder"]

class User(models.Model):
    name = models.CharField(max_length=256)
    sur_name = models.CharField(max_length=256)
    all_rooms = models.ForeignKey(Room, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.name}{self.sur_name}"
    
    class Meta:
        verbose_name = "Користувач/ка"
        verbose_name_plural = "Користувачі"
        ordering = ["name", "sur_name"]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user}# Booking, {self.room}"

    class Meta:
        verbose_name = "Резервування"
        ordering = ["start_time"]


    





# Create your models here.

