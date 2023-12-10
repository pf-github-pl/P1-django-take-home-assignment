from math import asin
from math import cos
from math import radians
from math import sin
from math import sqrt

from django.shortcuts import render

from main.forms import LocationForm
from main.models import FoodTruck


def index(request):
    context = {}
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():

            food_trucks = (FoodTruck.objects.filter(
                active=True,
                status="APPROVED",
                latitude__isnull=False,
                longitude__isnull=False,
            ).exclude(latitude=0, longitude=0)
            )

            latitude = form.cleaned_data["latitude"]
            longitude = form.cleaned_data["longitude"]

            for truck in food_trucks:
                lon1, lat1, lon2, lat2 = map(
                    radians, [float(truck.longitude), float(truck.latitude), float(longitude), float(latitude)]
                )

                # haversine formula
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
                c = 2 * asin(sqrt(a))
                r = 6371  # Radius of earth in kilometers.
                truck.distance = c * r * 1000

            food_trucks_nearby = sorted(food_trucks, key=lambda x: x.distance)[:5]

            for truck in food_trucks_nearby:
                truck.longitude = round(float(truck.longitude), 7)
                truck.latitude = round(float(truck.latitude), 7)

            context["food_trucks_nearby"] = food_trucks_nearby
            context["form"] = form
            return render(request, 'main/index.html', context)
    else:
        form = LocationForm()
        context["form"] = form
    return render(request, 'main/index.html', context)
