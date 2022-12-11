from django.contrib import admin

# Register your models here.
from .models import Country, Person, City, Car


Models = (Country, Person, City, Car)

admin.site.register(Models)
