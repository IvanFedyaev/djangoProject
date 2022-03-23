from django.contrib import admin
from .models import Tour, Departure


# Register your models here.

class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'stars', 'nights', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')


class DepartureAdmin(admin.ModelAdmin):
    list_display = ('id', 'departure', 'ru_departure')
    list_display_links = ('id', 'departure', 'ru_departure')
    search_fields = ('id', 'departure', 'ru_departure')


admin.site.register(Tour, TourAdmin)
admin.site.register(Departure, DepartureAdmin)
