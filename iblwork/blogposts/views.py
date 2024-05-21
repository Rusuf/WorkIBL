import email
from re import I, template

from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm


# Create your views here.
def index(request):
    template = "posted/index.html"
    return render(request, template, {})

def about(request):
      if request.method == 'POST':
            form = SubscriberForm(request.POST)
            if form.is_valid():
                  print("valid")
                  form.save()


def Subscribe(request):
                   
                  
        form = SubscriberForm()
        return render(request, 'posted/subscriber.html',{'form': form})


    

    #context={
       # "posted": BlogPost.objects.all()
    #}

    #return render(request, "posted/index.html", context)
