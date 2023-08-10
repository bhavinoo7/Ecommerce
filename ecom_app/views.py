from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def home(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def detail(request):
    return render(request, "detail.html")

def shop(request):
    product = Product.objects.all()
    p = Paginator(Product.objects.all(),3)
    print(p)
    context = {'product':product}
    return render(request, "shop.html",context)

def signup(request):
    return render(request, "registration.html")

def signin(request):
    return render(request, "login.html")


