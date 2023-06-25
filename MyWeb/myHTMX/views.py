from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserEntryForm
from .models import UserEntry


def search(request):
    print(f"search for {request.POST}")
    entries = UserEntry.objects.all()
    form = UserEntryForm(None)
    context = {"form": form, "entries": entries}

    return render(request, "myHTMX/home.html", context)

    # return redirect("home-entry")


def home(request):
    # entries = UserEntry.objects.all()
    form = UserEntryForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            entry = form.save(commit=False)
            entry.region = "EMEA"
            entry.save()
            print("myHTMX home entry saved, redirect to detail_entry...")
            return redirect("detail-entry", pk=entry.id)
        else:
            # if error
            return render(request, "myHTMX/entry_form.html", context={"form": form})

    # context = {"form": form, "entries": entries}
    context = {"form": form}

    return render(request, "myHTMX/home.html", context)


def update_entry(request, pk):
    print(f"update_entry ..for {pk}")
    entry = UserEntry.objects.get(id=pk)
    form = UserEntryForm(request.POST or None, instance=entry)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("detail-entry", pk=entry.id)

    context = {"form": form, "entry": entry}

    return render(request, "myHTMX/entry_form.html", context)


def delete_entry(request, pk):
    entry = get_object_or_404(UserEntry, id=pk)

    if request.method == "POST":
        entry.delete()
        return HttpResponse("")

    return HttpResponseNotAllowed(
        [
            "POST",
        ]
    )


def detail_entry(request, pk):
    print(f"detail_entry ..for {pk}")
    entry = get_object_or_404(UserEntry, id=pk)
    context = {"entry": entry}
    return render(request, "myHTMX/entry_detail.html", context)


def create_entry_form(request):
    print("create_entry_form .....")
    form = UserEntryForm()
    context = {"form": form}
    return render(request, "myHTMX/entry_form.html", context)
