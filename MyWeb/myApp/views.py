from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Person, City
from .forms import PersonForm
from collections import namedtuple
from django.http import JsonResponse
from .Util import getPropertiesList, getPropertiesJSONData


def example_dropdown(request):
    # subject = namedtuple("subject", "id title")
    # subject = namedtuple("subject", ["key", "value"])
    # subjects = [subject(1, 'CANADA'), subject(2, 'US')]

    subjects = getPropertiesList('country')

    context = {'subjects': subjects}

    return render(request, 'myApp/dropdown.html', context)


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('myApp/person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('myApp/person_changelist')


def load_cities(request):
    country_id = request.GET.get('countryId')
    cities = None
    if country_id != '':
        cities = City.objects.filter(country_id=country_id).order_by('name')

    return render(request, 'myApp/city_dropdown_list_options.html', {'cities': cities})


def get_cities_ajax(request):
    subject_id = request.GET.get(
        'subject_id') or request.POST.get('subject_id')
    cities = getPropertiesJSONData(subject_id)
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    return JsonResponse(cities, safe=False)
