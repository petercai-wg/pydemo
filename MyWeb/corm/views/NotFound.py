

from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


def error_404(request, exception):
    return render(request, "page_not_found.html", {"ex": exception})
