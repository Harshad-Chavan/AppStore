from django.shortcuts import render
from .models import Apps
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def Applist(request):
    apps = Apps.objects.all()
    
    # apps = [
    #     {'name':'Calculator','description':"this is used for calculation",'last_updated':"7/1/2020"},
    #     {'name':'File encryptor ','description':"Used for file encryption",'last_updated':"7/1/2020"},
    #     {'name':'To do','description':"Track your tasks with the todo app",'last_updated':"7/1/2020"},
    #     {'name':'Quiz','description':"Take a basic quiz",'last_updated':"7/1/2020"}
    
    # ]
    return render(request,'home.html',{'apps' : apps})
