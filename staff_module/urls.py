from django.contrib import admin
from django.urls import path
from staff_module import views


urlpatterns = [
    path('',views.home,name="home"),
    path('registration/',views.registration,name="registration"),
    path('login/',views.login,name="login"),
    path('listing/',views.staff_listing,name='listing'),
    path('add_staff/',views.add_staff,name="add_staff"),
    path('edit_staff/<int:pk>/',views.edit_staff,name="edit_staff"),

]
