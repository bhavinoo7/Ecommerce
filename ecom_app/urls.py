
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('cart', views.cart),
    path('shop', views.shop),
    path('detail', views.detail),
    path('checkout', views.checkout)
]