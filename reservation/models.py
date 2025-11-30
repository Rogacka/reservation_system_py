from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    locations = models.TextField()
    type = models.CharField(max_length=222, null=True, blank=True)

    def __str__(self):
        return f"Номер приміщення #{self.number} - {self.capacity}, тип приміщення#{self.type}"
    
    class Meta:
        verbose_name = "Приміщення"
        ordering = ["number"]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    all_rooms = models.ForeignKey(Room, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.user} {self.phone_number}"
    
    class Meta:
        verbose_name = "Користувач/ка"
        verbose_name_plural = "Користувачі"
        ordering = ["user"]

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

