from django.db.models import Min, Max, Count
from django.shortcuts import render, get_list_or_404
from tours.models import Tour, Departure
from random import sample


# Create your views here.

def main_view(request):
    main_objects = Tour.objects.all()
    main = sample(list(main_objects), 6)
    return render(request, 'index.html', {'tours': main})


def departure_view(request, departure):
    tours_objects = Tour.objects.filter(departure__departure=departure)
    tours = tours_objects.aggregate(min_price=Min('price'), max_price=Max('price'), min_nights=Min('nights'),
                                    max_nights=Max('nights'))
    return render(request, 'departure.html', {'tours': tours_objects, 't': tours})


def tour_view(request, pk):
    tour_objects = Tour.objects.get(pk=pk)
    return render(request, 'tour.html', {'tour': tour_objects})
