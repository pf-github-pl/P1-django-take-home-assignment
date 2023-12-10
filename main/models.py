from django.db import models


class Timestamped(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FoodTruck(Timestamped):
    class Meta:
        verbose_name_plural = "Food Trucks"

    applicant = models.CharField(max_length=100)
    facility_type = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    food_items = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.applicant} {self.status} {self.active}"
