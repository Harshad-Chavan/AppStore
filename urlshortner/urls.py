
from django.urls import path
from urlshortner import views

urlpatterns = [
    path('', views.urlshortner,name="urlshortner"),
    path('create', views.create,name="create"),
    path('<str:pk>', views.go,name="go"),
    
    
]
