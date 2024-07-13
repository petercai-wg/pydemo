from django.shortcuts import render
from .forms import FundForm, MyForm
from .models import FundRation


# Create your views here.
## show everything in a Form to submit
def myFormPartial(request):
    print("GET myFormPartial")
    if request.method == "GET":
        return render(request, "mxForm/mypartialForm.html", {"form": MyForm()})


def myFormSave(request):
    forms = []
    if request.method == "POST":
        print(f"myFormSave POST {request.POST}")

        fundname = request.POST.get("fundname")

        name_list = request.POST.getlist("name")
        print(name_list)
        pct_list = request.POST.getlist("pct")
        print(pct_list)
        cmt_list = request.POST.getlist("comment")
        print(cmt_list)

        for i, (name, pct, comment) in enumerate(zip(name_list, pct_list, cmt_list)):
            f = MyForm(initial={"name": name, "pct": int(pct), "comment": comment})
            forms.append(f)

    print(f"myFormSave forward to mxForm/myForm.html, with {len(forms)}")
    return render(request, "mxForm/myForm.html", {"forms": forms, "fundname": fundname})


def myFormInit(request):
    print("myForm forward to mxForm/myForm.html")
    return render(request, "mxForm/myForm.html")


def index(request):
    print("index forward to mxForm/index.html")
    return render(request, "mxForm/index.html")


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
