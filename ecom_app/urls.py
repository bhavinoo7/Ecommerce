
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('cart', views.cart),
    path('shop', views.shop),
    path('detail', views.detail),
    path('checkout', views.checkout)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)