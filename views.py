from rest_framework import viewsets, filters
from .models import Movie, Showtime, Booking
from .serializers import MovieSerializer, ShowtimeSerializer, BookingSerializer


# Movie CRUD
class MovieViewSet(viewsets.ModelViewSet):
