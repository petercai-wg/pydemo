from django.db import models
from .choices import CAR_BRAND_CHOICES, CAR_TANSMISSION_TYPE

from . import Util


class Car(models.Model):
    vin = models.IntegerField(unique=True)

    brand = models.CharField(max_length=200, choices=CAR_BRAND_CHOICES)
    # brand = models.CharField(max_length=200, choices=Util.getDBChoice(
    #     'select distinct brand from myApp_car', 'Car_Brand'))

    trans_type = models.CharField(
        max_length=200, choices=CAR_TANSMISSION_TYPE, verbose_name="TransmissionType", )

    mileage = models.IntegerField(default=0)
    color = models.CharField(max_length=200,)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.vin)


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
