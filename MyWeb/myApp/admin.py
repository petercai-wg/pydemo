from django.contrib import admin

# Register your models here.
from .models import Country, Person, City


Models = (Country, Person, City)

admin.site.register(Models)
