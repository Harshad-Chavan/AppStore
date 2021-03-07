from django.shortcuts import render,HttpResponse,redirect
import uuid
from .models import Urls


# Create your views here.
def urlshortner(request):
    return render(request,'urlshortner.html',{})

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(link=url,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request,pk):
    url_details = Urls.objects.get(uuid=pk)
    return redirect (url_details.link)
