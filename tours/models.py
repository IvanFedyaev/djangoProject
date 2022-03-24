from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Departure(models.Model):
    departure = models.CharField(max_length=50, verbose_name='Отпрвление')
    ru_departure = models.CharField(max_length=100, verbose_name='Отправление(на русском)')

    def get_absolute_url(self):
        return reverse('tours', kwargs={'departure': self.departure})

    class Meta:
        verbose_name = 'Отправления'
        verbose_name_plural = 'Отправления'
        ordering = ['id']


class Tour(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    picture = models.URLField(max_length=300, verbose_name='Фото')
    price = models.PositiveIntegerField(verbose_name='Цена')
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                             verbose_name='Звезды')
    country = models.CharField(max_length=15, verbose_name='Страна')
    nights = models.PositiveSmallIntegerField(verbose_name='Дни')
    date = models.CharField(max_length=30, verbose_name='Дата')
    departure = models.ForeignKey(Departure, on_delete=models.CASCADE, related_name='tour', verbose_name='Отправление')

    def __str__(self):
        return f"{self.title} - {self.departure.departure}"

    def get_absolute_url(self):
        return reverse('tour', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Туры'
        verbose_name_plural = 'Туры'
        ordering = ['title']
