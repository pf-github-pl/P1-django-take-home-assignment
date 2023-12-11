from math import asin
from math import cos
from math import radians
from math import sin
from math import sqrt

from django.shortcuts import render

from main.forms import LocationForm
from main.models import FoodTruck


def index(request):
    """
    This view handles the main page of the application. It processes the form with the user's location data
    and finds the nearest food trucks.
    """
    context = {}  # Initialize the context dictionary

    # Check if the request method is POST
    if request.method == "POST":
        form = LocationForm(request.POST)  # Create a form instance with the submitted data
        # Check if the form is valid
        if form.is_valid():

            # Query the database for active, approved food trucks with non-null and non-zero coordinates
            food_trucks = (FoodTruck.objects.filter(
                active=True,
                status="APPROVED",
                latitude__isnull=False,
                longitude__isnull=False,
            ).exclude(latitude=0, longitude=0)
            )

            # Extract the user's latitude and longitude from the form
            latitude = form.cleaned_data["latitude"]
            longitude = form.cleaned_data["longitude"]

            # Iterate over the food trucks
            for truck in food_trucks:
                # Convert longitude and latitude to radians for both the truck and user's location
                lon1, lat1, lon2, lat2 = map(
                    radians, [float(truck.longitude), float(truck.latitude), float(longitude), float(latitude)]
                )

                # haversine formula to calculate the distance between two points on the Earth's surface
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
                c = 2 * asin(sqrt(a))
                r = 6371  # Radius of earth in kilometers.
                truck.distance = c * r * 1000  # Calculate the distance in meters

            # Sort the food trucks by distance and take the first 5
            food_trucks_nearby = sorted(food_trucks, key=lambda x: x.distance)[:5]

            for truck in food_trucks_nearby:
                # Round the longitude and latitude to 7 decimal places
                truck.longitude = round(float(truck.longitude), 7)
                truck.latitude = round(float(truck.latitude), 7)

            # Add the nearby food trucks and the form to the context
            context["food_trucks_nearby"] = food_trucks_nearby
            context["form"] = form
            return render(request, 'main/index.html', context)
    else:
        # If the request method is not POST, create a new form
        form = LocationForm()
        # Add the form to the context
        context["form"] = form
    return render(request, 'main/index.html', context)
