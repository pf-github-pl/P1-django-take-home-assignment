from django.contrib import admin

from main.models import FoodTruck


@admin.register(FoodTruck)
class FoodTruckAdmin(admin.ModelAdmin):
    list_display = ["applicant", "facility_type", "address", "latitude", "longitude", "food_items", "status", "active"]
    list_filter = ["status", "active"]
    search_fields = ["applicant", "facility_type", "address", "food_items"]
