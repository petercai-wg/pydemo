from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse


from collections import namedtuple

from .Util import getPropertiesList, getPropertiesJSONData
from .models import Person, City, Car
from .forms import PersonForm, ContactForm

from .filters import UserFilter, CarListingFilter


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


def basic_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        print(form.data['name'] + " / " + form['password'].value())

        if form.is_valid():
            print(
                "after form validate, form.cleaned_data['password'] " + " /  " + form.instance.message)
        else:
            print(form.errors)
    else:
        form = ContactForm()
        # this won't take effect,
        form.data['name'] = "peter"
    return render(request, 'myApp/basic_contact.html', {'form': form})


def search_user(request):
    user_list = User.objects.all()
    if request.method == 'POST':
        user_filter = UserFilter(request.POST, queryset=user_list)
    if request.method == 'GET':
        user_filter = UserFilter(request.GET, queryset=user_list)

    return render(request, 'myApp/user_list.html', {'filter': user_filter})


def search_car(request):
    car_list = Car.objects.all()
    if request.method == 'POST':
        car_filter = CarListingFilter(request.POST, queryset=car_list)
    if request.method == 'GET':
        car_filter = CarListingFilter(request.GET, queryset=car_list)

    return render(request, 'myApp/car_list.html', {'car_filter': car_filter})
