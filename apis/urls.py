from django.urls import path
from . import views

urlpatterns = [

    path('api/getrange', views.getrange, name="getrange"),
    path('api/setrange', views.setrange, name="getrange"),
   
]