from django.shortcuts import render
from django.http import HttpResponse
from . models import Products
# /Uniform Resource Locator (Address) --> url


def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})


def home(request):
    return HttpResponse("Amazon")
# Create your views here.

