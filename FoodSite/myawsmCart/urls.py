from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="EcomSite"), 
    path('about',views.about_us,name="AboutUs")
  
]