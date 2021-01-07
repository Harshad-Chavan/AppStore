from django.shortcuts import render

# Create your views here.
def quizHome(request):
    return render(request,'quiz_home.html',{})