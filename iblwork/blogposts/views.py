import email
from multiprocessing import context
from re import I, template
from django.shortcuts import render
from django.http import HttpResponse

from .forms import SubscriberForm


# Create your views here.
def index(request):
    template = "posted/index.html"
    return render(request, template)

def Subscribe(request):
        form = SubscriberForm(request.POST)
        template=("posted/index.html")
        print(request.POST)
        return render(request, "posted/subscriber.html", {'form':form})
    

    #context={
       # "posted": BlogPost.objects.all()
    #}

    #return render(request, "posted/index.html", context)
