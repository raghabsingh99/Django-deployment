from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessREcord

# Create your views here.

def index(request):

    webpages_list = AccessREcord.objects.order_by('date')
    print(webpages_list)
    date_dict = {'access_records': webpages_list}

    
    return render(request,"first_app/index.html",context=date_dict)
   