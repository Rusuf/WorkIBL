from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost



# Create your views here.
def index(request):
    
    context={
        "posted": BlogPost.objects.all()
    }

    return render(request, "posted/index.html", context)
