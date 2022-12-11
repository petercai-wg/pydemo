from collections import OrderedDict

from django.contrib.auth.models import User
import django_filters
from .models import Car
from .choices import CAR_BRAND_CHOICES
from . import Util
# from .forms import CarListingForm
EMPTY_CHOICE = [('', '---------')]


class CarListingFilter(django_filters.FilterSet):

    brand = django_filters.MultipleChoiceFilter(choices=EMPTY_CHOICE + Util.getDBChoice(
        'select distinct brand from myApp_car', 'Car_Brand'),)

    class Meta:

        model = Car

        fields = OrderedDict({
            'trans_type': ['exact'],
            'description': ['icontains'],
            'mileage': ['lt'],

        })


class UserFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='iexact')
    username = django_filters.CharFilter(lookup_expr='icontains')

    # join_year = django_filters.NumberFilter(
    #     field_name='date_joined', lookup_expr='year')
    # join_year__gt = django_filters.NumberFilter(
    #     field_name='date_joined', lookup_expr='year__gt')
    # join_year__lt = django_filters.NumberFilter(
    #     field_name='date_joined', lookup_expr='year__lt')

    class Meta:
        model = User
        # fields = ['username',  'last_name', 'date_joined']
        fields = {

            'date_joined': ['exact', 'year__gt'],
        }
