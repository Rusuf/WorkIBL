import email
from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import SubscriberForm
from blogposts.forms import SubscriberForm


# Create your views here.
def index(request):
    template = "posted/index.html"
    return render(request, template, {})


     
def Subscribe(request):
        form = SubscriberForm(request.POST) 
        print(request.POST)
        if form.is_valid():
              form.save()
              
              return HttpResponse("Thank you for subscribing!")
        
        
        return render(request,'posted/subscriber.html', {'form': SubscriberForm})

    
        

     


                   
        


    

    #context={
       # "posted": BlogPost.objects.all()
    #}

    #return render(request, "posted/index.html", context)
