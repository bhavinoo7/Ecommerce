from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def detail(request):
    return render(request, "detail.html")

def shop(request):
    return render(request, "shop.html")

def signup(request):
    return render(request, "registration.html")

def signin(request):
    return render(request, "login.html")


