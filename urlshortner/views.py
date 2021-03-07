from django.shortcuts import render

# Create your views here.
def urlshortner(request):
    return render(request,'urlshortner.html',{})