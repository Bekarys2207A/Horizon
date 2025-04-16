from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def about(request):
    return render(request, 'shop/about.html')
