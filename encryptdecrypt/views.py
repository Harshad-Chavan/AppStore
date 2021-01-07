from django.shortcuts import render

# Create your views here.
def encdecHome(request):
    return render(request,'encdec_home.html',{})