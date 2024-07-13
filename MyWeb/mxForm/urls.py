# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="mxForm-show"),
    path("create-row-form", views.addrow, name="create-row-form"),
    path("save-row-form", views.saverow, name="save-row-form"),
    path("myForm", views.myFormInit, name="myForm-show"),
    path("saveForm", views.myFormSave, name="myForm-save"),
    path("create-partial-form", views.myFormPartial, name="create-mypartialform"),
]
