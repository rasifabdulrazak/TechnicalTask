from django.contrib import admin
from django.urls import path
from product_module import views

urlpatterns = [
    path('staff/',views.demo,name="staff"),
]
