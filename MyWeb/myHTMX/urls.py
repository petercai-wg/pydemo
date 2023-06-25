from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.home, name="home-entry"),
    path("search", views.search, name="home-search"),
    path("htmx/entry/<pk>/", views.detail_entry, name="detail-entry"),
    path("htmx/entry/<pk>/update/", views.update_entry, name="update-entry"),
    path("htmx/entry/<pk>/delete/", views.delete_entry, name="delete-entry"),
    path("htmx/create-entry-form/", views.create_entry_form, name="create-entry-form"),
]
