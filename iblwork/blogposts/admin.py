from django.contrib import admin
from .models import BlogPost, Subscriber

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Subscriber)