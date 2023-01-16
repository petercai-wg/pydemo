from django.urls import include, path
from . import views

urlpatterns = [

    path('grp/', views.graph,  name='grp'),
]
