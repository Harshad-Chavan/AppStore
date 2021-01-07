from django.shortcuts import render

# Create your views here.
def Applist(request):
    apps = [
        {'name':'calculator','description':"this is used for calculation",'last_updated':"7/1/2020"},
        {'name':'calculator','description':"this is used for calculation",'last_updated':"7/1/2020"}
    
    ]
    return render(request,'home.html',{'apps' : apps})
