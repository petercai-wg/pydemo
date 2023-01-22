from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
import time
import os
import json

from collections import namedtuple

from .Util import getPropertiesList, getPropertiesJSONData
from .models import Person, City, Car
from .forms import PersonForm, ContactForm
from .domainobj import DropDownKeyValue

from .filters import UserFilter, CarListingFilter

import logging

logger = logging.getLogger(__name__)


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
    download_file = 'N'
    if request.method == 'POST':
        time.sleep(1)
        logger.info("sleep 5 seconds ...")
        download_file = 'Y'
        messages.info(request, 'File successfully created.')

        user_filter = UserFilter(request.POST, queryset=user_list)
    if request.method == 'GET':
        user_filter = UserFilter(request.GET, queryset=user_list)

    return render(request, 'myApp/user_list.html', {'filter': user_filter, "download_file": download_file})


def search_car(request):
    car_list = Car.objects.all()
    if request.method == 'POST':
        car_filter = CarListingFilter(request.POST, queryset=car_list)
    if request.method == 'GET':
        car_filter = CarListingFilter(request.GET, queryset=car_list)

    return render(request, 'myApp/car_list.html', {'car_filter': car_filter})


def download_file(request):
    logger.info("downloading file ....")
    file_download = "django_web"

    zipper = os.path.join("c:/TEMP/logs", file_download + ".zip")

    resp = HttpResponse(open(zipper, 'rb').read(),
                        content_type="application/octet-stream")
    resp['Content-Disposition'] = 'attachment; filename=%s.zip' % file_download
    resp['Set-Cookie'] = 'fileDownload=true; Path=/'

    return resp


def group_user(request):
    users = User.objects.all()

    # group_users = []
    h_group_users = []
    q = ""

    # if request.method == 'GET' and 'q' in request.GET:
    #     q = request.GET["q"]
    if request.method == 'POST':
        print(f" POST {request.POST}")
        q = request.POST["q"]
        if q is not None and q != '':
            print(f"user filter {q}")
            users = users.filter(username__icontains=q)

        action = request.POST['form-action']
        h_group_users_str = request.POST['h-group-users']
        h_group_users = json.loads(h_group_users_str.replace("'", "\""))

        print(
            f" hidden group users {h_group_users_str}, --> {h_group_users}  {type(h_group_users)}")

        if action == 'ADD':
            user_selected = request.POST.getlist("user_selected")

            print(f"user selected {user_selected}")

            h_group_users.extend(user_selected)
            h_group_users.sort(key=str.lower)

        if action == 'REMOVE':
            group_selected = request.POST.getlist("group_selected")
            print(f"group selected {group_selected}")
            h_group_users = [
                x for x in h_group_users if x not in group_selected]

    users = users.exclude(username__in=h_group_users)
    user_list = [DropDownKeyValue(u.username, str(u)) for u in users]
    group_users = [DropDownKeyValue(u, u) for u in h_group_users]

    ctx = {"q": q, "search_q": q,  'h_group_users': h_group_users,
           'users': user_list,
           'group_users': group_users

           }

    # return render(request, 'myApp/group_user.html', ctx)
    return render(request, 'myApp/group_user_js.html', ctx)
