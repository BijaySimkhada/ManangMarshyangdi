from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Booking(models.Model):
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    contact = models.CharField(max_length=25)
    booked_at = models.DateTimeField(auto_now_add=True)
    booked_date = models.DateField(null=False)
    book_time = models.TimeField(null=False)

    def __str__(self):
        return self.contact


class BookingHistory(models.Model):
    class Meta:
        verbose_name_plural = 'Booking histories'
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    booked_time = models.TimeField(null=True)
    booked_date = models.DateField(null=False)
    booked_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.booked_time, self.booked_date


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    contact = models.CharField(max_length=25)

    def __str__(self):
        return self.contact


class Gallery(models.Model):
    class Meta:
       verbose_name_plural = 'galleries'
    img = models.ImageField(upload_to="photos/gallery", blank=True, null=True)
    uploaded_at = models.DateField(auto_now_add=True)
    caption = models.TextField(max_length=255, null=True, default="Manang Marshyangdi")


class Tournament(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=146)
    img = models.ImageField(upload_to="photos/tournament", blank=True)
    date = models.DateField(null=False)
    time = models.CharField(max_length=10, null=False)
    location = models.CharField(max_length=255, null=False)

    def __str__(self):
        self.name