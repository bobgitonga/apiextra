# bookings/views.py

from django.db import models
from rest_framework import serializers, viewsets, filters, routers
from django.urls import path, include
from django.contrib import admin

# ---------------------------------------
#  MODELS
# ---------------------------------------

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # duration in minutes
    description = models.TextField()

    def __str__(self):
        return self.title


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, related_name='showtimes', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hall = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.movie.title} at {self.start_time}"


class Booking(models.Model):
    showtime = models.ForeignKey(Showtime, related_name='bookings', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    seats_reserved = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.showtime.movie.title}"


# ---------------------------------------
#  SERIALIZERS
# ---------------------------------------

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ShowtimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Showtime
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    showtime = ShowtimeSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'


# ---------------------------------------
#  VIEWS (CRUD)
# ---------------------------------------

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'genre']


class ShowtimeViewSet(viewsets.ModelViewSet):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie__title', 'hall']


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['customer_name', 'showtime__movie__title']


# ---------------------------------------
#  URL ROUTING
# ---------------------------------------

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'showtimes', ShowtimeViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# ---------------------------------------
#  SETTINGS 
# ---------------------------------------

"""
Add to settings.py:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'bookings',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
"""

# ---------------------------------------
# RUN SERVER
# ---------------------------------------

"""
Commands to run:

1. Apply migrations:
    python manage.py makemigrations
    python manage.py migrate

2. Create superuser (optional):
    python manage.py createsuperuser

3. Run server:
    python manage.py runserver
"""
