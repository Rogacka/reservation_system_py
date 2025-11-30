from django.urls import path
from reservation import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms_list", views.room_list, name="room_list"),
    path("book_room", views.book_room, name="book_room"),
    path("booking_details/<int:pk>/", views.booking_details, name="booking_details"),
]


