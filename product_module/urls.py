from django.contrib import admin
from django.urls import path
from product_module import views

urlpatterns = [
    path('products/',views.product_list,name="products"),
]
