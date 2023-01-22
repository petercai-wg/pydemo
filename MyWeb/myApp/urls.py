from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

    path('dropdown/', views.example_dropdown, name='example_dropdown'),

    path('get_cities_ajax/', views.get_cities_ajax,     name='get_cities_ajax'),

    path('basic_contact/', views.basic_contact,     name='basic_contact'),

    path('search_user/', views.search_user, name='search_user'),
    path('search_car/', views.search_car, name='search_car'),
    path('download_file/', views.download_file, name='download_file'),

    path('group_user/', views.group_user, name='group_user'),

]
