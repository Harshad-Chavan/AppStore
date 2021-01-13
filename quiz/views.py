from django.shortcuts import render
from .models import LeaderBoard

# Create your views here.
def quizHome(request):
    leaderboard = LeaderBoard.objects.all().order_by('-best_score')
    return render(request,'quiz_home.html',{'leaderboard':leaderboard})