from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.URLField(max_length=300)
    price = models.PositiveIntegerField()
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    country = models.CharField(max_length=15)
    nights = models.PositiveSmallIntegerField()
    date = models.CharField(max_length=30)
    departure = models.ForeignKey('Departure', on_delete=models.CASCADE)

class Departure(models.Model):
    departure = models.CharField(max_length=50)
    ru_departure = models.CharField(max_length=100)


