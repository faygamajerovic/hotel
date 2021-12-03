from django.db import models
from django.db.models.base import Model
from django.db.models.fields import URLField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.


class Hotel(models.Model):
    # location, images, description
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="hotels")

    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)

    date = models.DateTimeField()

    price = models.FloatField()

    def __str__(self):
        return f"{self.user} booking at {self.hotel}"
