import pandas as pd
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from main.models import FoodTruck


class Command(BaseCommand):
    help = 'Loads data from food-truck-data.csv into FoodTruck model'

    def handle(self, *args, **options):
        csv_file_path = 'main/food-truck-data.csv'
        try:
            data = pd.read_csv(csv_file_path)
            food_trucks = data[['Applicant', 'FacilityType', 'Address', 'Latitude', 'Longitude', 'FoodItems', 'Status']]
            food_trucks.columns = [
                'applicant', 'facility_type', 'address', 'latitude', 'longitude', 'food_items', 'status'
            ]
            for _, row in food_trucks.iterrows():
                print(row.to_dict())
                FoodTruck.objects.get_or_create(**row.to_dict())
        except Exception as e:
            raise CommandError(f'Error occurred while processing CSV file: {e}') from e

        self.stdout.write(self.style.SUCCESS('Successfully loaded data into FoodTruck model'))
