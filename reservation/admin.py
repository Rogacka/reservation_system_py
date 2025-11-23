from django.contrib import admin
from reservation.models import Booking, Room, User


admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(User)

# Register your models here.
