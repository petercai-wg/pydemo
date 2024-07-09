from django.shortcuts import render
from .forms import FundForm
from .models import FundRation

# Create your views here.


def index(request):
    return render(
        request,
        "mxForm/index.html",
    )


def saverow(request):
    print("POST saverow")
    if request.method == "POST":
        form = FundForm(request.POST or None)
        if form.is_valid():
            print("POST form is valid")
            fr = form.save()
            ctx = {"fr": fr}
            return render(request, "mxForm/fundratial.html", ctx)

        return render(request, "mxForm/partialform.html", {"form": FundForm()})


def addrow(request):
    print("GET newrow")
    if request.method == "GET":
        return render(request, "mxForm/partialform.html", {"form": FundForm()})
