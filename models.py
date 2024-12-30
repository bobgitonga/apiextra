from django.db import models

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
