import pandas as pd
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from main.models import FoodTruck


class Command(BaseCommand):
    """
    Django management command to load data from a CSV file into the FoodTruck model.
    """
    help = 'Loads data from food-truck-data.csv into FoodTruck model'

    def handle(self, *args, **options):
        """
        The actual logic of the command. Reads the CSV file and creates FoodTruck objects.
        """
        csv_file_path = 'main/food-truck-data.csv'
        try:
            # Read the CSV file using pandas
            data = pd.read_csv(csv_file_path)

            # Select the necessary columns and rename them to match the model's fields
            food_trucks = data[['Applicant', 'FacilityType', 'Address', 'Latitude', 'Longitude', 'FoodItems', 'Status']]
            food_trucks.columns = [
                'applicant', 'facility_type', 'address', 'latitude', 'longitude', 'food_items', 'status'
            ]
            i = 0  # Counter for the number of created FoodTruck objects
            for _, row in food_trucks.iterrows():
                # Create a FoodTruck object for each row in the DataFrame
                FoodTruck.objects.create(**row.to_dict())
                print(f'Created FoodTruck with data {row.to_dict()}')
                i += 1  # Increment the counter
        except Exception as e:
            # If an error occurs, raise a CommandError with a description of the error
            raise CommandError(f'Error occurred while processing CSV file: {e}') from e

        # If everything went well, print a success message with the number of created FoodTruck objects
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {i} trucks into FoodTruck model.'))
