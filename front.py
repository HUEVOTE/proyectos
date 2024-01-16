from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_list, name='cart_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('admin/', admin.site.urls),
]