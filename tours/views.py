from django.shortcuts import render, get_list_or_404
from tours.models import Tour, Departure
from random import sample


# Create your views here.

def main_view(request):
    main_objects = Tour.objects.all()
    main = sample(list(main_objects), 6)
    return render(request, 'index.html', {'tours': main})


def departure_view(request, departure):
    tours_objects = get_list_or_404(Tour, departure__departure=departure)
    return render(request, 'departure.html', {'tours': tours_objects})


def tour_view(request, pk):
    tour_objects = Tour.objects.get(pk=pk)
    return render(request, 'tour.html', {'tour': tour_objects})
