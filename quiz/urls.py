
from django.urls import path
from quiz import views

urlpatterns = [
    path('', views.quizHome,name="quizHome"),
    
]
