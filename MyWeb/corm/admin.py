from django.contrib import admin
from .models import Report, Category, Product, Order

admin.site.register(Report)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
