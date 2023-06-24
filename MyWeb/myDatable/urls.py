# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dt-show'),
    path('addnew', views.addnew, name='dt-addnew'),
    path('edit/<int:id>', views.edit,  name='dt-edit'),
    path('update/<int:id>', views.update, name='dt-update'),
    path('delete/<int:id>', views.destroy, name='dt-delete'),
]
