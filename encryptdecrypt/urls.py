
from django.urls import path
from encryptdecrypt import views

urlpatterns = [
    path('', views.encdecHome,name="encdecHome"),
    
]
