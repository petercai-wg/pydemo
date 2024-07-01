from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path(
        "movie_dt_server",
        TemplateView.as_view(template_name="mydtmx/movie_dt_server.html"),
        name="movie_dt_server",
    ),
    # path("movie_data/", views.MovieistView.as_view()),
    path("movie_data/", views.movie_dt_ajax_data, name="movie_data"),
    path("movie_dt_client", views.movie_datatable, name="movie_dt_client"),
    path("", views.index),
    path("movies", views.movie_list, name="movie_list"),
    path("movies/add", views.add_movie, name="add_movie"),
    path("movies/remove/<int:pk>", views.remove_movie, name="remove_movie"),
    path("movies/edit/<int:pk>", views.edit_movie, name="edit_movie"),
]
