from django.contrib import admin
from reservation.models import Booking, Room, Profile


admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(Profile)

# Register your models here.
