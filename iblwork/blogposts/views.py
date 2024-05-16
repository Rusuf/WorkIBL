from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost



# Create your views here.
def index(request):
    template = "posted/index.html"
    return render(request, template)

    #context={
       # "posted": BlogPost.objects.all()
    #}

    #return render(request, "posted/index.html", context)
