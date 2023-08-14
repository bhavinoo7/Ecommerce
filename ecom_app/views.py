from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, "index.html")

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def detail(request):
    return render(request, "detail.html")

def shop(request):
    product = Product.objects.all().order_by('id')
    p = Paginator(product,3)
    page_number = request.GET.get('page')
    print(page_number,"@@@@@@@@@@@@@@@@@@@@@")
    

    try:
        pagination = p.page(page_number)
    except PageNotAnInteger:
        pagination = p.page(1)
    except EmptyPage:
        pagination = p.page(p.num_pages)
    
    context = {'product':pagination}
    return render(request, "shop.html",context)

def signup(request):
    return render(request, "registration.html")

def signin(request):
    return render(request, "login.html")


