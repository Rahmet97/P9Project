from django.shortcuts import render
from .models import *


def home(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products': products})