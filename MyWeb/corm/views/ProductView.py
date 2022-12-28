from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from corm.models import Product
from corm.forms import ProductModelForm


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "corm/product_list.html", context)


def product_detail_view(request, pk):
    object = get_object_or_404(Product, id=pk)
    context = {
        'object': object
    }
    return render(request, 'corm/product_detail.html', context)


def product_create_view(request):
    initial_data = {
        'title': 'ASUS Laptop',

    }
    form = ProductModelForm(request.POST or None, initial=initial_data)
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            messages.add_message(request, messages.ERROR,
                                 'Form Validation error')

    context = {'form': form}
    return render(request, 'corm/product_create.html', context)
