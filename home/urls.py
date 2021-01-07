
from django.urls import path
from django.views.generic import TemplateView
from home import views


urlpatterns = [
    # path('', TemplateView.as_view(template_name="home.html")),
    path('', views.Applist,name="Applist"),
    
]
