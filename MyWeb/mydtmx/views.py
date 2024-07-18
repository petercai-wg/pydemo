import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

# """ from django.core import serializers """" ## directly using Django Serilizer
from rest_framework import serializers

from .models import Movie
from .forms import MovieForm
import time

# from django_serverside_datatable.views import ServerSideDatatableView


# class MovieistView(ServerSideDatatableView):
#     queryset = Movie.objects.all()
#     columns = ["id", "title", "year", "rating"]


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


def movie_datatable(request):
    data = Movie.objects.all().values()
    json_data = json.dumps(list(data))
    print(json_data)
    context = {"table_data": json_data}
    return render(request, "mydtmx/movie_dt_client.html", context)
    ## using Django serlizer
    # data = serializers.serialize("json", Movie.objects.all())

    # data = MyModelSerializer(Movie.objects.all(), many=True).data
    return JsonResponse(data, safe=False)
    # return HttpResponse(data, content_type="application/json")


def movie_dt_ajax_data(request):

    ##  get draw sequence from client, for serverside = True
    draw = 1
    for key, value in request.GET.items():
        try:
            key_dict = json.loads(key)
            draw_input = key_dict["draw"]
            if draw_input is not None:
                draw = int(draw_input)
                break
        except Exception:
            print(f"There is no draw in the input key, {key} ")
    # for serverside = True
    print(f"movie_dt_ajax_data ... {request.GET}, {draw}")

    data = Movie.objects.all().values()
    ret = {
        "draw": draw,
        "recordsTotal": len(data),
        "recordsFiltered": len(data),
        "data": list(data),
    }
    print(ret)
    return HttpResponse(json.dumps(ret), content_type="application/json")


def index(request):
    print("Movie  index.html ...")
    return render(request, "mydtmx/index.html")


def movie_list(request):
    print("Movie_list ...to movie_list.html")
    # time.sleep(5)
    return render(
        request,
        "mydtmx/movie_list.html",
        {
            "movies": Movie.objects.all(),
        },
    )


def add_movie(request):
    print("add_movie ....")
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "movieListChanged": None,
                            "showMessage": f"{movie.title} added.",
                        }
                    )
                },
            )
    else:
        form = MovieForm()
    return render(
        request,
        "mydtmx/movie_form.html",
        {
            "form": form,
        },
    )


def edit_movie_addcomment(request):
    print("GET edit_movie_addcomment")
    if request.method == "GET":
        return render(request, "mydtmx/partialform.html")


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        print(f"edit_movie {request.POST}")
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "movieListChanged": None,
                            "showMessage": f"{movie.title} updated.",
                        }
                    )
                },
            )
    else:
        form = MovieForm(instance=movie)

    print("edit_movie send to movie_form.html")
    return render(
        request,
        "mydtmx/movie_form.html",
        {
            "form": form,
            "movie": movie,
        },
    )


@require_POST
def remove_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return HttpResponse(
        status=204,
        headers={
            "HX-Trigger": json.dumps(
                {"movieListChanged": None, "showMessage": f"{movie.title} deleted."}
            )
        },
    )


def movie_year(request):
    print("movie_year ...to movie_selection.html")

    return render(
        request,
        "mydtmx/movie_selection.html",
        {
            "movie_years": Movie.objects.all(),
        },
    )


def movie_title(request):
    year = request.GET.get("year")
    print(f"movie_title ...for {year} to movie_selection.html")
    movies = Movie.objects.filter(year=year)
    return render(request, "mydtmx/movie_list.html", {"movies": movies})
