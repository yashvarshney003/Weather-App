from django.urls import include, path
from login import views
from rest_framework import routers

urlpatterns = [
    path("", views.cityweather, name="cityweather"),
    
    
     
    
]