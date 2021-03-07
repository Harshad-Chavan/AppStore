
from django.urls import path
from urlshortner import views

urlpatterns = [
    path('', views.urlshortner,name="urlshortner"),
    
]
